from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("CALLKARO_API_KEY")
BASE_URL = os.getenv("CALLKARO_BASE_URL")
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "CallKaro Backend is running",
        "endpoints": {
            "health": "GET /health",
            "outbound_call": "POST /call/outbound"
        }
    }), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/call/outbound", methods=["POST"])
def outbound_call():
    data = request.json or {}

    # Required fields
    if "to_number" not in data:
        return jsonify({
            "status": "error",
            "message": "Missing required field: to_number"
        }), 400

    if "agent_id" not in data:
        return jsonify({
            "status": "error",
            "message": "Missing required field: agent_id"
        }), 400

    # Build payload dynamically (only send what exists)
    payload = {
        "to_number": data["to_number"],
        "agent_id": data["agent_id"]
    }

    optional_fields = [
        "batch_id",
        "metadata",
        "schedule_at",
        "min_trigger_time",
        "max_trigger_time",
        "carry_over",
        "number_of_retries",
        "gap_between_retries",
        "priority",
        "language"
    ]

    for field in optional_fields:
        if field in data:
            payload[field] = data[field]

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": API_KEY
    }

    try:
        response = requests.post(
            f"{BASE_URL}/call/outbound",
            json=payload,
            headers=headers,
            timeout=10
        )

        return jsonify(response.json()), response.status_code

    except requests.exceptions.Timeout:
        return jsonify({
            "status": "error",
            "message": "CallKaro API timeout"
        }), 500

    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)