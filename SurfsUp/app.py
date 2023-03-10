# Import all dependencies: 
################################################# 

import numpy as np

import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify 

# Create connection to Hawaii.sqlite file
#################################################

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# # Save references to the measurement and station tables in the database
Measurement = Base.classes.measurement
Station = Base.classes.station

# Initialize Flask
#################################################
app = Flask(__name__)

# Create Flask Routes 

# Create root route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Note: to access values between a start and end date enter both dates using format: YYYY-mm-dd/YYYY-mm-dd"
    )

# Create a route that queries precipiation levels and dates and returns a dictionary using date as key and precipation as value
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation (prcp)and date (date) data"""
    
    # Create new variable to store results from query to Measurement table for prcp and date columns
    precipitation_query_results = session.query(Measurement.prcp, Measurement.date).all()

    # Close session
    session.close()

