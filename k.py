import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "9579c6fb00ae4ceb973102635252204"

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result = {
            "city": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "temperature_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "feels_like_c": data["current"]["feelslike_c"]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "City not found or API error"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
