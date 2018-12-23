from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categories(models.Model):
    ten_dm = models.CharField(max_length = 40, unique = True)

    def __str__(self):
        return str(self.ten_dm)

class Product(models.Model):
    ten_sp = models.CharField(max_length = 200, unique = True)
    don_gia = models.IntegerField()
    description = RichTextField(max_length = 5000)
    hinh = models.ImageField(upload_to = 'images/')
    danh_muc = models.ForeignKey(Categories, on_delete = models.PROTECT)
    
    def __str__(self):
        return str(self.ten_sp)
