from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    birtday = models.DateField(null = True, blank = True)

    def __unicode__ (self):
        return self.user_id
    
    def get_absolute_url(self):
        return reverse('user_detail', args = [str(self.id)])

        
