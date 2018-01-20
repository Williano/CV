from django.shortcuts import render


def about_me(request):
    context = {}
    template = 'about_me/about_me.html'
    return render(request, template, context)