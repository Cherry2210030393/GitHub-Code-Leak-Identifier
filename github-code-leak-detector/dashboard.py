from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

ALERTS_FILE = "alerts.json"


if not os.path.exists(ALERTS_FILE):
    with open(ALERTS_FILE, 'w') as f:
        json.dump([], f)

def load_alerts():
    with open(ALERTS_FILE, 'r') as f:
        return json.load(f)

def save_alert(alert):
    alerts = load_alerts()
    alert["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alerts.insert(0, alert)
    with open(ALERTS_FILE, 'w') as f:
        json.dump(alerts, f, indent=2)

@app.route('/')
def index():
    alerts = load_alerts()
    return render_template("dashboard.html", alerts=alerts)

@app.route('/add', methods=["POST"])
def add_alert():
    data = request.json
    if data:
        save_alert(data)
        return {"status": "Alert saved"}, 200
    return {"error": "No data received"}, 400

if __name__ == '__main__':
    app.run(debug=True)
