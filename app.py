import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
BOOKS_API_URL = os.getenv('BOOKS_API_URL', 'http://bookss-api-server.f6erhqa8aqc7anbs.uksouth.azurecontainer.io:5000/books')

@app.route('/books', methods=['GET'])
def get_books():
    genre = request.args.get('genre', default=None, type=str)
    '''
    genre = request.args.get('genre', type=str)
    author = request.args.get('author', type=str)
    
    # Construct the query parameters to be sent to the API
    query_params = {}
    if genre:
        query_params['genre'] = genre
    if author:
        query_params['author'] = author
    # Add more parameters to the dictionary as needed
    '''

    # Replace this URL with the actual URL of your first service
    # response = requests.get(BOOKS_API_URL, params=query_params)
    response = requests.get(BOOKS_API_URL)
    if response.ok:
        '''
        return jsonify(response.json())
        '''
        books = response.json()
        
        # If a genre is specified, filter the books by that genre
        if genre:
            filtered_books = [book for book in books if book['genre'].lower() == genre.lower()]
        else:
            # If no genre is specified, return the third book
            filtered_books = books[2] if len(books) >= 3 else None

        return jsonify(filtered_books)
        

    else:
        return jsonify({"error": "Bad response from the first service"}), 500

if __name__ == '__main__':
    app.run(debug=True)
