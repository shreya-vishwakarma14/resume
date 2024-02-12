from django.urls import path
from . import views
# #This will import our view that we have already created
from .views import GeneratePdf,display_data

urlpatterns = [
    # path('', views.home_invoice),
    # path('home/', views.demo_page),
  
    path('display/', display_data, name='display_data'),
    path('pdf-invoice/', GeneratePdf.as_view()),
   
 
]