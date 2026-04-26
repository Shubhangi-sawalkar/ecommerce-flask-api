from flask import Blueprint, request, jsonify
from models import Product
from database.db import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/add-product', methods=['POST'])
def add_product():
    data = request.json

    product = Product(
        name=data['name'],
        price=data['price']
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product added"})


@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()

    output = []
    for p in products:
        output.append({
            "id": p.id,
            "name": p.name,
            "price": p.price
        })

    return jsonify(output)