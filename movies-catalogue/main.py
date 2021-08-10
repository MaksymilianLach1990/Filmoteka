from flask import Flask, render_template


app = Flask(__name__)
app.config["ENV"] = "development"


@app.route('/')
def homepage():
    movies = ["Spider-man", "Batman", "Red", "Superman"]
    return render_template("homepage.html", movies=movies)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
