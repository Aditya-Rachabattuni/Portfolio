from django.shortcuts import render
from .models import Project, Skill



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    return render(request, 'contact.html')
def projects(request):
    return render(request, 'projects.html')

def project_ransomware(request):
    return render(request, 'project_ransomware.html')

def project_churn(request):
    return render(request, 'project_churn.html')

def project_spam(request):
    return render(request, 'project_spam.html')

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def internships(request):
    return render(request, 'internships.html')

def more_about_me(request):
    return render(request, 'more_about_me.html') 
