from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        code = request.form['code']
        description = request.form['description']
        price = float(request.form['price'])

        new_product = Product(name=name, code=code, description=description, price=price)
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    product = Product.query.get(id)

    if request.method == 'POST':
        product.name = request.form['name']
        product.code = request.form['code']
        product.description = request.form['description']
        product.price = float(request.form['price'])

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', product=product)

@app.route('/delete/<int:id>')
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
