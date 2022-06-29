from django.core.mail import send_mail

class Email():
    def __init__(self,destinatario,assunto,mensagem) -> None:
        self.destinatario=destinatario
        self.assunto=assunto
        self.mensagem=mensagem
        
    def enviarEmail(self):
        send_mail(
        self.assunto,
        self.mensagem,
        self.destinatario,
        [self.destinatario],
        fail_silently=False,
        )