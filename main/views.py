from django.shortcuts import render
from .models import Biography, Achievement, Project, Training

def home(request):
    biography = Biography.objects.first()
    achievements = Achievement.objects.all().order_by('-date')
    projects = Project.objects.all().order_by('-launch_date')
    trainings = Training.objects.all().order_by('-date')
    context = {
        'biography': biography,
        'achievements': achievements,
        'projects': projects,
        'trainings': trainings,
    }
    return render(request, 'main/home.html', context)
