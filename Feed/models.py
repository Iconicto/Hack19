from django.db import models


# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='Source/logo/')

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=350)
    time = models.DateTimeField(auto_now=True)
    link = models.URLField()
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING, related_name='NewsSource')
    image = models.ImageField(upload_to='News/', blank=True, null=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=150)
    venue = models.CharField(max_length=350)
    organizer = models.CharField(max_length=350)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    registration_link = models.URLField()
    banner = models.ImageField(upload_to='Event/Banner')

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=200)
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


class Widget(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Widget/', blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.name



