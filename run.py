from flask import Flask

app=Flask(__name__)

@app.route("/")
def Homepage():
    return "hello patrick"
if __name__=="__main__":
    app.run(debug=True)