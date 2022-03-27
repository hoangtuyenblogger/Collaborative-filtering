from django.shortcuts import render, HttpResponse
# Create your views here.
from .tests import get_data
from .models import *
from .collaborative_filtering_tuvanvieclam import X, correlation_matrix, get_recommend_job
from django.core.paginator import Paginator

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request,'home.html')

def search_job(request):
    query_string = request.GET.get("location")
    location_ = str(query_string)
    data = jobs.objects.filter(location=location_)
    return render(request, 'search_job.html', {"data": data})


def search(request):
    query_string = request.GET.get("keyword")
    keyword = str(query_string)
    data = jobs.objects.filter(title__contains=keyword)

    paginator = Paginator(data, 10)  # Show 10 page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_job.html', {"data": data}, {'page_obj': page_obj})


def about(request):
    return render(request,'about.html')

def post(request):
    id_job = request.GET.get('id_job')
    i = int(id_job)
    recommend = get_recommend_job(i, 4)

    data1 = jobs.objects.filter(id__in=recommend)
    data = jobs.objects.get(id=id_job)
    return render(request,'post.html', {"data": data,"data1":data1})

def page_404(request,exception):
    return render(request, '404.html')
def page_500(request,exception):
    return render(request, '500.html')
def report(request):
    return render(request, 'report.html')