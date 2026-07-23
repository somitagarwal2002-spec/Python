from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Cafe
from forms import CafeForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes)

@app.route("/cafes")
def cafes():
    return render_template("cafes.html", cafes=Cafe.query.order_by(Cafe.name).all())

@app.route("/cafe/<int:cafe_id>")
def cafe(cafe_id):
    return render_template("cafe.html", cafe=Cafe.query.get_or_404(cafe_id))

@app.route("/add", methods=["GET","POST"])
def add_cafe():
    form=CafeForm()
    if form.validate_on_submit():
        cafe=Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )
        db.session.add(cafe)
        db.session.commit()
        flash("Cafe Added Successfully!","success")
        return redirect(url_for("cafes"))
    return render_template("add_cafe.html", form=form)

@app.route("/edit/<int:cafe_id>", methods=["GET","POST"])
def edit_cafe(cafe_id):
    cafe=Cafe.query.get_or_404(cafe_id)
    form=CafeForm(obj=cafe)
    if form.validate_on_submit():
        form.populate_obj(cafe)
        db.session.commit()
        flash("Cafe Updated!","success")
        return redirect(url_for("cafe", cafe_id=cafe.id))
    return render_template("edit_cafe.html", form=form)

@app.route("/delete/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe=Cafe.query.get_or_404(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    flash("Cafe Deleted!","danger")
    return redirect(url_for("cafes"))

if __name__=="__main__":
    app.run(debug=True)
