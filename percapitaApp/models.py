from email.policy import default
from time import timezone
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class itemPurchase(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()
    ino = models.IntegerField()
    dop = models.DateField()
    created = models.DateTimeField(auto_now_add=True,editable=False)
    def __str__(self):
        return self.item
