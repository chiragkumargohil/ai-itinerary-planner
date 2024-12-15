# AI Itinerary Planner

This is a Python Flask application that leverages **LangChain** and **Gemini AI** to create personalized travel itineraries. Users can input details such as their starting point, specific locations, trip type, number of days, travel companions, and other preferences, and the application generates an AI-driven travel itinerary.

---

## Features

- **AI-Powered Itinerary Generation**: Uses LangChain's prompt templates and Gemini AI to generate tailored travel plans based on user inputs.
- **Customizable Inputs**: Accepts user preferences like starting location, travel mode, trip type, budget, and special notes.
- **Flask Backend**: Simple and scalable API built with Flask.

---

## Requirements

- Python 3.8+
- Git Bash (for running the installation script on Windows)

---

## Installation

### Windows (Using Git Bash)

To set up the project on a Windows system, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/chiragkumargohil/ai-itinerary-planner.git
   cd ai-itinerary-planner
   ```

2. Run the initialization script:
   ```bash
   sh init.sh
   ```

   This script will:
   - Create a virtual environment.
   - Install all required dependencies (like Flask, LangChain, etc.).

3. Start the Flask server:
   ```bash
   python run.py
   ```

### For Other Platforms

You can manually set up the project:

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/chiragkumargohil/ai-itinerary-planner.git
   cd ai-itinerary-planner
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate     # For Windows (Command Prompt)
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python run.py
   ```

---

## Usage

1. Access the application and make an API request to `http://127.0.0.1:8888/api/itinerary`.
2. Provide inputs like:
   - **Start Location**: Your starting city.
   - **Specific Locations**: Places you want to visit.
   - **Trip Type**: Cultural, Adventure, Family, etc.
   - **Number of Days**: Duration of the trip.
   - **Preferred Modes of Travel**: Bus, Train, Flight, etc.
   - **Budget Range**: Low, Moderate, High.
   - **Travel Companions**: Family, Friends, Solo, etc.
   - **Interests**: Food, History, Nature, etc.
   - **Travel Pace**: Easy, Normal, Fast.
   - **Special Notes**: Any additional requirements.
3. Submit the form to receive a detailed AI-generated itinerary.

---

## Dependencies

- **Flask**: Web framework for building the API.
- **LangChain**: Framework for building chains of prompts.
- **Gemini AI**: Language model API for itinerary generation.
- Additional libraries listed in `requirements.txt`.

---

## Example API Request

**Endpoint**: `POST /api/itinerary`

**Request Body**:
```json
{
  "start_location": "Vadodara",
  "specific_locations": "Dwarka, Somnath, Gir Forest, Diu",
  "number_of_days": 5,
  "preferred_modes_of_travel": "Car",
  "budget_range": "moderate",
  "travel_companions": "Family",
  "trip_type": "Cultural",
  "interests": "Food",
  "travel_pace": "Normal",
  "constraints": "None",
  "special_notes": "Please include a visit to the local markets."
}
```

**Response**:
```json
{
  "status": "success",
  "data": "Day 1: Vadodara to Dwarka\nDay 2: Dwarka to Somnath\nDay 3: Somnath to Gir Forest\nDay 4: Gir Forest to Diu\nDay 5: Diu to Vadodara\n\nPlease include a visit to the local markets."
}
```

---

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

---

## Contact

If you have any questions or feedback, feel free to reach out!

---

Happy Traveling! 🌍