from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Render the index.html file
    return render_template("index.html")

if __name__ == "__main__":
    # Run the app on port 5000
    app.run(host="0.0.0.0", port=5001, debug=True)
