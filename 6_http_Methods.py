### http methods
# flask http method -> GET , POST , PUT , PATCH , DELETE

# Creating APIs with Flask and testing in Postman

from flask import Flask, jsonify, request

app = Flask(__name__)

# temp database
# Python List of Dictionary

books = [
    {
        "id": 1,
        "title": "Programming Challenges",
        "Author": "Ratan Sharma"
    },
    {
        "id": 2,
        "title": "The Indian Economy",
        "Author": "Kishan Dwivedi"
    },
    {
        "id": 3,
        "title": "DSA with Python",
        "Author": "Shivam Singh"
    },
    {
        "id": 4,
        "title": "DevOps made Easy",
        "Author": "Manish Pandey"
    },
    {
        "id": 5,
        "title": "EasyIOT",
        "Author": "Ritesh"
    },
    {
        "id": 6,
        "title": "Communicate Effectively",
        "Author": "Sudhanshu Sid"
    },
]


@app.route('/', methods=['GET'])
def homePage():
  return jsonify("Welcome to the Flask book API")


# route to get all the books


@app.route('/books', methods=['GET'])
def get_books():
  return jsonify(books)


# http://127.0.0.1:5000/books


# route to get a specific books by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
  for book in books:
    if book['id'] == book_id:
      return jsonify(book)

  return {'error': 'Book not found'}


# http://127.0.0.1:5000/books/1


# Route to add new book
@app.route('/books', methods=['POST'])
def add_book():
  newBook = {
      "id": request.json['id'],
      "title": request.json['title'],
      "Author": request.json['Author']
  }
  books.append(newBook)
  return jsonify({'message': 'Book added successful'})


# send post request through Postman http://127.0.0.1:5000/books
# {"id":7 , "title":"Java Explore" , "Author": "Love Hater"}


# Route to update existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
  for book in books:
    if book['id'] == book_id:
      book['title'] = request.json['title']
      book['Author'] = request.json['Author']
      return jsonify({'message': 'Book added successful'})

  return {'error': 'Book not found'}


# send put request through postman http://127.0.0.1:5000/books/7
# {"title":"C++ STL" , "Author": "Ratan"}


# Route to delete book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
  for book in books:
    if book['id'] == book_id:
      books.remove(book)
      return jsonify({'message': 'Book deleted successful'})

  return {'error': 'Book not found'}


# send delete request through postman http://127.0.0.1:5000/books/7

if __name__ == "__main__":
  app.run(debug=True)
