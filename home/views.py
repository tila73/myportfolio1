from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    biodata = BioData.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    works = Work.objects.all()
    contact_form = ContactForm
    context = {'biodata':biodata, 'skills':skills, 'services':services, 'works':works, 'form':contact_form}
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            subject = "Contact form"
            body = {
                'full_name': contact_form.cleaned_data['full_name'],
                'email': contact_form.cleaned_data['email'],
                'subject': contact_form.cleaned_data['subject'],
                'message': contact_form.cleaned_data['message'],
            }
            message="\n".join(body.values())
            try:
                send_mail(subject, message, 'lebisha0thapa@gmail.com', ['lebisha0thapa@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Bound')
            return redirect('home')
    return render(request, "home/index.html", context)
