import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
BOOKS_API_URL = os.getenv('BOOKS_API_URL', 'http://bookss-api-server.f6erhqa8aqc7anbs.uksouth.azurecontainer.io:5000/books')

@app.route('/', methods=['GET'])
def index():
    # Render an HTML form for inputting search criteria
    return render_template('search_form.html')

@app.route('/books', methods=['GET'])
def get_books():
    # Extract search criteria from query parameters
    # genre = request.args.get('genre', '')
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
    # response = requests.get(f"{BOOKS_API_URL}?genre={genre}")
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
            filtered_books = books

        # return jsonify(filtered_books)
        
        return render_template('search_result.html', books=filtered_books)

    else:
        return jsonify({"error": "Bad response from the first service"}), 500

if __name__ == '__main__':
    app.run(debug=True)
