from flask import request ,redirect, render_template, url_for
from .model import Item
from app import app
from app import db



@app.route('/') 
def show(): 
    items = Item.query.all() 
  
    return render_template('main.html', inventory = items) 
  
  
@app.route('/add', methods=['POST']) 
def add(): 
    
    item = Item.query.filter_by(item_name = request.form['item']).first()
    #print(item.item_name)
    if item == None:
        new_item = Item(item_name = request.form['item'], count = int(request.form['count']))
        db.session.add(new_item)
    else:
        print(item.count)
        item.count += int(request.form['count'])
    db.session.commit()

  
    return redirect(url_for('show')) 
  
  
@app.route('/delete', methods = ['POST']) 
def delete(): 
    item = Item.query.filter_by(item_name = request.form['item']).first()
    
    if item != None and item.count>int(request.form['count']):

        item.count -= int(request.form['count'])
  
    
    db.session.commit() 
  
    return redirect(url_for('show')) 