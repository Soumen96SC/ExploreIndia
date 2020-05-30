

# Register your models here.
from django.contrib import admin
from .models import Destination,Ppd,Hotels,TransactionHistory
# Register your models here.
admin.site.register(Destination)
admin.site.register(Ppd)
admin.site.register(Hotels)
admin.site.register(TransactionHistory)