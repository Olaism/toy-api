from django.urls import path

from .views import (
    toy_list,
    toy_detail
)

urlpatterns = [
    path("", toy_list),
    path("<int:toy_pk>", toy_detail)
]