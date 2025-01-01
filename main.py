from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', validators=[DataRequired()],
                         choices=[('✘'), ('☕'), ('☕☕'), ('☕☕☕'), ('☕☕☕☕'), ('☕☕☕☕☕')])
    wifi = SelectField('Wifi Rating', validators=[DataRequired()],
                       choices=[('✘'), ('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')])
    power = SelectField('Power Outlet Rating', validators=[DataRequired()],
                        choices=[('✘'), ('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')

def get_cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        return list_of_rows

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        input_cafe = form.cafe.data
        input_location = form.location.data
        input_open_time = form.open_time.data
        input_closing_time = form.closing_time.data
        input_coffee = form.coffee.data
        input_wifi = form.wifi.data
        input_power = form.power.data
        csv_data = [input_cafe, input_location, input_open_time, input_closing_time, input_coffee, input_wifi,
                    input_power]
        with open('cafe-data.csv', 'a', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(csv_data)
        list_of_rows = get_cafes()
        return render_template('cafes.html', cafes=list_of_rows)
    else:
        return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    list_of_rows = get_cafes()
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/aws')
def hifromcloud():
    return render_template('hi-from-aws.html')


if __name__ == '__main__':
    app.run()

