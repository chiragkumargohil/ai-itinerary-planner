from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# import blueprints
from app.controllers.itinerary_planner import api

# load environment variables
load_dotenv()

# create the Flask app
app = Flask(__name__)

# apply CORS to this app
CORS(app)

# register the blueprint routes
app.register_blueprint(api, url_prefix="/api")