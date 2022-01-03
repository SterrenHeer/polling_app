from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponse


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


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.first_count += 1
        elif selected_option == 'option2':
            poll.second_count += 1
        elif selected_option == 'option3':
            poll.third_count += 1
        else:
            return HttpResponse(400, 'Invalid form option')
        poll.save()
    return redirect('results', poll.id)
