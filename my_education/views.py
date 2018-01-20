from django.shortcuts import render


def my_education(request):
    context = {}
    template = 'my_education/my_education.html'
    return render(request, template, context)
