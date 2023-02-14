from django.shortcuts import render
from .models import Skill, Service, Experience, Education, UserContact
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def welcome(request):
    return render(request, 'welcome.html')


def about(request):
    skills = Skill.objects.all()
    ctx = {
        'skills': skills,
    }
    return render(request, 'about.html', ctx)


def services(request):
    services = Service.objects.all()
    ctx = {
        'services': services,
    }
    return render(request, 'services.html', ctx)


def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    ctx = {
        'educations': educations,
        'experiences': experiences,
    }
    return render(request, 'resume.html', ctx)


def works(request):
    return render(request, 'works.html')


def contact(request):
    sent = False
    if request.POST:
        # model = UserContact()
        # model.name = request.POST.get('name', None)
        # model.email = request.POST.get('email', None)
        # model.subject = request.POST.get('subject', None)
        # model.message = request.POST.get('message', None)
        # model.save()
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = f"{request.POST.get('name')} who is a" \
                  f" {subject} sent you the message : " \
                  f"{request.POST.get('message')} from the mail : {email}"
        send_mail(subject, message, 'abbosr180@gmail.com', [email])
        sent = True
        # ... send email
    return render(request, 'contact.html')


def team(request):
    return render(request, 'team.html')
