#!/usr/bin/python3
from legotrain import *
import sys
import bottle
from bottle import route, request, response, template, static_file

app = bottle.Bottle()

# Change IPADDRESS if access is required from another computer
IPADDRESS = 'localhost'
# Where the files are stored
DOCUMENT_ROOT = '/home/pi/iot-train'

# public files
# *** WARNING ANYTHING STORED IN THE PUBLIC FOLDER WILL BE AVAILABLE TO DOWNLOAD 
@app.route ('/public/<filename>')
def server_public (filename):
    return static_file (filename, root=DOCUMENT_ROOT+"/public")

@app.route ('/')
def server_home ():
    return static_file ('index.html', root=DOCUMENT_ROOT+"/public")

@app.route ('/control')
def control_train():
    getvar_dict = request.query.decode()
    speed = int(request.query.speed)
    if (speed >=0 and speed <= 7):
        train_set_speed(speed)
        return 'Speed changed to '+str(speed)
    else:
        return 'Invalid command'



app.run(host=IPADDRESS)
