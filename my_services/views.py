from django.shortcuts import render


def my_services(request):
    context = {}
    template = 'my_services/my_services.html'
    return render(request, template, context)

