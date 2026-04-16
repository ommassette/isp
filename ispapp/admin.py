from django.contrib import admin
from django.contrib import admin
from .models import Packages, Bloglist, Blog, Lead

admin.site.site_header = "Tornet Admin Portal"
admin.site.site_title = "Tornet Management"
admin.site.index_title = "Site Content Manager"

# Register your models here.
from .models import Packages, Bloglist, Blog, Lead, AdminDashboardProfile

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'speed', 'unit', 'price')

@admin.register(Bloglist)
class BloglistAdmin(admin.ModelAdmin):
    list_display = ('heading', 'date')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('main_title', 'author', 'date')

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'interested_package', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(AdminDashboardProfile)
class AdminDashboardProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_notified_on_new_lead')