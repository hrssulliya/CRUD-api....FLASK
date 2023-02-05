# In this file only make API using flask without database get(access) and post(insert)
from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name':'sansar',
        'items':[
            {
                'name':'kulfi',
                'price':30
            }
        ]
    },
    {
        'name':'aksa',
        'items':[
            {
                'name':'Room',
                'price':1200
            }
        ]
    },
]

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if (store['name']== name):
            return jsonify(store['name'])
    return jsonify({'massage':'Store not found'})

@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if (store['name']== name):
            return jsonify(store['items'])
    return jsonify({'massage':'Store not found'})

@app.route('/stores')
def get_all_store_name():
    return jsonify({'stores': stores})

@app.route('/store',methods=['POST'])
def create_store():
    req_data = request.get_json()
    new_store = {
    'name':req_data['name'],
    'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)
    

@app.route('/store/<string:name>/item',methods=['POST'])
def create_store_item(name):
    for store in stores:
        if (store['name']== name):
            req_data = request.get_json()
            new_item = {
            'name':req_data['name'],
            'price':req_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'massage':'Store not found'})

@app.route('/')
def home():
    return "hay"
app.run(debug=True, port=5500)


list_num = [16,17,4,3,5,2]
ls=[]
for x in range(0, len(list_num)):
    for j in range(x+1, len(list_num)):
        if list_num[x] <= list_num[j]:
            break
    if j == len(list_num)-1:
        ls.append(list_num[x])
print(ls)