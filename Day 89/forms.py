from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional

class TaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[Optional()])
    priority = SelectField("Priority",
                           choices=[("High","High"),("Medium","Medium"),("Low","Low")],
                           default="Medium")
    category = StringField("Category", validators=[DataRequired()])
    due_date = DateField("Due Date", format="%Y-%m-%d", validators=[Optional()])
    submit = SubmitField("Save Task")
