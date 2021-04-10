from django.shortcuts import render
from .models import *
from .filters import JobFilter


def loginPage(request):
    return render(request, 'portal/login.html')


def signup(request):
    return render(request, 'portal/register.html')


def homePage(request):
    jobs = Job.objects.filter(approved=True).order_by('-created')
    context = {
        'jobs': jobs
    }
    return render(request, 'portal/index.html', context)


def jobs(request):
    jobs = Job.objects.filter(approved=True).order_by('-created')

    filters = JobFilter(request.GET, queryset=jobs)
    jobs = filters.qs

    context = {
        'jobs': jobs,
        'filters':filters
    }
    return render(request, 'portal/search.html', context)


# Job Detail View
def jobDetail(request, slug):
    jobs = Job.objects.filter(approved=True).order_by('-created')

    try:
        job = Job.objects.get(approved=True, slug=slug)
        requirements = job.requirements.all()
    except Exception:
        pass

    context = {
        'job': job,
        'jobs': jobs,
        'requirements': requirements,
    }
    return render(request, 'portal/single.html', context)


def blog(request):
    return render(request, 'portal/blog-home.html')


def contact(request):
    return render(request, 'portal/contact.html')


def about(request):
    return render(request, 'portal/about-us.html')
