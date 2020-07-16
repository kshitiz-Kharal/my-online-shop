from django.db import models

# Create your models here.


class BlogPost(models.Model):
    post_id = models.AutoField
    title = models.CharField(max_length=700, default="")
    head0 = models.CharField(max_length=600, default="")
    chead0 = models.CharField(max_length=6000, default="")
    head1 = models.CharField(max_length=600, default="")
    chead1 = models.CharField(max_length=6000, default="")
    head2 = models.CharField(max_length=600, default="")
    chead2 = models.CharField(max_length=6000, default="")
    thumbnail = models.ImageField(upload_to='shop/images', default="")
    Published_date = models.DateField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, default="")
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
