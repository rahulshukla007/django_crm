from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def signUp(request):
    if request.method == "POST":
        #print(request.POST)
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
       fm = UserCreationForm()

    return render(request, 'account/registration.html', {'form':fm})