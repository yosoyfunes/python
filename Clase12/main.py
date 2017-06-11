#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, render_template, json
from jinja2 import Template

app = Flask(__name__)

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]

posts = [ # fake array of posts
	        { 
	            'author': {'nickname': 'John'},
	            'body': 'Beautiful day in Portland!'
	        },
	        {
	            'author': {'nickname': 'Susan'},
	            'body': 'The Avengers movie was so cool!'
	        }
	    ]

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/form')
def form():
  return render_template('formulario.html', titulo = "Cargar STORES")

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items': [{
    	'name':  request_data['name'], 
    	'price': float(request_data['price']) 
    }]
  }
  stores.append(new_store)
  return jsonify(new_store)

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': 'store not found'})

#get /store
@app.route('/store')
def get_stores():
  return  render_template('store.html', titulo = "STORES", stores = json.dumps(stores), posts=posts)
  #json.dumps(stores)  jsonify(stores)

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Pagina No encontrada</h1>"

app.run(port=5000, debug=True)
