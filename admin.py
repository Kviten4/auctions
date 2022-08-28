from django.contrib import admin
from .models import User, Lot, Category, Comments, Bids
# Register your models here.

admin.site.register(User)
admin.site.register(Lot)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Bids)