from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_data = request.form
        bestemming = bereken_bestemming(form_data)
        return render_template('../result.html', bestemming=bestemming)
    return render_template('../ql.html')

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

    # Logica voor temperatuur en strand/bergen
    if temperature == 'warm':
        if beach == 'ja':
            if destination == 'Europa':
                return 'Spanje'
            elif destination == 'Azië':
                return 'Bali'
            elif destination == 'Amerika':
                return 'Florida'
            else:
                return 'Maldiven'
        elif mountain == 'ja':
            if destination == 'Europa':
                return 'Zwitserse Alpen'
            elif destination == 'Azië':
                return 'Himalaya'
            elif destination == 'Amerika':
                return 'Rocky Mountains'
            else:
                return 'Andes'
    elif temperature == 'koud':
        if mountain == 'ja':
            if destination == 'Europa':
                return 'Noorwegen'
            elif destination == 'Azië':
                return 'Japan'
            elif destination == 'Amerika':
                return 'Canada'
            else:
                return 'Nieuw-Zeeland'
        elif beach == 'ja':
            if destination == 'Europa':
                return 'IJsland'
            elif destination == 'Azië':
                return 'Hokkaido, Japan'
            elif destination == 'Amerika':
                return 'Alaska'
            else:
                return 'Antarctica'

    # Logica voor activiteit en natuur/stad
    if activity == 'actief':
        if nature == 'natuur':
            if modern == 'modern':
                return 'Nieuw-Zeeland'
            else:
                return 'Patagonië'
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

    # Logica voor religie
    if religion == 'ja':
        if destination == 'Europa':
            return 'Vaticaanstad'
        elif destination == 'Azië':
            return 'India'
        elif destination == 'Amerika':
            return 'Mexico'
        else:
            return 'Jeruzalem'

    # Logica voor vervoersmiddel en cultuur
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

    # Logica voor toeristische gebieden
    if tourist_area == 'ja':
        return 'Orlando'
    elif tourist_area == 'nee':
        if remote_destination == 'ja':
            return 'Bhutan'
        else:
            return 'Madagaskar'

    # Logica voor doel van de reis
    if purpose == 'cultuur':
        return 'Egypte'
    elif purpose == 'frisse lucht':
        return 'Alaska'

    return 'Onbekende bestemming'

if __name__ == '__main__':
    app.run(debug=True)
