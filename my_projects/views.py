from django.shortcuts import render


def my_projects(request):
    context = {}
    template = 'my_projects/my_projects.html'
    return render(request, template, context)