#######
#
# app.py
#######

from flask import Flask, render_template, request, redirect, url_for, make_response
import initio
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD) #set up GPIO
initio.init()
speed = 60

app = Flask(__name__) #set up flask server

#when the root IP is selected, return index.html page
@app.route('/')
def index():

	return render_template('index.html')

#recieve which pin to change from the button press on index.html
#each button returns a number that triggers a command in this function
#
#Uses methods from initio.py to send commands to the GPIO to operate the initio
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) #cast changepin to an int

	if changePin == 1:
		initio.spinLeft(speed)
	elif changePin == 2:
		initio.forward(speed)
	elif changePin == 3:
		initio.spinRight(speed)
	elif changePin == 4:
		initio.reverse(speed)
	else:
		initio.stop()


	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000
