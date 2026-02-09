from django.shortcuts import render, get_object_or_404, redirect
from PortfolioDatabase.models import Portfolio, Contact
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from PortfolioDatabase.contactForm import ContactModelForm, PortfolioForm


def home(request):
    return render(request, 'PortfolioDatabase/home.html', {})

def resume(request):
    return render(request, 'PortfolioDatabase/resume.html', {})

def achievements(request):
    return render(request, 'PortfolioDatabase/achievements.html', {})

def portfolio(request):
    projects = Portfolio.objects.all()
    return render(request, 'PortfolioDatabase/portfolio.html', {
        'items': projects,
        'section': 'Portfolio'
    })


def detailedPortfolio(request, project_name):
    project = get_object_or_404(Portfolio, project_title=project_name)
    return render(request, 'PortfolioDatabase/detailedPortfolio.html', {
        'item': project.project_summary(),
        'section': 'Portfolio',
    })

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact_instance = form.save()
            print("Saved Contact and message: ", contact_instance)
            return redirect('contact')
    else:
        form = ContactModelForm()

    context = {
        'form': form,
    }
    return render(request, 'PortfolioDatabase/contact.html', context)

def contact_list(request):
    contacts = Contact.objects.all()
    html = "<html><body><h2>Contact Submissions</h2><ul>"

    for contact in contacts:
        html += f"<li>{contact.name} — {contact.email} — {contact.message}</li>"

    html += "</ul></body></html>"
    return HttpResponse(html)

@login_required
def add_project(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = PortfolioForm()
    return render(request, 'PortfolioDatabase/addProject.html', {
        'form': form,
        'section': 'Add Project'
    })

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Portfolio, id=project_id)
    form = PortfolioForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('portfolio')
    projects = Portfolio.objects.all()
    return render(request, 'PortfolioDatabase/editProject.html', {
        'form': form,
        'section': 'Edit Project'
    })


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Portfolio, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio')
    return render(request, 'PortfolioDatabase/deleteProject.html', {
        'project': project,
        'section': 'Delete Project'
    })


