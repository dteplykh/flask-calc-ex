from wtforms import Form, StringField, FloatField, validators


class CalculatorForm(Form):
    operator = StringField("operator", [validators.any_of(
        ("+", "-", "*", "/")), validators.DataRequired()])
    operand_a = FloatField("operand_a", [validators.InputRequired()])
    operand_b = FloatField("operand_b", [validators.InputRequired()])
