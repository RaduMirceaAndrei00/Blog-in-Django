from django.shortcuts import render
from .models import ProjectsAndAchievements, TechnicalSkills, Skills, Awards, Languages

def cv(request):
    projects_and_achievements = ProjectsAndAchievements.objects.all()
    technical_skills = TechnicalSkills.objects.all()
    skills = Skills.objects.all()
    awards = Awards.objects.all()
    languages = Languages.objects.all()
    return render(request, 'cv/cv.html', {'projects_and_achievements': projects_and_achievements, 'technical_skills': technical_skills, 'skills': skills, 'awards': awards, 'languages': languages})

