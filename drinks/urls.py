from django.urls import path
from drinks.views import drink_list, drinks_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('drinks/', drink_list, name='drinks'),
    path('<int:id>', drinks_detail, name='drinks_detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)