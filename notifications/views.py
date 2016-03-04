from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.db.models import F
from django.views import generic

from django.utils import timezone

from .models import Notification

# Create your views here.
class IndexView(generic.DetailView):
	template_name = 'notifications/index.html'
	model = Notification