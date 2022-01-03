from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'poll/home.html', context)
