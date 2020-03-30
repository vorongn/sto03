from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = 'sto'

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles_list'),
    path('articles/<int:article_id>/', views.ArticleDetailViews.as_view(), name='article_detail'),

    path('clients/', views.ClientsView.as_view(), name='clients'),
    path('clients/<int:client_id>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', views.create_client, name='create_client'),

    path('cars/', views.CarsView.as_view(), name='cars'),
    path('cars/<int:car_id>/', views.CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', views.create_car, name='create_car'),

    path('repairs/', views.repairs, name='repairs'),
    path('repairs/<int:repair_id>/', views.repair_detail, name='repair_detail'),
    path('repairs/create/', views.create_repair, name='create_repair'),

    path('works/create/', views.create_works, name='create_works'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
