from flask import Flask,render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user
import stripe

app=Flask(__name__)
app.config["SECRET_KEY"]="secret-key"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:////Users/somitagarwal/Desktop/Python/Day 97/instance/shop.db"

db=SQLAlchemy(app)
login_manager=LoginManager(app)

stripe.api_key="YOUR_STRIPE_SECRET_KEY"

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True)
    password=db.Column(db.String(255))

class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    price=db.Column(db.Integer)
    image=db.Column(db.String(300))

@login_manager.user_loader
def load_user(uid):
    return db.session.get(User,int(uid))

@app.route("/")
def home():
    return render_template("index.html",products=Product.query.all())

@app.route("/checkout/<int:pid>")
@login_required
def checkout(pid):
    p=Product.query.get_or_404(pid)
    session=stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data":{
                "currency":"usd",
                "product_data":{"name":p.name},
                "unit_amount":p.price*100},
            "quantity":1}],
        mode="payment",
        success_url=url_for("success",_external=True),
        cancel_url=url_for("home",_external=True))
    return redirect(session.url)

@app.route("/success")
def success():
    return "<h2>Payment Successful!</h2>"

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
