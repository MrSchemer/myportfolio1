from django.db import models
import bleach


  

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    slug = models.SlugField(max_length=122, unique=True)
    catagory = models.CharField(max_length=122, choices=(('edu', 'education'), ('project', 'projects'), ('experience', 'experience')), default='edu')
    image = models.ImageField(upload_to='static/images/portfolio',null=True)
    slogan = models.CharField(max_length=122)
    title = models.CharField(max_length=122)
    desc = models.TextField()
    url= models.URLField(max_length=200, null=True)
    date = models.DateField()

 


    def __str__(self):
        return self.title
    
class Blog(models.Model):
    slug = models.SlugField(max_length=122, unique=True)
    catagory = models.CharField(max_length=122, choices=(('web', 'Web Design'), ('app', 'App Design'), ('graphic', 'Graphic Design'), ('video', 'Video Editing'), ('photo', 'Photography'), ('Education', 'Education'),('other','others')), default='web')
    image = models.ImageField(upload_to='static/images/blog')
    slagan= models.CharField(max_length=122)
    title = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title
