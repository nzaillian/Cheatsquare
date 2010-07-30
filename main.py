'''
Author: Nicholas Zaillian (http://www.columbia.edu/~naz2106)
License (see LICENSE.txt file in this directory)
'''

import foursquare
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_form import Ui_Login_Form
from checkin_form import Ui_Checkin_Form
from checkin_complete_form import Ui_Checkin_Success_Form
import pickle
import urllib2
import base64
import sys

DATA_FILE_NAME = "settings.data"

class SettingsManager(object):
	def __init__(self):
		self.remember_username = False
		self.remember_password = False
		self.username = None
		self.password = None

class FoursquareManager(object):
	def __init__(self):
		self.username = None
		self.password = None
		self.foursquare_obj = None
	
	def login(self, username=None, password=None):
		if username is None or password is None:
			self.foursquare_obj = foursquare.Foursquare(foursquare.BasicCredentials(self.username, self.password))
		else:
			self.foursquare_obj = foursquare.Foursquare(foursquare.BasicCredentials(username, password))
		#make sure authentication was effective
		try:
			self.foursquare_obj.user()
			
		#if authentication failed
		except foursquare.FoursquareRemoteException:
			return False
			
		#if we get to here, then authentication has not failed
		return True
			
#Presents username and password fields, as well as checkboxes giving the user the option of having username/password stored locally
#for subsequent recall.  Handles the serialization of username/password, as well as checkbox state,
#by working with a pickled SettingsManager object.
class LoginView(QFrame): 
	def __init__(self, parent=None, foursquare_manager=None):
		QFrame.__init__(self, parent)

		self.foursquare_manager = foursquare_manager
		self.form = Ui_Login_Form()
		self.form.setupUi(self)
		
		self.setObjectName("login_view")
		self.settings_manager = None
		
		self.resize(400,200)
		
		#get saved settings obj
		try:
			data_file = open(DATA_FILE_NAME, "r")
			self.settings_manager = pickle.load(data_file)
			data_file.close()
		except EOFError:
			print 'no stored settings.'
			#self.settings_manager = SettingsManager()
		
		#login fields
		self.username_field = self.form.username_field
		self.password_field = self.form.password_field
		
		#checkboxes
		self.remember_username_checkbox = self.form.remember_username_checkbox
		self.remember_password_checkbox = self.form.remember_password_checkbox
		
		#conceal password
		self.password_field.setEchoMode(QLineEdit.Password)
		
		#login button
		self.login_button = self.form.login_button
		self.login_button.setObjectName("login_button")
		
		
		#password management  
		self.remember_username_checkbox = self.form.remember_username_checkbox 
		self.remember_password_checkbox = self.form.remember_password_checkbox
		
		if self.settings_manager is not None and self.settings_manager.remember_username is True and self.settings_manager.username is not None:
			#check appropriate checkbox and fill in field
			self.remember_username_checkbox.setCheckState(Qt.Checked)
			self.username_field.setText(self.settings_manager.username)
			
		if self.settings_manager is not None and self.settings_manager.remember_password is True and self.settings_manager.password is not None:
			#check appropriate checkbox and fill in field
			self.remember_password_checkbox.setCheckState(Qt.Checked)
			self.password_field.setText(base64.b64decode(self.settings_manager.password))
			
		QObject.connect(self.remember_username_checkbox, SIGNAL("stateChanged(int)"),  self.save_settings)
		QObject.connect(self.remember_password_checkbox, SIGNAL("stateChanged(int)"), self.save_settings)
		QObject.connect(self.login_button, SIGNAL("clicked()"), self.save_settings)
			
	def save_settings(self):
		if self.settings_manager is None:
			self.settings_manager = SettingsManager()
			
		if self.remember_username_checkbox.checkState() == Qt.Checked:
			self.settings_manager.remember_username = True
			self.settings_manager.username = str(self.username_field.text())
		else: 
			self.settings_manager.remember_username = False
			
		if self.remember_password_checkbox.checkState() == Qt.Checked:
			self.settings_manager.remember_password = True
			self.settings_manager.password = base64.b64encode(str(self.password_field.text()))
		else:
			self.settings_manager.remember_password = False
			
		data_file = open(DATA_FILE_NAME, 'w')
		pickle.dump(self.settings_manager, data_file)
		data_file.close()

#Screen presented to the user if there is a login error.		
class LoginErrorView(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self)
		self.layout = QGridLayout()
		self.setLayout(self.layout)
		
		self.error_label = QLabel("A Login Error occurred.\n\nDouble check that the username and password you have entered \nare correct, and try again.")
		self.back_button = QPushButton(text="return to login screen")
		
		self.layout.addWidget(self.error_label, 0,0,1,3)
		self.layout.addWidget(self.back_button, 1,2,1,1)
	
#Pop-up that is presented when a user has been successfully checked into a venue.
#shows venue's icon, name, address, and the time of the checkin.	
class CheckinSucceededView(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.form = Ui_Checkin_Success_Form()
		self.form.setupUi(self)
		self.ok_button = self.form.ok_button
		self.venue_name_label = self.form.venue_name_label
		self.venue_address_label = self.form.venue_address_label
		self.checkin_date_label = self.form.checkin_date_label
		self.image_label = self.form.venue_icon_label
		self.hide()
		self.icon_pixmap = QPixmap()
		
		QObject.connect(self.ok_button, SIGNAL("clicked()"), self.hide)
		
	def checkin_succeeded(self, foursquare_obj):
		checkin_history = foursquare_obj.history(l=1)
		last_checkin = checkin_history['checkins']
		last_checkin = last_checkin[0]
		self.venue_name_label.setText(last_checkin['venue']['name'])
		self.venue_address_label.setText(last_checkin['venue']['address'])
		self.checkin_date_label.setText(str(last_checkin['created']))
		icon_url = last_checkin['venue']['primarycategory']['iconurl']
		icon_fp = urllib2.urlopen(icon_url)
		icon_data = icon_fp.read()
		icon_pixmap = QPixmap()
		icon_pixmap.loadFromData(icon_data)
		self.image_label.setPixmap(icon_pixmap)
		self.show()

#View showing recent checkins and presenting user with a VID field and button 
#allowing him/her to be checked into an arbitrary venue.		
class CheckinView(QFrame):
	def __init__(self, parent = None, foursquare_manager=None):
		QFrame.__init__(self, parent)
		self.form = Ui_Checkin_Form()
		self.form.setupUi(self)
		
		self.foursquare_manager = foursquare_manager
		self.recent_checkins = None
		self.setObjectName("checkin_view")
		
		self.recent_checkins_view = self.form.recent_checkins_view
		
		self.vid_text_field = self.form.vid_field
		self.checkin_button = self.form.checkin_button
	
		QObject.connect(self.recent_checkins_view, SIGNAL("currentRowChanged(int)"), self.handle_row_click)
		
	def handle_row_click(self):
		current_row = self.recent_checkins_view.currentRow()
		if self.recent_checkins is not None:
			self.vid_text_field.setText(str(self.recent_checkins[current_row]['venue']['id']))

	def update_checkin_list(self):
		history = self.foursquare_manager.foursquare_obj.history(l=20)
		self.recent_checkins = history['checkins']
		self.recent_checkins_view.clear()
		venue_counter = 0
		for item in self.recent_checkins:
			date_in_us_fmt = item['created'][0:item['created'].find("+0000")]
			details = item['venue']['name']+" ("+str(item['venue']['id'])+"), "+date_in_us_fmt+"GMT"
			self.recent_checkins_view.addItem(details)
			venue_counter += 1
	
#View presented in the case that an error occurs when application attempts to check user into venue.		
class CheckinErrorView(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.layout = QGridLayout()
		self.setLayout(self.layout)
		self.error_message_label = QLabel("An error occurred checking you in.\n\nMake sure that you have provided a valid VID.")
		self.okay_button = QPushButton("OK")

		self.layout.addWidget(self.error_message_label, 0,0,1,4)
		self.layout.addWidget(self.okay_button, 2, 3, 1, 1)

		QObject.connect(self.okay_button, SIGNAL("clicked()"), self.destroy)

#The main view.  Manages LoginView, CheckinView, CheckinSuccessView and associated error objects.		
class MainWindow(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.foursquare_manager = FoursquareManager()
		self.layout = QGridLayout()
		self.setLayout(self.layout)
		
		self.login_view = LoginView(foursquare_manager=self.foursquare_manager)
		self.checkin_view = CheckinView(foursquare_manager=self.foursquare_manager)
		self.login_error_view = LoginErrorView()
		self.checkin_success_view = CheckinSucceededView()
		
		self.layout.addWidget(self.login_view, 0,0,1,1)
		self.layout.addWidget(self.checkin_view, 0,0,1,1)
		self.layout.addWidget(self.login_error_view, 0,0,1,1)
		self.checkin_view.hide()
		self.login_error_view.hide()
		
		self.resize(500,340)
		self.setWindowTitle("Cheatsquare")
		
		QObject.connect(self.login_view.login_button, SIGNAL("clicked()"), self.login)
		QObject.connect(self.login_error_view.back_button, SIGNAL("clicked()"), self.revert_to_login_view)
		QObject.connect(self.checkin_view.checkin_button, SIGNAL("clicked()"), self.checkin_button_clicked)
		
	def login(self):
		self.foursquare_manager.username = self.login_view.username_field.text()
		self.foursquare_manager.password = self.login_view.password_field.text()
		login_result = self.foursquare_manager.login()
		if login_result is False:
			self.login_view.hide()
			self.login_error_view.show()
		else:
			self.login_view.hide()
			self.checkin_view.update_checkin_list()
			self.checkin_view.show()

	def revert_to_login_view(self):
		self.login_error_view.hide()
		self.login_view.show()
		
	def checkin_button_clicked(self):
		checkin_success = True
		try:
			remote_response = self.foursquare_manager.foursquare_obj.checkin(vid=int(self.checkin_view.vid_text_field.text()))
		except foursquare.FoursquareRemoteException:
			self.checkin_error_view = CheckinErrorView()
			self.checkin_error_view.show()
			checkin_success=False
		if checkin_success is True:
			self.checkin_success_view.checkin_succeeded(self.foursquare_manager.foursquare_obj)
			self.checkin_view.update_checkin_list()
			
#App initialization		
app = QApplication(sys.argv)
main_window = MainWindow() 
main_window.show()
sys.exit(app.exec_())