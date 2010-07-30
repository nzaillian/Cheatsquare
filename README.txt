This application provides a simple, visual interface for the foursquare service (no formal affiliation).  More specifically, it provides a simple means of checking into arbitrary venues by VID.

A self-contained app bundle is available for download at http://www.columbia.edu/~naz2106/random/cheatsquare

If you would like to customize the application, you will need a copy of PyQt4 (available at http://www.riverbankcomputing.co.uk/software/pyqt) and, to create a standalone app bundle, a copy of py2app (http://svn.pythonmac.org/py2app/py2app/trunk/doc/index.html).

It is important to note that at present, py2app does not support x86_64, so if you would like to create a 64bit app bundle, you'll have to find some other way of doing it.

once you have satisfied the PyQt4 dependency, all you'll need to do to run the app is invoke:
"python main.py"

To create a standalone app bundle:
"python setup.py py2app"

This will drop the app bundle in the 'dist' directory.

SCRIPTS:

I've included a number of useful scripts related to building the app in the 'script' directory.

If you modify any of the .ui files using Qt designer, you'll need to run 'script/make_forms.sh' to reconstruct the corresponding .py files and see the results of your modifications when the application runs.


If you intend to commit any code to the public github repository for this project, you should run 'script/delete_stored_settings.sh' before doing so.  This script clears the settings.data file, which may otherwise include the foursquare username (in pain text) and password (encoded in base64) that you have been using to test the application.

(MAC ONLY:)

You should run the 'script/clean.sh' script after you build the app bundle and before you rebuild it, to clean out the 'build' and 'dist' directories.

For reasons that are beyond me, py2app includes a number of massive debug files when it builds app bundles for programs that leverage PyQt, and you will notice that once you have run 'python setup.py py2app', the app bundle that is generated and placed in the 'dist' directory is over 200mb in size.  'script/remove_debug_files_from_app_bundle.sh' will remove the superfluous debug files and shrink the app bundle to ~50mb.
