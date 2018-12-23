from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    class Meta:
        db_table = u'Contact'

class Blogtype(models.Model):
    name = models.CharField(max_length=264, unique = True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = u'Blogtype'

class Blog(models.Model):
    title = models.CharField(max_length=264, unique = True)
    intro = models.CharField(max_length=1000)
    body = RichTextField(max_length=20000)
    image = models.ImageField(upload_to = "images/", blank=True)
    blog_type = models.ForeignKey(Blogtype, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    class Meta:
        db_table = u'Blog'
    
