from django.db import models


# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='Source/logo/')

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    time = models.DateField(auto_now=True)
    link = models.URLField()
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING, related_name='PostSource')
    image = models.ImageField(upload_to='Post/', blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=150)
    venue = models.CharField(max_length=350)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    registration_link = models.URLField()

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    title = models.CharField(max_length=150)
    author = models.DateField()
    published_date = models.DateField()
    link = models.URLField()
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING, related_name='TutorialSource')

    def __str__(self):
        return self.title


class Community(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    irc_link = models.URLField(blank=True, null=True)
    community_link = models.URLField()

    def __str__(self):
        return self.name




