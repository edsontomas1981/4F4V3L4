from cgitb import html
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

class Email():
    def __init__(self,usuario,destinatario,assunto,html_message) -> None:
        self.destinatario=destinatario
        self.assunto=assunto
        self.html_message=html_message
        self.usuario=usuario
        
        
    def enviarEmail(self):
        send_mail(
        self.assunto,
        self.mensagem,
        self.destinatario,
        [self.destinatario],
        fail_silently=False,
        )
    
    def envia_email_html(self):
        message=strip_tags(self.html_message)
        send_mail(subject=self.assunto, 
                message=message,
                html_message=self.html_message,
                from_email=settings.EMAIL_HOST_USER, 
                recipient_list=[self.usuario.email], 
                fail_silently=False,
                )    