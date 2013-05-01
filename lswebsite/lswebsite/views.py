from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.core.context_processors import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

def home_page(request):
    return render_to_response('index2.html',context_instance=RequestContext(request))
