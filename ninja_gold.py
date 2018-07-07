from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key='these_exercises_are_slowly_killing_me'
import random
import time

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['building'] = ""
        session['activity'] = []
        session['i'] = 0
    return render_template('ninja_gold.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_money():
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        goldEarned = random.randint(10,20)
    elif session['building'] == 'cave':
        goldEarned = random.randint(5,10)
    elif session['building'] == 'house':
        goldEarned = random.randint(2,5)
    else:
        goldEarned = random.randint(-50,50)
    # print("GOLD EARNED", goldEarned)
    session['gold']+= goldEarned
    if goldEarned > 0:
        session['activity'].append("Earned "+str(goldEarned)+" gold from the "+session['building']+"!\n")
        print("INDEX ",session['i'])
        session['i']+=1
        print("INDEX2 ",session['i'])
        for i in range(len(session['activity'])):
            print(session['activity'][i])
    else:
        session['activity'].append("Entered a "+session['building']+" and lost "+str(goldEarned)+" gold... Ouch...\n")
        for i in range(len(session['activity'])):
            print(session['activity'][i])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)