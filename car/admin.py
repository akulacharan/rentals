from django.contrib import admin
from . models import Cars,Orders,Contact

# Register your models here.

admin.site.register(Cars)
admin.site.register(Orders)
admin.site.register(Contact)