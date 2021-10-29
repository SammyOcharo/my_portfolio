from django.db import models

# Create your models here.

class Tag(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Project(models.Model):
    Headline = models.CharField(max_length=150)
    Subheadline = models.CharField(blank=True, null=True, max_length=200)
    #thmbnail
    Body = models.TextField(null=True, blank=True)
    Created = models.DateTimeField(auto_now_add=True)
    Active = models.BooleanField(default=False)
    Featured = models.BooleanField(default=False)
    Tags = models.ManyToManyField(Tag)
    #slug = 

    def __str__(self):
        return self.Headline

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    Photo = models.ImageField(upload_to = 'media')
    Title = models.CharField(max_length=100)
    SubTitle = models.CharField(max_length=120)
    contact_email = models.EmailField()

    def __str__(self):
        return self.Title




