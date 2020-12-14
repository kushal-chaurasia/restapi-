
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cardcreate', views.card_create),
    path('cardinfo/<int:ck>', views.card_detail),
]
