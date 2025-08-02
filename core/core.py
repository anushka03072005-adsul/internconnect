from django.shortcuts import render, redirect
from .forms import ApplicantForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ApplicantForm()
    return render(request, 'register.html', {'form': form})
