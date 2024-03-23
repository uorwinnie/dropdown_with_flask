from flask import Flask, render_template, request, send_file
import random
import time
app = Flask(__name__)



Pizza = ["Regular","Sicilian"]
Flowers =["Lily", "Daisy","Cosmos","Tulip", "Babay Breath"]
City = ["Denver","NY","Seoul"]
l =[Pizza, Flowers, City]
@app.route('/')
@app.route('/index')
def index():
    picks = random.choice(l)
    print(picks)
    return render_template('index.html', picks=picks)

@app.route('/testingcsv', methods=[ "POST"],)
def csv_name():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Run':
            time.sleep(10)
            print("ran")
            num = 200
            return "ran"
        if request.form['submit_button'] == 'Download' and num == 200:
            select = request.form.get('things').lower()
            return send_file(f"{select}.csv", as_attachment=True)
        


if __name__ == '__main__':
    app.run(debug=True)