from flask import Flask, jsonify
import requests

app = Flask(__name__)

# services IT wants to keep an eye on
SERVICES = {
    "intranet": "https://intranet.outbackcorp.internal/health",
    "payroll": "https://payroll.outbackcorp.internal/health",
    "wiki": "https://wiki.outbackcorp.internal/health",
}


@app.get("/status")
def status():
    results = {}
    for name, url in SERVICES.items():
        try:
            r = requests.get(url, timeout=5)
            results[name] = "up" if r.ok else f"down ({r.status_code})"
        except requests.RequestException:
            results[name] = "unreachable"
    return jsonify(results)
