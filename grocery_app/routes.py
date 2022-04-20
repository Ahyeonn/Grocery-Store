from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
from grocery_app.forms import GroceryStoreForm, GroceryItemForm

# Import app and db from events_app package so that we can run app
from grocery_app.extensions import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    form = GroceryStoreForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            grocery_title = request.form.get('title')
            grocery_address = request.form.get('address')
        
            new_grocery = GroceryStore(title=grocery_title, address=grocery_address)

            db.session.add(new_grocery)
            db.session.commit()

            flash('Successfully Added!')
            return redirect(url_for('main.new_store'))
    
    return render_template('new_store.html', form=form)

@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    form = GroceryItemForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            item_name = request.form.get('name')
            item_price = request.form.get('price')
            item_category = request.form.get('category')
            photo_url = request.form.get('photo_url')
            store_id = int(request.form.get('store'))

            new_item = GroceryItem(name=item_name, price=item_price, category=item_category, photo_url=photo_url, store_id=store_id)

            db.session.add(new_item)
            db.session.commit()

            flash('Successfully Added!')
            return redirect(url_for('main.new_item'))

    return render_template('new_item.html', form=form)

@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    form = GroceryStoreForm(obj=store)

    if request.method == 'POST':
        if form.validate_on_submit():
            store.title = form.title.data
            store.address = form.address.data
            db.session.add(store)
            db.session.commit()

            flash('Successfully Updated!')
            return redirect(url_for('main.store_detail', store_id=store.id))

    return render_template('store_detail.html', store=store, form=form)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    form = GroceryItemForm(obj=item)

    if request.method == 'POST':
        if form.validate_on_submit:
            item.name = form.name.data
            item.price = form.price.data
            item.category = form.category.data
            item.photo_url = form.photo_url.data
            item.store = form.store.data

            db.session.add(item)
            db.session.commit()
            flash('Successfully Updated!')
            return redirect(url_for('main.item_detail', item_id=item.id))

    item = GroceryItem.query.get(item_id)
    return render_template('item_detail.html', item=item, form=form)

