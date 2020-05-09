from django.contrib import admin
from .models import (HomePictures, ContactForm, AboutUs,
                     ClassAbout, Notice, DanceStyleWeTeach, FacultiesProfile,
                     FunkFactoryGallery, Reviews, OurDetail, Passwords)

# Register your models here.
admin.site.register(HomePictures)
admin.site.register(ContactForm)
admin.site.register(AboutUs)
admin.site.register(ClassAbout)
admin.site.register(Notice)
admin.site.register(DanceStyleWeTeach)
admin.site.register(FacultiesProfile)
admin.site.register(FunkFactoryGallery)
admin.site.register(Reviews)
admin.site.register(OurDetail)
admin.site.register(Passwords)