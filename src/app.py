from flask import Flask, jsonify, redirect

app = Flask(__name__)

@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "ok"}), 200

@app.route("/")
def root():
    return redirect("/characters")

@app.route("/characters")
def characters():
    data = [
        {"id": 1, "name": "Rick Sanchez"},
        {"id": 2, "name": "Morty Smith"},
        {"id": 3, "name": "Summer Smith"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


