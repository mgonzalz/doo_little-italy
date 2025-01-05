from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from pizzeria.settings import EMAIL_HOST_USER
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        # Si el campo no está presente, se envía una cadena vacía.

        # Enviar correo
        email = EmailMessage(
            "Little Pizzeria: Nuevo mensaje de contacto",
            "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
            EMAIL_HOST_USER,
            ["6962a3ea86-d2674a+1@inbox.mailtrap.io"],
            reply_to=[email],
        )
        try:
            # Todo ha ido bien, redireccionamos a OK.
            email.send()
            return redirect(reverse('contact') + "?ok")
        except:
            # Algo no ha ido bien, redireccionamos a FAIL.
            return redirect(reverse('contact') + "?fail")
    return render(request, "contact/contact.html", {'form': contact_form})

def home_service(request):
    return render(request, 'contact/home-service.html')
