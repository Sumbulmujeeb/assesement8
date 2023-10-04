from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)


# Initialize the MySQL database connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="order_management"
)

# Sample data (you should replace this with a database)
users = []
products = []
orders = []

# Endpoint to register a user
@app.route('/registeruser', methods=['POST'])
def register_user():
    data = request.json
    users.append(data)
    return jsonify({'message': 'User registered successfully'}), 201

# Endpoint to get all products
@app.route('/getallproducts', methods=['GET'])
def get_all_products():
    return jsonify({'products': products}), 200

# Endpoint to place an order
@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    orders.append(data)
    return jsonify({'message': 'Order placed successfully'}), 201

# Endpoint to get all orders
@app.route('/allorders', methods=['GET'])
def get_all_orders():
    return jsonify({'orders': orders}), 200

# Endpoint to add a product
@app.route('/addproduct', methods=['POST'])
def add_product():
    data = request.json
    products.append(data)
    return jsonify({'message': 'Product added successfully'}), 201

# Endpoint to update a product
@app.route('/updateproduct/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Implement product update logic here
    return jsonify({'message': 'Product updated successfully'}), 200

# Endpoint to delete a product
@app.route('/deleteproduct/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Implement product deletion logic here
    return jsonify({'message': 'Product deleted successfully'}), 200

@app.route('/getuser/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        user_data = {
            'id': user[0],
            'username': user[1],
            'password': user[2]
        }
        return jsonify({'user': user_data}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

# Endpoint to get all users
@app.route('/getallusers', methods=['GET'])
def get_all_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users_data = [{'id': user[0], 'username': user[1], 'password': user[2]} for user in cursor.fetchall()]
    cursor.close()
    
    return jsonify({'users': users_data}), 200


if __name__ == '__main__':
    app.run(debug=True)
