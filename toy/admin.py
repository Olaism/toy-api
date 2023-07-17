from django.contrib import admin

from toy.models import Toy
@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'was_included_in_home', 'release_date')