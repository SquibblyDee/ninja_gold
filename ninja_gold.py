from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key='these_exercises_are_slowly_killing_me'
import random
import time
import datetime

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['building'] = ""
        session['activity'] = ""
        session['goldEarned'] = 0
    return render_template('ninja_gold.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_money():
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        session['goldEarned'] = random.randint(10,20)
    elif session['building'] == 'cave':
        session['goldEarned'] = random.randint(5,10)
    elif session['building'] == 'house':
        session['goldEarned'] = random.randint(2,5)
    else:
        session['goldEarned'] = random.randint(-50,50)
    print("GOLD EARNED", session['goldEarned'])
    session['gold']+= session['goldEarned']
    if session['goldEarned'] > 0:
        session['activity']+="Earned "+str(session['goldEarned'])+" gold from the "+session['building']+"!  ("+str(datetime.datetime.now().strftime("%y/%m/%d %H:%M"))+")\n"
    else:
        session['activity']+="Entered a "+session['building']+" and lost "+str(session['goldEarned'])+" gold... Ouch...  ("+str(datetime.datetime.now().strftime("%y/%m/%d %H:%M"))+")\n"
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)