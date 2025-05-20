import requests

def send_alert(alert_data):
    try:
        response = requests.post("http://localhost:5000/add", json=alert_data)
        if response.status_code == 200:
            print("✅ Alert sent to dashboard.")
        else:
            print(f"❌ Failed to send alert. Status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending alert: {e}")
