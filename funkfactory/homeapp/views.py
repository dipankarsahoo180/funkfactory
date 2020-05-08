from django.shortcuts import render, redirect
from .models import (HomePictures, Cards, ContactForm, AboutUs,
                     ClassAbout, Notice, DanceStyleWeTeach,
                     FacultiesProfile, FunkFactoryGallery, Reviews,
                     OurDetail, Passwords)
from django.db.models import manager
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.


def home(request):
    queryset_pictures = HomePictures.objects.all()
    queryset_Cards = Cards.objects.all()
    queryset_AboutUs = AboutUs.objects.all().first()
    queryset_AboutClass = ClassAbout.objects.all().first()
    queryset_NoticeClass = Notice.objects.all()
    queryset_Dance_styles = DanceStyleWeTeach.objects.all()
    queryset_Faculties = FacultiesProfile.objects.all()
    queryset_gallery = FunkFactoryGallery.objects.all()
    queryset_reviews = Reviews.objects.all()
    queryset_client_details = OurDetail.objects.all().first()
    queryset_passwords = Passwords.objects.all()
    if request.method == "POST":
        print(request.POST)
        if "contact_submit" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            form = ContactForm(name=name, email=email, phone=phone, message=message)
            form.save()
            text = "Hi " + name + "! Thank you for contacting us."
            messages.success(request, text)
            return redirect('/')

        elif "sign_up" in request.POST:
            try:
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                username = request.POST.get('username')
                password = request.POST.get('password1')
                password2 = request.POST.get('password2')
                email = request.POST.get('email')
                form = User.objects.create_user(username=username, first_name=first_name,
                                                last_name=last_name, email=email, password=password)
                form.save()
                text = "Hi " + str(first_name) + "! Your account has been created successfully."
                messages.success(request, text)
                password = Passwords(username=username, email=email, password=password)
                password.save()
                print(password)
                return redirect('/')
            except:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'user already there')
                    gotodiv = 'small-dialog'
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already registered')
                    gotodiv = 'small-dialog'

                return redirect('/')

    context = {'pictures': queryset_pictures, 'cards': queryset_Cards,
               'about': queryset_AboutUs, 'classSummary': queryset_AboutClass,
               'notifications': queryset_NoticeClass, 'dance_styles': queryset_Dance_styles,
               'instructors': queryset_Faculties, 'gallery': queryset_gallery,
               'reviews': queryset_reviews, 'details': queryset_client_details}
    return render(request, 'index.html', context)
