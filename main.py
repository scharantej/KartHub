
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret'

products = [
    {'id': 1, 'name': 'Product 1', 'price': 10},
    {'id': 2, 'name': 'Product 2', 'price': 20},
    {'id': 3, 'name': 'Product 3', 'price': 30},
]

cart = []

@app.route('/')
def products_page():
    return render_template('products.html', products=products)

@app.route('/cart')
def cart_page():
    return render_template('cart.html', cart=cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    product = [p for p in products if p['id'] == int(product_id)][0]
    cart.append({'product': product, 'quantity': int(quantity)})
    flash('Product added to cart')
    return redirect(url_for('products_page'))

@app.route('/update_cart', methods=['POST'])
def update_cart():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    for item in cart:
        if item['product']['id'] == int(product_id):
            item['quantity'] = int(quantity)
    flash('Cart updated')
    return redirect(url_for('cart_page'))

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = request.form.get('product_id')
    for item in cart:
        if item['product']['id'] == int(product_id):
            cart.remove(item)
    flash('Product removed from cart')
    return redirect(url_for('cart_page'))

@app.route('/checkout', methods=['POST'])
def checkout():
    # Handle payment and redirect to confirmation page
    return redirect(url_for('confirmation_page'))

@app.route('/confirmation')
def confirmation_page():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
