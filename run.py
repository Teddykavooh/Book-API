from flask import Flask,jsonify,request
from app.model import Books
from app.model import Users


books = Books()

app = Flask(__name__)

@app.route('/books', methods=["GET","POST"])
def index():
    if request.method == "POST":
        title = request.json.get("title", None)
        authors= request.json.get("authors", None)
        genre= request.json.get("genre", None)
        items= request.json.get("items", None)
       
        return books.post_a_book(title=title, authors=authors, genre=genre, items=items)

    return jsonify({"books": books.get_all_books()})

@app.route('/books/<int:book_id>')
def get_book(book_id):
    return jsonify({"books": books.get_a_book(book_id=book_id)})


users = Users()


@app.route('/users', methods=["GET", "POST"])
def start():
    if request.method == "POST":
        name = request.json.get("name", None)
        types = request.json.get("types", None)
        age = request.json.get("age", None)  

        return users.post_a_user(name=name, types=types, age=age)
    return jsonify({"users":users.get_users()}) 

@app.route('/users/<int:user_id>')
def get_a_user(user_id):
    return jsonify({"users": users.get_a_user(user_id=user_id)})

    
if __name__ == '__main__':
    app.run(debug=True)  