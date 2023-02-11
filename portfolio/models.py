from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=220, unique=True)
    description = models.TextField(max_length=300, help_text='about your qualification')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=200,
                               blank=True,
                               null=True)
    message = models.TextField()

    class Meta:
        verbose_name = 'usercontact'
        verbose_name_plural = 'usercontacts'

    def __str__(self):
        return self.name