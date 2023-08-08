from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_restful import Api

import pyodbc
import constants
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

# global connection obj used in each sql query

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
def drop_table(table_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        conn.commit()
        print(f"Table '{table_name}' successfully dropped.")
    except sqlite3.Error as e:
        print(f"Error dropping table '{table_name}': {e}")
    finally:
        conn.close()

def create_table():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT  NULL, preview TEXT  NULL, photos TEXT  NULL, description TEXT  NULL, size INT  NULL, isAccessory TEXT  NULL, brand TEXT  NULL, price INT  NULL)')
    conn.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, postid INT NULL, name TEXT  NULL, preview TEXT  NULL, description TEXT  NULL, brand TEXT  NULL, price INT  NULL)')
    conn.commit()
    conn.close()

@app.route('/posts')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY id DESC').fetchall()
    conn.close()
    posts_json = []
    for post in posts:
        posts_json.append({
            'id': post['id'],
            'name': post['name'],
            'preview': post['preview'],
            'photos': post['photos'],
            'description': post['description'],
            'size': post['size'],
            'isAccessory': post['isAccessory'],
            'brand': post['brand'],
            'price': post['price']
        })
    return jsonify(posts_json)
@app.route('/posts/<int:id>', methods=['GET'])
def get_post_by_id(id):
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM posts WHERE id = ?', (id,))
    post = cursor.fetchone()
    conn.close()

    if post is None:
        return jsonify({'message': 'Post not found'}), 404

    post_json = {
        'id': post['id'],
            'name': post['name'],
            'preview': post['preview'],
            'photos': post['photos'],
            'description': post['description'],
            'size': post['size'],
            'isAccessory': post['isAccessory'],
            'brand': post['brand'],
            'price': post['price']
    }
    return jsonify(post_json)

@app.route('/add', methods=['POST'])
def add_post():
    data = request.get_json()  # Assuming the client sends a JSON object in the request body

    name = data.get('name', '')
    photos = data.get('photos', '')
    preview = data.get('preview', '')
    description = data.get('description', '')
    size = 1
    isAccessory = 'false'
    brand = data.get('brand', '')
    price = data.get('price', 0)

    conn = get_db_connection()
    conn.execute('INSERT INTO posts (name, preview, photos, description, size, isAccessory, brand, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                 (name, preview, photos, description, size, isAccessory, brand, price))
    conn.commit()
    conn.close()

    return jsonify({'response': "Success"})

@app.route('/add-order', methods=['GET', 'POST'])
def add_order():
    #drop_table('posts')
    create_table()
    data = request.get_json()
    name = data['name'] 
    postid= data['postid'] 
    description = data['description'] 
    brand = data['brand'] 
    price = data['price'] 

    conn = get_db_connection()
    conn.execute('INSERT INTO orders (name, postid,description,brand,price) VALUES (?, ?, ?, ?, ?)', (name, postid,description,brand,price))
    conn.commit()
    conn.close()
       

    return jsonify({'response': "Success"})

@app.route('/delete/post/<int:id>')
def delete_post(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete/order/<int:id>')
def delete_order(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM orders WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/orders')
def orders():
    conn = get_db_connection()
    orders = conn.execute('SELECT * FROM orders ORDER BY id DESC').fetchall()
    conn.close()
    posts_json = []
    for order in orders:
        posts_json.append({
            'id': order['id'],
            'name': order['name'],
            'description': order['description'],
            'postid': order['postid'],
            'brand': order['brand'],
            'price': order['price']
        })
    return jsonify(posts_json)
#define main and add the API endpoints
def __main__():
    api.add_resource(index, '/posts')
    api.add_resource(orders, '/orders')
    api.add_resource(add_post, '/add')
    api.add_resource(add_order, '/add-order')
    api.add_resource(delete_post, '/delete')
    api.add_resource(delete_order, '/delete/order/<int:id>')
    
    

    
if __name__ == "__main__":
    app.run(host='localhost', port='1222', debug=True, threaded=True)

