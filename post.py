from flask import Flask, request

app = Flask(__name__)

books = []

@app.route('/books/', methods=['POST'])  # 👈 THIS LINE IS CRUCIAL!
def create_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'title': data['title']
    }
    books.append(new_book)
    return new_book, 201

if __name__ == '__main__':
    app.run(debug=True)
