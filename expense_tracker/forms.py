from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired

class ExpenseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    category = SelectField(
        'Category',
        choices=[('Food', 'Food'), ('Transport', 'Transport'), ('Entertainment', 'Entertainment')],
        validators=[DataRequired()]
    )
    amount = FloatField('Amount', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Add Expense')
