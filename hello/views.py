from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

from logging import getLogger,StreamHandler,DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

logger.debug('HelloViews')

# Create your views here.
def index(request):

    logger.debug('index request')

    return HttpResponse('Hello from Python!')


def db(request):

    logger.debug('db request')

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

