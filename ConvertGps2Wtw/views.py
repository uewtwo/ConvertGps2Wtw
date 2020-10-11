from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ConvertGps2Wtw.settings import GOOGLE_API_KEY, WHAT3WORDS_KEY

def index(request):
    template = loader.get_template('ConvertGps2Wtw/index.html');
    context = {
        'GOOGLE_API_KEY': GOOGLE_API_KEY,
        'WHAT3WORDS_KEY': WHAT3WORDS_KEY,
    }

    return HttpResponse(template.render(context, request))
