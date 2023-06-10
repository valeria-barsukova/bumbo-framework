from api import API


app = API()


@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"

    def delete(self, req, resp):
        resp.text = "Delete Book"

    def put(self, req, resp):
        resp.text = "Endpoint to update a book"

def handler(req, resp):
    resp.text = "sample"

app.add_route("/sample", handler)

@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html",
        context={"name": "Bumbo", "title": "Best Framework"}
    ).encode()

