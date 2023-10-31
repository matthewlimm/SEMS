import json
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from random import random
from threading import Lock
from datetime import datetime
#from dht22_module import DHT22Module
from gmc320s_module import GMC320SModule
#from mics5524_module import MICS5524Module
from ltr390_module import LTR390Module
import board
import time

#dht22_module = DHT22Module(board.D4) # temperature and humidity
gmc320s_module = GMC320SModule() # radiation
#mics5524_module = MICS5524Module() # gas 
ltr390_module = LTR390Module() # uv, lux, etc.

#modules = [dht22_module, gmc320s_module]
# https://learn.adafruit.com/raspberry-pi-iot-dashboard-with-azure-and-circuitpython

thread = None     
thread_lock = Lock()

app = Flask(__name__)
app.config["SECRET_KEY"] = "alphatheta!"
socketio = SocketIO(app, cors_allowed_origins="*")

"""
Background Thread
"""
def background_thread():
    while True:
        #for module in modules:
        ts  = time.strftime("%l:%M:%S")
        #temperature, humidity = dht22_module.get_sensor_readings()
        cpm = gmc320s_module.get_sensor_readings()
        #co2 = mics5524_module.get_sensor_readings()
        lux = ltr390_module.get_sensor_readings()
        sensor_readings = {
            #"id": module.get_id(),
            "temperature": lux,
            "humidity": cpm,
            #"cpm": cpm,
        }
        sensor_json = json.dumps(sensor_readings)
        socketio.emit("updateSensorData", sensor_json)
        socketio.sleep(1)

"""
Serve root index file
"""

@app.route("/")
def index():
    return render_template("index.html") #, modules=modules)


"""
Decorator for connect
"""


@socketio.on("connect")
def connect():
    global thread
    print("Client connected")

    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)


"""
Decorator for disconnect
"""


@socketio.on("disconnect")
def disconnect():
    print("Client disconnected", request.sid)


# if __name__ == "__main__":
#     socketio.run(app, port=5000, host="0.0.0.0", debug=True)
