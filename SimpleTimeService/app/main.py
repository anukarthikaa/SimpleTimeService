from flask import Flask, request, jsonify
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route('/')
def get_time_and_ip():
    utc_now = datetime.now(timezone.utc)
    ist_now = utc_now.astimezone(ZoneInfo("Asia/Kolkata"))
    
    return jsonify({
        "timestamp": ist_now.isoformat(),
        "ip": request.remote_addr,
        "timezone": "IST (UTC+5:30)"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)