from django.shortcuts import render
from projects.models import Project
from django.core.files.storage import FileSystemStorage


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)