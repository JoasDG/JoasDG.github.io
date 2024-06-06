from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_data = request.form
        bestemming = bereken_bestemming(form_data)
        return render_template('result.html', bestemming=bestemming)
    return render_template('ql.html')

def bereken_bestemming(form_data):
    temperature = form_data.get('temperature')
    mountain = form_data.get('mountain')
    beach = form_data.get('beach')
    activity = form_data.get('activity')
    nature = form_data.get('nature')
    modern = form_data.get('modern')
    destination = form_data.get('destination')
    religion = form_data.get('religion')
    vehicle = form_data.get('vehicle')
    tourist_area = form_data.get('tourist_area')
    same_culture = form_data.get('same_culture')
    remote_destination = form_data.get('remote_destination')
    purpose = form_data.get('purpose')

    # Voorbeeld logica op basis van de formuliergegevens
    if temperature == 'warm':
        if beach == 'ja':
            if destination == 'Europa':
                return 'Spanje'
            else:
                return 'Bali'
        elif mountain == 'ja':
            if destination == 'Europa':
                return 'Zwitserse Alpen'
            else:
                return 'Rocky Mountains'
    elif temperature == 'koud':
        if mountain == 'ja':
            if destination == 'Europa':
                return 'Noorwegen'
            else:
                return 'Canada'
        elif beach == 'ja':
            if destination == 'Europa':
                return 'IJsland'
            else:
                return 'Patagonië'

    if activity == 'actief':
        if nature == 'natuur':
            if modern == 'modern':
                return 'Nieuw-Zeeland'
            else:
                return 'Peru'
        elif nature == 'stad':
            if modern == 'modern':
                return 'Tokyo'
            else:
                return 'Rome'
    elif activity == 'relaxed':
        if nature == 'natuur':
            if modern == 'modern':
                return 'Malediven'
            else:
                return 'Toscane'
        elif nature == 'stad':
            if modern == 'modern':
                return 'Dubai'
            else:
                return 'Parijs'

    if religion == 'ja':
        if destination == 'Europa':
            return 'Vaticaanstad'
        else:
            return 'India'

    if vehicle == 'auto':
        if same_culture == 'ja':
            return 'België'
        else:
            return 'Oostenrijk'
    elif vehicle == 'vliegtuig':
        if remote_destination == 'ja':
            return 'Paaseiland'
        else:
            return 'New York'

    if tourist_area == 'ja':
        return 'Orlando'
    elif tourist_area == 'nee':
        if remote_destination == 'ja':
            return 'Bhutan'
        else:
            return 'Madagaskar'

    if purpose == 'cultuur':
        return 'Egypte'
    elif purpose == 'frisse lucht':
        return 'Alaska'

    return 'Onbekende bestemming'

if __name__ == '__main__':
    app.run(debug=True)
