from django.contrib import admin
from .models import card

# Register your models here.
@admin.register(card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'card_no', 'expiry', 'cvv']
