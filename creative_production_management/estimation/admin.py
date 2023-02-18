from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(CSO)
admin.site.register(Designer)
admin.site.register(Task)
admin.site.register(Vendor)
admin.site.register(Service)
admin.site.register(VendorService)

