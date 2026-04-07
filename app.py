# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/user/<name>")
# def Home(name):
#     # name = "Jeet Jana"
#     return render_template("index.html",username = name)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])

def Home():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form.get("email")
        password = request.form.get("password")

        if username == "Jeet Jana" and password == "333":

            return render_template("index.html",username = username)
    
    return render_template("base.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)
