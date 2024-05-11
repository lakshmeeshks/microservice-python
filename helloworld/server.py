from flask import Flask

app = Flask("My hello world Application")

@app.route("/")
def hello():
    return "Hello Worold"

if __name__ == "__main__":
    app.run(debug=True)
