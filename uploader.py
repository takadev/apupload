from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

f = drive.CreateFile({'title': '', 'mimeType': ''})
f.SetContentFile('test.jpg')
f.Upload()
