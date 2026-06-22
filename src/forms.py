from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional
class EntryForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    entry_type = SelectField('Income or Expense?', choices=[('income', 'Income'), ('expense', 'Expense')], validators=[DataRequired()])
    category = SelectField('Category', choices=[('rent', 'Rent'), ('utilities', 'Utilities'), ('gas', 'Gas'), ('school_costs', 'Tuition/Fees'), ('car_insurance', 'Car Insurance'), ('renters_insurance', 'Renter\'s Insurance'), ('phone_bill', 'Phone Bill'), ('groceries', 'Groceries'), ('outside_food', 'Eating Out'), ('entertainment', 'Entertainment')],validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    description = StringField('Description', validators=[Optional()])
    is_recurring = BooleanField('Recurring')
    recurrence_frequency = SelectField('How often?', choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('annually', 'Annually')], validators=[Optional()])
    ends_on = DateField('Ends On:', validators=[Optional()])
    submitted_by = SelectField('Submitted by:', choices=[('brandon', 'Brandon'), ('riley', 'Riley')], validators=[DataRequired()])
    submit = SubmitField('Submit')