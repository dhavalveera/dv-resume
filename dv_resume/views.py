from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from datetime import date

# Create your views here.

def index(request):

    today = date.today()
    age = today.year - 1996 - (( today.month, today. day ) < (7, 2))


    if request.method == "POST":
        fullname = request.POST['fullName']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        recipient = ['dhavalveera@rocketmail.com']

        send_mail(
        subject + " - Dhaval Vira Resume/Portfolio",
        "Full Name = " + fullname + "\n\n" + "Email ID = " + email + "\n\n" + "\n\n" + "Message = " + message,
        email,
        recipient,
        fail_silently = False )

        messages.add_message(request, messages.SUCCESS, f'Thank You for Contacting Us, We will get back to you soon.')
        return HttpResponseRedirect(reverse('index'))


    return render(request, 'index.html', { 'age' : age })



def page_not_found(request, exception):

    return render(request, '404-not-found.html', status=404)


def custom_error(request, exception=None):

    return render(request, '500-error.html', status=500)
