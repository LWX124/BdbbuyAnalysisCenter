from django.db import models

# Create your models here.
from Tools.model_util import CModel

class Adminuser(CModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    boss = models.IntegerField(blank=True, null=True)
    driver = models.IntegerField(blank=True, null=True)
    store_manager = models.IntegerField()
    sale_manager = models.IntegerField(blank=True, null=True)
    sale_manager7 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminuser'

