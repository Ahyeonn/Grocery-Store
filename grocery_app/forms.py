from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from .models import *

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField("Title", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField("Name", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    category = SelectField("Category", choices=ItemCategory.choices(), validators=[DataRequired()])
    photo_url = StringField("Photo URL", validators=[DataRequired()])
    store = QuerySelectField("Store", query_factory=lambda: GroceryStore.query, validators=[DataRequired()])
    submit = SubmitField("Submit")