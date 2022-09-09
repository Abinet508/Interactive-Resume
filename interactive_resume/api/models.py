from django.db import models
from django.contrib.auth.models import User


class Exprience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=500)
    date_started = models.DateField()
    date_ended = models.DateField()

    def __str__(self):
        return f'{self.user.username}-exprience'



class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=500)
    date_started = models.DateField()
    date_ended = models.DateField()

    def __str__(self):
        return f'{self.user.username}-education'



language_choice = (("English", "English"),
                    ("Amharic", "Amharic")
)

gender_choice = (("male", "male"),
                 ("Female", "Female"),
                 ("other", "other")
)
class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    full_name = models.CharField(max_length=100, blank=True)
    resident = models.CharField(max_length=200, blank=True)
    skills = models.CharField(max_length=200, blank=True)
    job_des = models.TextField(blank=True)
    language = models.CharField(choices=language_choice, max_length=200, blank=True)
    expirience = models.ForeignKey(Exprience, on_delete=models.DO_NOTHING, blank=True, null=True)
    education = models.ForeignKey(Education, on_delete=models.DO_NOTHING, blank=True, null=True)
    gender = models.CharField(choices=gender_choice, max_length=200, blank=True)

    def __str__(self):
        return f'{self.full_name}-Resume'


