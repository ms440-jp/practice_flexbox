from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print("POST")
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)