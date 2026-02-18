from django.shortcuts import render
from django.http import HttpResponse
from .models import Contracts


def index(request):
    # This is the base structure of each view of thr website, escluding the detail pages 
    # Are shown all the modules
    
	contracts = Contracts.objects.all()

	context = {'contracts' : contracts }
    
	return render(request, 'alby_intelligence/base.html', context)
