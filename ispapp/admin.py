from django.contrib import admin
from .models import (
    Packages, Bloglist, Blog, Lead, AdminDashboardProfile,
    HeroCarousel, WhyUs, AboutUs, ServiceArea, ContactInfo
)

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'speed', 'unit', 'price')
    list_filter = ('category',)

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

@admin.register(HeroCarousel)
class HeroCarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not AboutUs.objects.exists()

@admin.register(ServiceArea)
class ServiceAreaAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()

admin.site.register(AdminDashboardProfile)