from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll


def home(request):
    polls = Poll.objects.all()
    return render(request, 'poll/home.html', {'polls': polls})


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    return render(request, 'poll/create.html', {'form': form})
