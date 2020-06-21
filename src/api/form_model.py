from wtforms import Form, validators, StringField


class InputForm(Form):
    title = StringField(
        label='title', default=None,
        validators=[validators.InputRequired()])
    address = StringField(
        label='address', default=None)
    city = StringField(
        label='frequency (1/s)', default=None,
        validators=[validators.InputRequired()])
    state = StringField(
        label='time interval (s)', default='CO',
        validators=[validators.InputRequired()])
    postal_code = StringField(
        label='time interval (s)', default=None,
        validators=[validators.InputRequired()])
    # price = FloatField(
    #     label='time interval (s)', default=18,
    #     validators=[validators.InputRequired()])
    facts_and_features = StringField(
        label='time interval (s)', default=None,
        validators=[validators.InputRequired()])
    real_estate_provider = StringField(
        label='time interval (s)', default=None,
        validators=[validators.InputRequired()])
    url = StringField(
        label='time interval (s)', default=None)
