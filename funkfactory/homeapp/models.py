from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db.models.functions import datetime
from django.contrib.auth.models import auth


class HomePictures(models.Model):
    title = models.CharField(max_length=10, blank=True)
    body = models.CharField(max_length=30, blank=True)
    images = models.ImageField(upload_to='carousel', blank=True)
    date = models.DateTimeField(auto_now_add=datetime.datetime.now())

    class Meta:
        verbose_name_plural = "1 Website Carousel Image"
        verbose_name = "Website Top Image"
        ordering = ('-date',)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    heading = models.CharField(max_length=100, blank=True)
    sub_heading = models.CharField(max_length=100, blank=True)
    body = models.CharField(max_length=1000, blank=True)
    more_body = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='about_us', blank=True)
    more_popup_image = models.ImageField(upload_to='about_us', blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "2 About Us"
        verbose_name = "About Us"


class Notice(models.Model):
    notice = models.CharField(max_length=300, null=False)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.notice

    class Meta:
        verbose_name_plural = "3 Notice"
        verbose_name = "Notice"
        ordering = ('-date',)



class ClassAbout(models.Model):
    heading = models.CharField(max_length=30, blank=True)
    body = models.CharField(max_length=1000, blank=True)
    heading2 = models.CharField(max_length=30, blank=True)
    body2 = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "4 personalise about class"
        verbose_name = "personalise about class"


class DanceStyleWeTeach(models.Model):
    class_name = models.CharField(max_length=20, blank=True)
    dance_style = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='dance_styles', blank=True)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = "5 Dance class photo details"
        verbose_name = "Heading And Body"


class Packages(models.Model):
    class_name = models.CharField(max_length=10, blank=True)
    timing = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=10, blank=True)
    rating = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = "6 Class Packages"
        verbose_name = "Details"


class FacultiesProfile(models.Model):
    image = models.ImageField(upload_to='dance_masters', blank=True)
    name = models.CharField(max_length=20, blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "7 Instructor details"
        verbose_name = "Details"


class FunkFactoryGallery(models.Model):
    likes = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    location = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='gallery', blank=True)
    background_image = models.ImageField(upload_to='gallery', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = "8 Gallery"
        verbose_name = "Details"


class Reviews(models.Model):
    name = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='gallery', blank=True)
    review = models.CharField(max_length=400, null=False)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "9 Reviews"
        verbose_name = "Reviews"


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

    class Meta:
        verbose_name_plural = "910 our details"
        verbose_name = "Details"


class ContactForm(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone = models.CharField(max_length=10, null=False)
    message = models.TextField(max_length=1000, null=False)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "911 Contact forms"
        verbose_name = "Details"
        ordering = ('-date',)


class BackgroundImage(models.Model):
    name = models.CharField(max_length=15, blank=True)
    image1 = models.ImageField(upload_to='background', blank=True)
    image2 = models.ImageField(upload_to='background', blank=True)
    image3 = models.ImageField(upload_to='background', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "912 Background Image"
        verbose_name = "Details"
