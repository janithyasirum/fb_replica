from django.db import models
from django.contrib.auth.models import User
from FB_Replica.shared_utils import UploadToPathAndRename


class Profile(models.Model):
    Male = 'Male'
    Female = 'Female'
    Others = 'Others'

    GENDER_CHOICES = (
        (Male, 'M'),
        (Female, 'F'),
        (Others, 'O'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=UploadToPathAndRename('media/Images/User/'),
                              default='media/Images/User/default_user.png')
    street = models.TextField(max_length=254, blank=True)
    city = models.TextField(max_length=254, blank=True)
    state = models.TextField(max_length=254, blank=True)
    country = models.TextField(max_length=254, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=37, choices=GENDER_CHOICES, null=True, blank=True, default=Male)

