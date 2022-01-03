from django.shortcuts import render, redirect
from .forms import CreatePollForm


def home(request):
    context = {}
    return render(request, 'poll/home.html', context)


def create(request):
    context = {}
    return render(request, 'poll/create.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    return render(request, 'poll/create.html', {'form': form})
