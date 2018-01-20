from django.shortcuts import render


def my_skills(request):
    context = {}
    template = 'my_skills/my_skills.html'
    return render(request, template, context)