from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
            return self.location_name
    def save_location(self):
        self.save()
      
class Sector (models.Model):
    sector_name = models.CharField(max_length=30, unique=True)
    def __str__(self):
            return self.sector_name

    def save_sector_name(self):
        self.save()

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
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
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
    def search_by_sector(cls,search_term):
        sectors = cls.objects.filter(sector__sector_name__icontains=search_term)
        # activities = cls.objects.filter(loca__location_name__contains=search_term)
        return sectors    
    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()
    @classmethod
    def find_activities(cls,activities_id):
        playground = cls.objects.get(id=activities_id)
        return playground
    @classmethod
    def filter_sector(cls,sector):
        filter_sect = cls.objects.filter(sector__sector_name__icontains=sector)
        return filter_sect

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
    phone_number = models.CharField(max_length = 10,blank =True)
    
    team = models.ForeignKey(Team ,null=True)

    def __str__(self):
        return self.username.username

    def save_profile(self):
        self.save()    
        
    def update_profile(self):
        self.update()

    def delete_profile(self):
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
    def all_event(cls,event_id):
        posts = cls.objects.get(id=event_id)
        return posts

        self.delete()

class Blog (models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=30)
    blog_description = models.TextField(max_length=300)
    posted_by = models.CharField(max_length=30)
    poster = models.ForeignKey(Fitness_activities)
    bloger = models.ForeignKey(User,on_delete=models.CASCADE , null=True)
    profile = models.ForeignKey(Profile,null = True) 

    @classmethod
    def get_blog(cls, post_blog):
        blogs = Blog.objects.filter(post_blog=id)
        return blogs

    @classmethod
    def all_blogs(cls,id):
        blogs = Blog.objects.all()
        return blogs

        self.delete()

class Comment(models.Model):
    comment_content = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    poster = models.ForeignKey(Fitness_activities,on_delete=models.CASCADE)

    def save_comment(self):
        '''Method to save a comment in the database'''
        self.save()

    def delete_comment(self):

        ''' Method to delete a comment from the database'''
        self.delete()
