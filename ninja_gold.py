from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key='these_exercises_are_slowly_killing_me'
import random

@app.route('/')
def index():
    return render_template('ninja_gold.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_money():
    if 'gold' not in session:
        session['gold'] = 0
        session['building'] = ""
        session['activity'] = ""
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        goldEarned = random.randint(10,20)
    elif session['building'] == 'cave':
        goldEarned = random.randint(5,10)
    elif session['building'] == 'house':
        goldEarned = random.randint(2,5)
    else:
        goldEarned = random.randint(-50,50)
    print("GOLD EARNED", goldEarned)
    session['gold']+= goldEarned
    if goldEarned > 0:
        session['activity']+="Earned "+str(goldEarned)+" gold from the "+session['building']+"! \n"
    else:
        session['activity']+="Entered a "+session['building']+" and lost "+str(goldEarned)+" gold... Ouch... \n"
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)