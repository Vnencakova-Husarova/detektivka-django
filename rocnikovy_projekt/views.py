from django.http import HttpResponse
from django.template import loader

from . import forms


def index_page(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def game_page(request):
    template = loader.get_template('game.html')
    questions = [
        "1. Je streda 10.3.2021, sedíš v počítačovej učebni 568-B a ucitel vam prave zadal zadanie. Zaujme ta "
        "zabudnute usb polozene na stole vedla, ktore tam lezalo uz ked si prisiel. Komu asi patri? ",
        "2. Pri toľkých možnostiach prichádza na rad len plán B. Zahodíš svoje morálne zásady s skúsiš pozrieť obsah "
        "usb v priečinku anonyms_USB či nenájdeš niečo čo by ťa priviedlo k majiteľovi... čo takto vylistovať obsah "
        "priečinka? ",
        "3. Hmmm... Meno si síce nenašiel ale prečo sa jeden súbor volá ---- (TODO doplnit nieco kreativne)? Nevolá "
        "sa rovnako ako vírus ktorý bol rozposlaný týžden dozadu všetkým študentom? Nie každý má dostatočné vedomosti "
        "k vytvoreniu virusu, keďže ty si sa to učil až v druhom ročníku na Základoch reverného inžinierstva(ZRI). "
        "Kto spadá do množiny podozrivých? ",
    ]

    context = {
        'counter': 0,
        'question': questions[0],
        'code_form': forms.CodeForm,
        'response': 'zatial ziadna',
    }

    if request.method == 'POST':
        # poslat tani request.POST['code'] potom
        # context['response'] = odpoved_od_tani

        if 'dotaz' in request.POST:
            context['response'] = request.POST['dotaz']
        else:
            context['response'] = 'zatial ziadna'
            counter = int(request.POST['question_id']) + 1
            if counter == len(questions):
                counter = 0
            context['counter'] = counter
            context['question'] = questions[counter]

        # context['question'] = questions[context['counter']]

    return HttpResponse(template.render(context, request))
