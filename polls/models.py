import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200) #What is your name?
    pub_date = models.DateTimeField('date published')#date
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    # profile_pic=models.FileField()
    # first_name=models.CharField(max_length=200,blank=True)
    # last_name=models.CharField(max_length=200,blank=True)
    # birth_date=models.DateField(null=True,blank=True)
    mobile_number=models.IntegerField(default=0)
    address=models.TextField(max_length=500,blank=True)
    country=models.TextField(max_length=True,blank=True)

    def __str__(self):
        return f"{self.id}"
    def testy(self):
        print("hello")

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    # print("signal triggered")
    # print(instance)
    # print(kwargs)
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()


