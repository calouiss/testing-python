from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# --- Logging Setup ---
logging.basicConfig(
    filename="bookstore.log",          # log file name
    level=logging.INFO,                # log only INFO+
    format="%(asctime)s %(message)s"   # include timestamp
)

# --- Data (list of books) ---
books = ["Book", "Pen", "Notebook", "Diary"]

# --- Route to get all books ---
@app.route('/books', methods=['GET'])
def get_books():
    # log each request (timestamp handled by logging)
    logging.info("HTTP Method: %s", request.method)
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
