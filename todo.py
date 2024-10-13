from flask import Blueprint, jsonify, request
from middleware.auth import token_required

todo_bp = Blueprint('todo', __name__)

# In-memory storage for books (mimics a database)
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "published_year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "published_year": 1960}
]

# Helper function to find a book by ID
def find_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

# GET all books
@todo_bp.route('/books', methods=['GET'])
def get_books():
    token_check = token_required()
    if token_check == True:
        return jsonify(books), 200
    return token_check  # Return token error if invalid

# POST to add a new book
@todo_bp.route('/books', methods=['POST'])
def add_book():
    token_check = token_required()
    if token_check == True:
        data = request.get_json()

        # Validate input
        if not data.get('title') or not data.get('author'):
            return jsonify({'error': 'Title and author are required!'}), 400

        # Create a new book
        new_book = {
            "id": len(books) + 1,
            "title": data['title'],
            "author": data['author'],
            "genre": data.get('genre', ''),
            "published_year": data.get('published_year', '')
        }
        books.append(new_book)
        return jsonify(new_book), 201
    return token_check  # Return token error if invalid

# PUT to update a book
@todo_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    token_check = token_required()
    if token_check == True:
        book = find_book(book_id)
        if not book:
            return jsonify({'error': 'Book not found!'}), 404

        data = request.get_json()
        book.update({
            "title": data.get('title', book['title']),
            "author": data.get('author', book['author']),
            "genre": data.get('genre', book['genre']),
            "published_year": data.get('published_year', book['published_year'])
        })
        return jsonify(book), 200
    return token_check  # Return token error if invalid

# DELETE a book by ID
@todo_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    token_check = token_required()
    if token_check == True:
        book = find_book(book_id)
        if not book:
            return jsonify({'error': 'Book not found!'}), 404
        books.remove(book)
        return jsonify({'message': 'Book deleted!'}), 200
    return token_check  # Return token error if invalid
