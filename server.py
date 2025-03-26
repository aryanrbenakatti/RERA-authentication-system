from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SUREPASS_API_KEY = "your_surepass_api_key" 
SUREPASS_URL = "https://api.surepass.io/api/v1/rera/verify"

@app.route("/verify_rera", methods=["POST"])
def verify_rera():
    data = request.get_json()
    rera_id = data.get("rera_id")

    if not rera_id:
        return jsonify({"error": "RERA ID is required"}), 400

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SUREPASS_API_KEY}"
    }

    payload = {"rera_id": rera_id}

    try:
        response = requests.post(SUREPASS_URL, json=payload, headers=headers)
        result = response.json()

        if result.get("status") == "success":
            return jsonify({"verified": True, "details": result.get("data")})
        else:
            return jsonify({"verified": False, "message": result.get("message")})

    except Exception as e:
        return jsonify({"error": "Failed to verify RERA ID"}), 500

if __name__ == "__main__":
    app.run(debug=True)
