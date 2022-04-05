from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.APIRoot.as_view(), name='root'),
    path('api/parameters/', views.ParameterListCreateView.as_view(), name='parameter-list-create'),
    path('api/parameters/<int:pk>/', views.ParameterRetrieveUpdateDestroyView.as_view(), name='parameter-detail'),
    path('api/toggle-system/', views.toggle_system, name='toggle_system'),
    path('api/get-system-status/', views.GetSystemStatus.as_view(), name='get_system_status'),
]
