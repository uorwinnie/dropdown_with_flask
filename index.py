from flask import Flask, render_template, request, redirect,send_file
import time
import random
import csv
app = Flask(__name__)

Flowers =["Lily", "Regular","Sicilian","Denver" ]
selected_item=[]
#picks = random.choice(l)
num = 100
@app.route('/')
@app.route('/index')
def index():
    print(Flowers)
    return render_template('index.html',num=num, picks=Flowers,chose=None)  
@app.route('/testingcsv', methods=[ "POST"],)
def csv_run():
    if request.method == 'POST':
        key = 1500
        run =request.form.get('submit_run')
        download=request.form.get('submit_download')
        select = request.form.get('things').lower()
        print(select)
        while key== 1500:
            if run:
                time.sleep(10)
                num =200
                chose=select.title()
                print(chose)
                Flowers.remove(chose)
                return render_template('index.html',num=num,picks=Flowers,chose=chose)
            elif download:
                return send_file(f"{select}.csv", as_attachment=True)
            key =1000
        else:
            return redirect('/index')
            

            

if __name__ == "__main__":
    app.run()
