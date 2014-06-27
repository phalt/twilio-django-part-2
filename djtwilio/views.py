# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

@twilio_view
def gather_digits(request):

    r = Response()
    with r.gather(action='/respond/', numDigits=1) as g:
        g.say('Press one to hear a song, two to receive an SMS')

    return r

