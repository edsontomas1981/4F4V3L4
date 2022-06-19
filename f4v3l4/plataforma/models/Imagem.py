from django.db import models
from .Pedidos import Pedidos
from PIL import Image

class Imagem(models.Model):
    imagem=models.ImageField(upload_to='media', blank=False)
    pedido_fk=models.ForeignKey(Pedidos,null=False,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.imagem.path)
        largura_desejada = 150
        largura_imagem = img.size[0]
        altura_imagem = img.size[1]
        percentual_largura = float(largura_desejada) / float(largura_imagem)
        altura_desejada = int((altura_imagem * percentual_largura))
        output_size = (200, 200)
        img.thumbnail(output_size)
        img.save(self.imagem.path)
