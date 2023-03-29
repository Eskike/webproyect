from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from misitioweb.settings import EMAIL_HOST_USER
from .forms import FormularioContactos


def contact(request):
    if request.method == 'POST':
         #en este caso procesaremos el formulario
        form = FormularioContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            #enviaremos el email y redireccionamos
            email = EmailMessage(
                'Nuevo mensaje de MISITIOWEB', #asunto del mensaje
                'De {} <{}>\n\{}'.format(cd['name'], cd['email'], cd['content']), #Datos del mensaje
                EMAIL_HOST_USER, #Origen del email que nosotros enviamos
                ['kike.lizno@gmail.com'], #Destino principal de nuestro email(nosotros)
                reply_to=[cd['email']], #email de replica, para contestar
            )
            try:
                email.send()
                #si todo va bien...
                return redirect(reverse('contact')+'?ok')
            except:
                #si algo va mal...
                return redirect(reverse('contact')+'?fail')
    else:
        form = FormularioContactos()
    return render(request, 'contact/contact.html', {'form': form})