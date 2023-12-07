from django.db import models

# Create your models here.

class Category(models.Model):
    # nombre de categoria tenemos 3   table  notebook y celulares
    Cname = models.CharField(max_length=128)
    # cantidad de articulos
    Cquantity = models.IntegerField()
    # si lo elimina normalmente es falso
    isDelete = models.BooleanField(null=False)

    def __str__(self):
        return self.Cname

class Product(models.Model):
    # nombre de producto
    pname = models.CharField(max_length=128)
    # fecha de creacion
    pdate = models.DateTimeField()
    # cantidad de stock
    pstock = models.IntegerField()
    # precio
    pprice = models.IntegerField()
    # de que categoria corresponde el producto
    pcategory = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    # si lo elimina normalmente es falso
    isDelete = models.BooleanField(null=False)

    def __str__(self):
        return self.pname

