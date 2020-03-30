from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Client, Car, Repair
from django.db.models import Q
from . import forms
from django.urls import reverse
from django.views.generic import View, ListView
from django.db.models.functions import Lower


# Create your views here.


class ArticlesView(ListView):
    """статьи для главной"""

    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'articles/articles_list.html', {'articles': articles})


class ArticleDetailViews(View):
    """статья подробно"""

    def get(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
        except:
            raise Http404("Материал не найден")
        return render(request, 'articles/article_detail.html',
                      {'article': article})


class ClientsView(ListView):
    """список клиентов"""

    def get(self, request):

        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            query = query.lower()

        else:
            query = ''

        clients = Client.objects.all().order_by('first_name')
        clients = clients.filter(Q(last_name__icontains=query)
                                 | Q(first_name__icontains=query)
                                 | Q(phone_number__icontains=query))
        return render(request, 'clients/list_clients.html', {'client_list': clients, 'search_query': query})


class ClientDetailView(View):
    """клиент подробно"""

    def get(self, request, client_id):
        client = Client.objects.get(id=client_id)
        return render(request, 'clients/detail_client.html', {'client_detail': client})


def create_client(request):
    """"добавить клиента"""
    if request.method == 'POST':
        client_form = forms.ClientForm(request.POST)
        if client_form.is_valid():
            new_material = client_form.save(commit=False)
            new_material.save()
            return render(request, 'clients/detail_client.html', {'client_detail': new_material})
    else:
        client_form = forms.ClientForm()
    return render(request, "clients/create_client.html", {'form': client_form}, )

#----------------------------------------------------------------------------------------------------


class CarsView(ListView):

    def get(self, request):
        """список авто
            с фильтром по гомномеру
            """
        if request.GET.get('q'):
            query = request.GET.get('q')
        else:
            query = ''
        latest_car_list = Car.objects.order_by('number').filter(Q(number__icontains=query))
        return render(request, 'cars/list_cars.html',
                      {'latest_car_list': latest_car_list, 'search_query': query})


class CarDetailView(View):

    def get(self, request, car_id):
        """авто подробно"""
        try:
            all_repairs = Repair.objects.filter(car=car_id).order_by('-date')
            a = Car.objects.get(id=car_id)
            clients = Client.objects.filter(cars=car_id)
        except:

            raise Http404("Нет элемента")
        return render(request,
                      'cars/detail_car.html',
                      {'car': a, 'all_repairs': all_repairs, 'clients': clients})


def create_car(request):
    """"добавить авто"""
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            new_car = car_form.save(commit=False)
            new_car.save()
            return render(request, 'cars/detail_car.html', {'car_detail': new_car, })
    else:
        car_form = forms.CarForm
    return render(request, "cars/create_car.html", {'form': car_form, })


def repairs(request):
    latest_repair_list = Repair.objects.order_by('-id')
    return render(request, 'repairs/list_repairs.html', {'latest_repair_list': latest_repair_list})


def repair_detail(request, repair_id):
    """ремонт подробно"""
    try:
        a = Repair.objects.get(id=repair_id)
        clients = Client.objects.filter(cars=a.car)
    except:
        raise Http404("Нет элемента")
    return render(request, 'repairs/detail_repair.html', {'repair': a, 'clients': clients})


def create_repair(request):
    """"добавить ремонт"""
    if request.method == 'POST':
        repair_form = forms.RepairForm(request.POST)
        if repair_form.is_valid():
            new_repair = repair_form.save(commit=False)
            new_repair.save()
            return render(request, 'repairs/detail_repair.html', {'repair': new_repair, })
    else:
        repair_form = forms.RepairForm
    return render(request, "repairs/create_repair.html", {'form': repair_form}, )


def create_works(request):
    """"добавить клиента"""
    if request.method == 'POST':
        work_form = forms.WorksForm(request.POST)
        if work_form.is_valid():
            new_work = work_form.save(commit=False)
            new_work.save()
            return render(request, 'works/detail_work.html', {'works_detail': new_work})
    else:
        work_form = forms.WorksForm()
    return render(request, "works/create_works.html", {'form': work_form}, )