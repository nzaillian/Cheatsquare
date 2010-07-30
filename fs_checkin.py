#!/usr/bin/python
import foursquare

checkin_vid = #place VID here
checkin_username = #place username here, enclosed in quotation marks
checkin_password = #place password here, enclosed in quotation marks

fs = foursquare.Foursquare(foursquare.BasicCredentials(checkin_username, checkin_password))
fs.checkin(vid=checkin_vid)