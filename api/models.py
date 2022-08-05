from django.db import models


# Create your models here.
class Profile(models.Model):
    STATE_CHOICES = (
        ('Punjab', 'Punjab'),
        ('Sindh', 'Sindh'),
        ('KPK', 'KPK'),
        ('Balochistan', 'Balochistan'),
        ('Fata', 'Fata'),)

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )


    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    pimage = models.ImageField(upload_to='pimage',  blank=True)
    rdocs = models.FileField(upload_to='rdocs', blank=True)


    def __str__(self):
        return self.name




