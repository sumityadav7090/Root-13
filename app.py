from flask import Flask, render_template, request

app = Flask(__name__)
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form["message"]
        shift = 13
        for c in text:
            loc = alpha.find(c.upper())
            if loc == -1:
                result += c
            else:
                new_loc = (loc + shift) % 26
                result += alpha[new_loc]
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
