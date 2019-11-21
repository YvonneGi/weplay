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

class Fitness_activities(models.Model):
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
    @classmethod
    def search_by_category(cls,search_term):
        activities = cls.objects.filter(category__cat_name__contains=search_term)
        return activities
    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()
    @classmethod
    def find_activities(cls,activities_id):
        playground = cls.objects.get(id=activities_id)
        return playground

class Team(models.Model):
    t_name = models.CharField(max_length = 400)
    description = models.CharField(max_length=300)
    members = models.IntegerField(choices=list(zip(range(0, 40), range(0, 40))), default=0)
    ground = models.ForeignKey(Fitness_activities)
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
    chat = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def save_chat(self):
        '''Method to save a chat in the database'''
        self.save()

    def delete_chat(self):

        ''' Method to delete a chat from the database'''
        self.delete()
class Events (models.Model):
    title = models.CharField(max_length=30)
    post_description = models.CharField(max_length=300)
    posted_by = models.CharField(max_length=30)
    poster = models.ForeignKey(Fitness_activities)
    @classmethod
    def get_event(cls, post_hood):
        posts = Events.objects.filter(post_hood=id)
        return posts

    @classmethod
    def all_event(cls,id):
        posts = Events.objects.all()
        return posts
