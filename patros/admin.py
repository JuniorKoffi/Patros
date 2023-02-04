from django.contrib import admin
from .models import About, Service, Lblog, Team, Portfolio, Localisation, Contact

admin.site.register(About)
admin.site.register(Service)
admin.site.register(Lblog)
admin.site.register(Team)
admin.site.register(Portfolio)
admin.site.register(Localisation)
admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'contenus', 'date_add', 'active')
    list_filter = ('active', 'date_add')
    search_fields = ('nom', 'email', 'contenus')
    actions = ['approve_contact']

    def approve_contact(self, request, queryset):
        queryset.update(active=True)