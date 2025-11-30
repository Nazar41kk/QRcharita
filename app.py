from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/qr")
def qr():
    return render_template("qr.html")

@app.route("/finish")
def finish():
    return render_template("finish.html")

if __name__ == "__main__":
    app.run(debug=True)
