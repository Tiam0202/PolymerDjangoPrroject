from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response


# @login_required(login_url='/login/')
from django.template import RequestContext
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
#
# def index(request):
#     return render_to_response('index.html', {}, RequestContext(request))
