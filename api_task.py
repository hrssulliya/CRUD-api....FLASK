# In this file make API using flask with database get(access) and post(insert) put(update) and delete 
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///store.db"
db = SQLAlchemy(app)

class Product(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/ins', methods=['POST'])
def insert():
    req_data = request.get_json()
    for ins_item in req_data:
        new_item = {'item' : ins_item['name'],
        'price' : ins_item['price']}
        store = Product(item=new_item['item'], price=new_item['price'])
        db.session.add(store)
        db.session.commit()
    return jsonify(Product.query.all())


@app.route('/update/<string:item>', methods=['PUT'])
def update(item):
    inp_data = request.get_json()
    new_item = {'item' : inp_data['name'],
    'price' : inp_data['price']}
    store = Product.query.filter_by(item=item).first()
    store.item = new_item['item']
    store.price = new_item['price']
    db.session.add(store)
    db.session.commit()


@app.route('/delete/<string:item>', methods=['DELETE'])
def delete(item):
    store = Product.query.filter_by(item=item).first()
    db.session.delete(store)
    db.session.commit()
    # return jsonify(Product.query.all())


with app.app_context():
    db.create_all()

app.run(debug=True, port=5600)