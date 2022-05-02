from django.http import HttpResponse
from django.template import loader

from . import forms


def index_page(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def game_page(request):
    template = loader.get_template('game.html')
    context = {
        'code_form': forms.CodeForm,
        'odpoved': 'zatial ziadna',
    }
    if request.method == 'POST':
        context['odpoved'] = request.POST['code']

    return HttpResponse(template.render(context, request))
