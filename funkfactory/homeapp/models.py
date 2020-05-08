from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db.models.functions import datetime
from django.contrib.auth.models import auth


class HomePictures(models.Model):
    title = models.CharField(max_length=10, null=False)
    body = models.CharField(max_length=30, null=True)
    images = models.ImageField(upload_to='carousel', null=True)
    date = models.DateTimeField(auto_now_add=datetime.datetime.now())

    class Meta:
        verbose_name = "Website Carousel Image"
        verbose_name_plural = "Website Top Images"

    def __str__(self):
        return self.title


class Cards(models.Model):
    card_title = models.CharField(max_length=20, null=False)
    card_text = models.CharField(max_length=100, null=False)
    images = models.ImageField(upload_to='cards', null=True)
    card_body = models.CharField(max_length=5000, null=False)

    def __str__(self):
        return self.card_title

    class Meta:
        verbose_name = "Website Card Image"


class ContactForm(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone = models.CharField(max_length=10, null=False)
    message = models.TextField(max_length=1000, null=False)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    heading = models.CharField(max_length=100, null=False)
    sub_heading = models.CharField(max_length=100, null=False)
    body = models.CharField(max_length=1000, null=False)
    more_body = models.CharField(max_length=1000, null=False)
    image = models.ImageField(upload_to='about_us', null=False)
    more_popup_image = models.ImageField(upload_to='about_us', null=False)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class ClassAbout(models.Model):
    heading = models.CharField(max_length=30, null=False)
    body = models.CharField(max_length=1000, null=False)
    heading2 = models.CharField(max_length=30, null=False)
    body2 = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.heading


class Notice(models.Model):
    notice = models.CharField(max_length=300, null=False)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.notice


class DanceStyleWeTeach(models.Model):
    class_name = models.CharField(max_length=20, null=False)
    dance_style = models.CharField(max_length=20, null=False)
    picture = models.ImageField(upload_to='dance_styles', null=False)

    def __str__(self):
        return self.class_name


class FacultiesProfile(models.Model):
    image = models.ImageField(upload_to='dance_masters', blank=True)
    name = models.CharField(max_length=20, null=False)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class FunkFactoryGallery(models.Model):
    likes = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=2000, null=False)
    location = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='gallery', blank=True)
    background_image = models.ImageField(upload_to='gallery', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.location


class Reviews(models.Model):
    name = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='gallery', blank=True)
    review = models.CharField(max_length=400, null=False)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class OurDetail(models.Model):
    email = models.EmailField()
    add_line_1 = models.CharField(max_length=30, blank=True)
    add_line_2 = models.CharField(max_length=30, blank=True)
    add_line_3 = models.CharField(max_length=30, blank=True)
    phone_line_1 = models.CharField(max_length=20, blank=True)
    phone_line_2 = models.CharField(max_length=20, blank=True)
    phone_line_3 = models.CharField(max_length=20, blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)

    def __str__(self):
        return self.email


class Passwords(models.Model):
    # userid = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, null=False)
    username = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.username
