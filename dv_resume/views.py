from django.shortcuts import render, redirect

from .forms import contactUs

from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.

def index(request):


    if request.method == "POST":

        form = contactUs(request.POST)


        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contactno']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

        recipient = ['dhavalveera@rocketmail.com']

        contact = str(contact)

        send_mail(
            subject + " - Dhaval Vira Portfolio/Resume",
            "Full Name = " + name + "\n\n" + "Email ID = " + email + "\n\n" + "Contact Number = " + contact + "\n\n" + "Message = " + message,
            email,
            recipient,
            fail_silently = False
        )

        messages.add_message(request, messages.SUCCESS,
                             'Thank You for Contacting Us, We will get back to you soon.')
        return redirect('index')

    
    else:

        form = contactUs()



    return render(request, 'index.html', { 'form' : form })
