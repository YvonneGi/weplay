from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Category(models.Model):

    """ class to indicate the category of the Playground"""

    cat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name

    def save_category(self):

        '''Method to save a category in the database'''

        self.save()

    def update_category(self):
        ''' Method to update an category in the database'''
        self.update()

    def delete_category(self):

        ''' Method to delete a category from the database'''

        self.delete()

class Playground(models.Model):
    photo = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length=3000)
    location = models.CharField(max_length=255)
    post_date=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.description

    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def update_image(self):
        ''' Method to update an image in the database'''
        self.update()

    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()
    @classmethod
    def find_playground(cls,playground_id):
        playground = cls.objects.get(id=playground_id)
        return playground

class Team(models.Model):
    t_name = models.CharField(max_length = 400)
    description = models.CharField(max_length=300)
    members = models.IntegerField()
    ground = models.ForeignKey(Playground)
    def save_name(self):
        '''Method to save an names in the database'''
        self.save()

    def update_name(self):
        ''' Method to update an team name in the database'''
        self.update()

    def delete_name(self):
        ''' Method to delete an team name from the database'''
        self.delete()
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='photos/',null=True)
    fullname = models.CharField(max_length=255,null=True)
    username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    phone_number = models.IntegerField(null=True)
    team = models.ForeignKey(Team ,null=True)

    def __str__(self):
        return self.username.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
       if created:
           Profile.objects.create(username=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #    instance.profile.save()

    def update_profile(self):

        ''' Method to update a profile in the database'''

        self.update()

    def delete_profile(self):

        ''' Method to delete a profile from the database'''

        self.delete()


class Chat(models.Model):
    message = models.TextField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def save_chat(self):
        '''Method to save a chat in the database'''
        self.save()

    def delete_chat(self):

        ''' Method to delete a chat from the database'''
        self.delete()