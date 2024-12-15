from flask import request, jsonify, Blueprint
from app.utils.gen_ai import generate_response

# Create a Blueprint for the routes
api = Blueprint("api", __name__)

@api.route("/itinerary", methods=["GET", "POST"])
def itinerary():
  if request.method == "GET":
    return jsonify({
      "status": "success",
      "message": "Welcome to the Itinerary Planner API"
    })
  
  body = request.get_json()

  user_preferences = {
    "start_location": body.get("start_location", "N/A"),
    "specific_locations": body.get("specific_locations", "N/A"),
    "number_of_days": body.get("number_of_days", "N/A"),
    "preferred_modes_of_travel": body.get("preferred_modes_of_travel", "N/A"), # car, bus, train, plane, boat, bike, walk
    "budget_range": body.get("budget_range", "any"), # low, medium, high, any
    "travel_companions": body.get("travel_companions", "N/A"), # family, friends, solo, couple, group
    "trip_type": body.get("trip_type", "N/A"), # vacation, business, family, friends, solo, couple, group
    "interests": body.get("interests", "N/A"), # history, art, food, shopping, nature, adventure, relaxation, nightlife, sports, culture
    "travel_pace": body.get("travel_pace", "N/A"), # fast, moderate, easy
    "constraints": body.get("constraints", "None"),
    "special_notes": body.get("special_notes", "None")
  }

  try:
    response = generate_response(user_preferences)
    return jsonify({
      "status": "success",
      "data": response
    })
  except Exception as e:
    return jsonify({"error": str(e)}), 400