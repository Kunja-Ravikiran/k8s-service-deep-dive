from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <h1>Kubernetes Service Deep Dive 🚀</h1>
    <p><strong>Pod Name:</strong> {hostname}</p>
    <p>This response helps demonstrate load balancing.</p>
    """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

