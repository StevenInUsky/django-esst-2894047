from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin')
def new_function(request):
    return render(request, 'home/test.html')
