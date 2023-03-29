from contact import views as conctac_views
from django.urls import path

urlpatterns =[
    path('contact/', conctac_views.contact, name='contact'),

]