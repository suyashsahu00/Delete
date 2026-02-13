from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'Django Basics'},
    {'id': 2, 'title': 'Python Guide'}
]

# GET /books/ - List all books
@app.route('/books/', methods=['GET'])
def get_books():
    return jsonify(books), 200

# GET /books/<id>/ - Get single book details
@app.route('/books/<int:id>/', methods=['GET'])
def get_book(id):
    book = next((b for b in books if b['id'] == id), None)
    if book:
        return jsonify(book), 200
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    print("Server starting at http://127.0.0.1:5000/books/")
    app.run(debug=True)
