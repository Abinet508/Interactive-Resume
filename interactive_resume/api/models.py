from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    gender_choice = (("male", "male"),
                     ("Female", "Female"),
                    ("other", "other"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume')
    profile_pic = models.ImageField(blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    resident = models.CharField(max_length=200, blank=True)
    skills = models.CharField(max_length=200, blank=True)
    job_des = models.TextField(blank=True)
    language = models.CharField(max_length=200, blank=True)
    # expirience = models.ForeignKey(Exprience, on_delete=models.DO_NOTHING, blank=True, null=True)
    # education = models.ForeignKey(Education, on_delete=models.DO_NOTHING, blank=True, null=True)
    gender = models.CharField(choices=gender_choice, max_length=200, blank=True)

    def __str__(self):
        return f'{self.full_name}-Resume'


class Exprience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=500)
    date_started = models.DateField()
    date_ended = models.DateField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}-exprience'



class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=500)
    date_started = models.DateField()
    date_ended = models.DateField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}-education'





