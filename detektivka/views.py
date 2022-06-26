from django.http import HttpResponse
from django.template import loader

from detektivka import forms


def index_page(request):
    template = loader.get_template('detektivka/index.html')
    with open('detektivka/static/detektivka/historia.txt', 'w') as file:
        file.write('Toto je tvoja historia: \n\n')
    return HttpResponse(template.render({}, request))


def game_page(request):
    template = loader.get_template('detektivka/game.html')
    questions = [
        "Je streda 10.3.2021, sedíš v počítačovej učebni 568-B a učiteľ vám práve zadal zadanie. Zaujme ťa "
        "zabudnuté usb položené na stole vedľa, ktoré tam ležalo uz keď si prišiel. Komu asi patrí? ",
        "Pri toľkých možnostiach prichádza na rad len plán B. Zahodíš svoje morálne zásady s skúsiš pozrieť obsah "
        "usb v priečinku anonyms_USB či nenájdeš niečo čo by ťa priviedlo k majiteľovi... čo takto vylistovať obsah "
        "priečinka?",
        "Hmmm... Meno si síce nenašiel ale prečo sa jeden súbor volá DanajskyDar? Nevolá "
        "sa rovnako ako vírus ktorý bol rozposlaný týžden dozadu všetkým študentom? Nie každý má dostatočné vedomosti "
        "k vytvoreniu virusu, keďže ty si sa to učil až v druhom ročníku na Základoch reverného inžinierstva(ZRI). "
        "Kto spadá do množiny podozrivých? ",
        "Asi nemá zmysel riešiť, na ktorých počítačoch bol súbor spustený, keďže to mohol byť hociktorý z počítačov "
        "patriacich študentom, ktorým bol odoslaný mail s daným súborom v prílohe. No možno by však stálo zato "
        "vyhľadat, na ktorých počítačoch bol skompilovaný.",
        "Viac ako jedna odpoveď...zaujímave...možno sa nachadzajú v jednej učebni...",
        "Zjavne sa k počítačom mohol dostať len niekto kto predtým navštívil danú miestnosť.",
        "Vyzerá, že si sa postupne dostal k dvom skupinám ľudí. Moment - vidíš, že sa niektoré mená opakujú v oboch...",
        "Vytvoriť sieťového červa nie je vôbec jednoduché a určite by to človek nezvládol sám, bez najlepšieho "
        "priateľa programatóra - internetu. Dal by si ruku do ohňa zato, že v internetovej historii vinníka nájdeš "
        "slovo 'worm'...",
        "Možno zistíš niečo viac, keď vylistuješ celú históriu v chronologickom poradí.",
        "Už vieš kto bol vrah milovaného Linuxu?"
    ]

    context = {
        'counter': 0,
        'question': questions[0],
        'code_form': forms.CodeForm,
        'response': 'zatiaľ žiadna',
    }

    if request.method == 'POST':
        # poslat tani request.POST['code'] potom
        # context['response'] = odpoved_od_tani

        counter = int(request.POST['question_id'])
        if 'dotaz' in request.POST:
            context['response'] = request.POST['dotaz']
            file = open('detektivka/static/detektivka/historia.txt', 'a')
            file.write('na dotaz: ' + request.POST['dotaz'] + '\n')
            file.write('si dostal odpoved: ' + context['response'] + '\n\n')
        else:
            context['response'] = 'zatiaľ žiadna'
            counter += 1
            if counter == len(questions):
                counter = 0
        context['counter'] = counter
        context['question'] = questions[context['counter']]

    return HttpResponse(template.render(context, request))
