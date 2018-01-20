from django.shortcuts import render


def experience(request):
    context = {}
    template = 'experience/experience.html'
    return render(request, template, context)
