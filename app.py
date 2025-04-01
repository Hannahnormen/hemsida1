from flask import Flask, render_template, request
from lager import Lager  # Importera Lager-klassen

app = Flask(__name__)

lager = Lager()  # Skapa en instans av lagret

@app.route('/')
def home():
    mediciner = lager.hämta_alla_produkter()  # Hämta listan med produkter
    return render_template('index.html', mediciner=mediciner)

@app.route('/bestall', methods=['GET', 'POST'])
def bestall():
    if request.method == 'POST':
        namn = request.form['namn']
        antal = int(request.form['antal'])
        lager.köp(namn, antal)  # Minskar lagersaldot
        return render_template('bestall.html', mediciner=lager.hämta_alla_produkter(), message="Din beställning har genomförts!")
    
    mediciner = lager.hämta_alla_produkter()
    return render_template('bestall.html', mediciner=mediciner)

if __name__ == '__main__':
    app.run(debug=True)
