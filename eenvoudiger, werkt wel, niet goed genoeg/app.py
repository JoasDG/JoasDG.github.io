from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Haal de ingevulde gegevens op uit het formulier
        temperature = request.form.get('temperature')
        mountain = request.form.get('mountain')
        beach = request.form.get('beach')

        # Logica om een bestemming te bepalen op basis van de antwoorden
        if temperature == 'warm' and beach == 'ja':
            destination = 'Hawaï'
        elif temperature == 'koud' and mountain == 'ja':
            destination = 'Zwitserland'
        else:
            destination = 'Nederland'

        # Render de result.html met de bestemming
        return render_template('result.html', destination=destination)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
