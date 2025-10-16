from flask import Flask, render_template, request
import os

# Tell Flask to look for templates and static files in the current folder
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    color = None

    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            height_m = height / 100  # convert cm to meters

            bmi = round(weight / (height_m ** 2), 2)

            if bmi < 18.5:
                category, color = "Underweight", "lightblue"
            elif 18.5 <= bmi < 24.9:
                category, color = "Normal", "lightgreen"
            elif 25 <= bmi < 29.9:
                category, color = "Overweight", "orange"
            else:
                category, color = "Obese", "red"

        except (ValueError, ZeroDivisionError):
            bmi = None
            category = "Invalid input. Please enter valid numbers."
            color = "gray"

    return render_template('index.html', bmi=bmi, category=category, color=color)

if __name__ == '__main__':
    app.run(debug=True)
