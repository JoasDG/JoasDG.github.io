from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

plaatsen = {
    'Madrid': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'Christendom', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 
    'Barcelona': {'temperature': 'warm', 'mountain': 'ja', 'beach': 'ja', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'Christendom', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'cultuur'},
    # Voeg alle andere bestemmingen hier toe
}

def find_best_destination(user_answers, destinations):
    best_destination = None
    best_score = -1

    for destination, properties in destinations.items():
        score = 0
        for key, value in user_answers.items():
            if key in properties and properties[key] == value:
                score += 1
        if score > best_score:
            best_score = score
            best_destination = destination

    return best_destination

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_answers = {
            'temperature': request.form['temperature'],
            'mountain': request.form['mountain'],
            'beach': request.form['beach'],
            'activity': request.form['activity'],
            'nature': request.form['nature'],
            'modern': request.form['modern'],
            'destination': request.form['destination'],
            'religion': request.form['religion'],
            'vehicle': request.form['vehicle'],
            'tourist_area': request.form['tourist_area'],
            'same_culture': request.form['same_culture'],
            'remote_destination': request.form['remote_destination'],
            'purpose': request.form['purpose']
        }
        best_destination = find_best_destination(user_answers, plaatsen)
        return redirect(url_for('result', destination=best_destination))
    return render_template('index.html')

@app.route('/result')
def result():
    destination = request.args.get('destination')
    return render_template('result.html', destination=destination)

if __name__ == '__main__':
    app.run(debug=True)
