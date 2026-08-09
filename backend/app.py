from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Smart Parking Backend is running",
        "status": "success"
    })

@app.route("/parking")
def parking():
    return jsonify({
        "parking_lots": [
            {
                "name": "City Center Parking",
                "available_spaces": 25
            },
            {
                "name": "Railway Station Parking",
                "available_spaces": 12
            },
            {
                "name": "Shopping Mall Parking",
                "available_spaces": 40
            }
        ]
    })

@app.route("/traffic")
def traffic():
    return jsonify({
        "congestion_level": "Moderate",
        "vehicle_count": 145
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)