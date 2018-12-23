from django.db import models

# Create your models here.
class Customer(models.Model):
    ho_ten = models.CharField(max_length = 60, blank = False)
    user_name = models.CharField(max_length = 100, blank = False)
    mat_khau = models.CharField(max_length = 100, blank = False)
    phone = models.CharField(max_length = 15, blank = False)
    email = models.CharField(max_length = 100, blank = False)
    dia_chi = models.CharField(max_length = 200, blank = False)
    def __str__(self):
        return self.ho_ten
    class Meta:
        db_table = u'Customer'