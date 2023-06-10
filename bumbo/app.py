from api import API


app = API()


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route("/home")
def home2(request, response):
    response.text = "Hello from the SECOND HOME page"