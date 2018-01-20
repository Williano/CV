from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_me(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            try:
                send_mail(subject, message, email, ['admin@example.com'], name)
            except BadHeaderError:
                return HttpResponse('Invalid header found. ')
            return redirect('contact_me:email_success')

    context = {'form': form}
    template = 'contact_me/contact_me.html'
    return render(request, template, context)


def email_success(request):
    context = {}
    template = 'contact_me/email_success.html'
    return render(request, template, context)

