
from django.contrib import admin
from .models import Employees,Timeline,Product,Home,Product_other


# Register your models here.
class displaytbl(admin.ModelAdmin):
    list_display = ('name', 'dp', 'email', 'phone', 'role')


admin.site.register(Employees, displaytbl)

class timelinetbl(admin.ModelAdmin):
    list_display = ('year','tag','desc')


admin.site.register(Timeline, timelinetbl)

class producttbl(admin.ModelAdmin):
    list_display = ('pname','ppic','ptype','pdesc')
admin.site.register(Product, producttbl)

class otherproducttbl(admin.ModelAdmin):
    list_display = ('pname','ppic','pdesc','potype')
admin.site.register(Product_other, otherproducttbl)

class hometbl(admin.ModelAdmin):
    list_display = ('pic','tag','desc','active')
admin.site.register(Home, hometbl)