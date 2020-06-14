from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        oslist = ["Windows", "Mac", "Linux"]
        return render_template("index.html", oslist=oslist)
    else:
        os = request.form["os"]
        print(os)
        oslist = ["Windows", "Mac", "Linux"]
        return render_template("index.html", oslist=oslist)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)