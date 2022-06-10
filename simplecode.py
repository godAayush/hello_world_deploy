import flask

app=flask.Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return "hello duniya"

if __name__=='__main__':
    app.secret_key = "secret"
    app.debug = True
    app.run()