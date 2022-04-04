from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.APIRoot.as_view(), name='root'),
    path('api/parameters/', views.ParameterListCreateView.as_view(), name='parameter-list-create'),
    path('api/parameters/<int:pk>/', views.ParameterRetrieveUpdateDestroyView.as_view(), name='parameter-detail'),
]
