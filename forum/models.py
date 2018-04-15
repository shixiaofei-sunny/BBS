from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200)
    post = models.textField()
    created = models.DateTimeFeild(auto_now=True)

    def __str__(self):
        return self.title
    
