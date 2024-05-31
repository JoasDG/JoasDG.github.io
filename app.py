from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

plaatsen = {

    'Madrid': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Barcelona': {'temperature': 'warm', 'mountain': 'ja', 'beach': 'ja', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Lissabon': {'temperature': 'warm', 'mountain': 'ja', 'beach': 'ja', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Friesland': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'ja', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'nee', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'frisse lucht'}, 

    'Maastricht': {'temperature': 'koud', 'mountain': 'ja', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'nee', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'frisse lucht'}, 

    'Oslo': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'frisse lucht'}, 

    'Reykjavík': {'temperature': 'koud', 'mountain': 'ja', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'frisse lucht'}, 

    'Berlijn': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Parijs': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Kroatië': {'temperature': 'warm', 'mountain': 'ja', 'beach': 'ja', 'activity': 'actief', 'nature': 'natuur', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'frisse lucht'}, 

    'Helsinki': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'nee', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Rome': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Milaan': {'temperature': 'warm', 'mountain': 'ja', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Athene': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'ja', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Londen': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Glasgow': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'nee', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Normandië': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'ja', 'activity': 'actief', 'nature': 'natuur', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'nee', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'frisse lucht'}, 

    'Venetië': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Wenen': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'Europa', 'religion': 'ja', 'vehicle': 'auto', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Pyongyang': {'temperature': 'koud', 'mountain': 'ja', 'beach': 'nee', 'activity': 'actief', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'vliegtuig', 'tourist_area': 'nee', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Beijing': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Dhaka': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'actief', 'nature': 'stad', 'modern': 'authentiek', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'vliegtuig', 'tourist_area': 'nee', 'same_culture': 'nee', 'remote_destination': 'ja', 'purpose': 'cultuur'}, 

    'New Delhi': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'actief', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'auto', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Tokio': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'ja', 'activity': 'actief', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Seoul': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'actief', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'auto', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Taipei': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Hongkong': {'temperature': 'warm', 'mountain': 'ja', 'beach': 'ja', 'activity': 'actief', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Bali': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'ja', 'activity': 'relaxed', 'nature': 'natuurlijk', 'modern': 'authentiek', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Ho Chi Minh stad': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'actief', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'nee', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'New York': {'temperature': 'koud', 'mountain': 'ja', 'beach': 'ja', 'activity': 'actief', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Los Angeles': {'temperature': 'warm', 'mountain': 'ja', 'beach': 'ja', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Las Vegas': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'actief', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Ohio': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'natuur', 'modern': 'authentiek', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Alabama': {'temperature': 'warm', 'mountain': 'ja', 'beach': 'ja', 'activity': 'relaxed', 'nature': 'natuur', 'modern': 'authentiek', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'California': {'temperature': 'warm', 'mountain': 'ja', 'beach': 'ja', 'activity': 'actief', 'nature': 'natuur', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'ja', 'purpose': 'cultuur'}, 

    'Utah': {'temperature': 'koud', 'mountain': 'ja', 'beach': 'nee', 'activity': 'actief', 'nature': 'natuur', 'modern': 'authentiek', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'ja', 'purpose': 'frisse lucht'}, 

    'Detroit': {'temperature': 'koud', 'mountain': 'nee', 'beach': 'ja', 'activity': 'relaxed', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Rio de Janeiro': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'ja', 'activity': 'actief', 'nature': 'beide', 'modern': 'authentiek', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Salvador': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'ja', 'activity': 'relaxed', 'nature': 'beide', 'modern': 'authentiek', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'cultuur'}, 

    'Manaus': {'temperature': 'warm', 'mountain': 'nee', 'beach': 'nee', 'activity': 'relaxed', 'nature': 'natuur', 'modern': 'authentiek', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'nee', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'frisse lucht'}, 

    'Denver': {'temperature': 'koud', 'mountain': 'ja', 'beach': 'nee', 'activity': 'actief', 'nature': 'stad', 'modern': 'modern', 'destination': 'wereldwijd', 'religion': 'ja', 'vehicle': 'vliegtuig', 'tourist_area': 'ja', 'same_culture': 'nee', 'remote_destination': 'nee', 'purpose': 'frisse lucht'} 
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
    return render_template('ql.html')

@app.route('/result')
def result():
    destination = request.args.get('destination')
    return render_template('result.html', destination=destination)

if __name__ == '__main__':
    app.run(debug=True)
