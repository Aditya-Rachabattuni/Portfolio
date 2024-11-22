from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('project/ransomware/', views.project_ransomware, name='project_ransomware'),
    path('project/churn/', views.project_churn, name='project_churn'),
    path('project/spam/', views.project_spam, name='project_spam'),
    path('skills/', views.skills, name='skills'),
    path('internships/', views.internships, name='internships'),
    path('more_about_me/', views.more_about_me, name='more_about_me'),

]
