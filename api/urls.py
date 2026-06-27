from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.get_portfolio_data, name='portfolio_data'),
    path('contact/', views.contact_submit, name='contact_submit'),
]
