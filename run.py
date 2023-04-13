from flask import Flask

app=Flask(__name__)

@app.route("/")
def Homepage():
    return "hello patri c k"
if __name__=="__main__":
    app.run(debug=True)