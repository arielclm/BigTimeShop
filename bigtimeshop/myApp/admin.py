from django.contrib import admin


from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['pk','Cname','Cquantity','isDelete']
    list_filter = ['Cname']



class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'pname', 'pdate','pprice','pstock','pcategory', 'isDelete']
    list_filter = ['pname']

    fieldsets = [
        ("num", {"fields": ['pprice', 'pstock']}),
        ("base", {"fields": ['pname', 'pdate', 'pcategory','isDelete']})
    ]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
