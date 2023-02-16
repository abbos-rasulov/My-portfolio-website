from django.db import models


class JobSkill(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=220, unique=True)
    available = models.BooleanField(default=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=220, unique=True)
    description = models.TextField(max_length=300, help_text='about your qualification')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class UserContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=200,
                               blank=True,
                               null=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'usercontact'
        verbose_name_plural = 'usercontacts'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True)
    image = models.ImageField(upload_to='team/%Y/%m/%d')
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.name.title()} {self.job.lower()}"


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='work/%Y/%m/%d')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
