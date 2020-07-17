from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request,'project_index.html',context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) #retrieves a query based on the primary key
    context = {
        'project' : project
    }
    return render(request, 'project_detail.html', context)
""" 
def blog_index(request):
    return render(request, 'project_index.html')
"""