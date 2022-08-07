
#########Commenting out the hellow world lesson code######

#import dependancies
#from flask import Flask

#Create a New Flask App Instance
#app = Flask(__name__)

#Create Flask Routes, the decorator thing
#@app.route('/')
#def hello_world():
#    return 'Hello world'

#########################################      STARTIN 9.5.1             ########


###   Python Dependancies   ###
import numpy as np
import pandas as pd

####     Database dependancies      #####
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

###   Flask Dependancies   ###
from flask import Flask, jsonify

#####################    Set Up the Database     #####

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#############################    Set Up FLASK     #####
import app

app = Flask(__name__)


print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

#############################  Create the Welcome Route   ####

@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')