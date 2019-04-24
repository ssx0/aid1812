from django.contrib import admin
from .models import *

#ModelAdmin
class AutAdmin(admin.ModelAdmin):
    list_display = ('name','age','email','isActive')

    list_display_links = ('name','email')

    list_editable = ('age',)

    list_filter = ('isActive',)

    search_fields = ('name',)

    # fields = ('name','email','age')

    # fieldsets = (
    #     ("基本选项",{
    #         'fields':('name','age'),
    #     }),
    #     ("高级选项",{
    #         'fields':('email','isActive'),
    #         'classes':('collapse',)
    #     })
    # )

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publicate_date')

    date_hierarchy = "publicate_date"


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city')
    list_editable = ('address','city')
    list_filter = ('city','country')
    search_fields = ('name','website')
    fieldsets = (("基本选项",{
        'fields':('name','address','city')
    }),("高级选项",{
        'fields': ('country', 'website'),
        'classes': ('collapse',)
    })
                 )

# Register your models here.

admin.site.register(Author,AutAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife)