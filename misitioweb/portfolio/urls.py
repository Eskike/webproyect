from portfolio import views as portfolio_views
from django.urls import path

urlpatterns =[
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),

]