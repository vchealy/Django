# cities/views.py
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import City


class HomePageView(TemplateView):
    template_name = "cities/home.html"


class SearchResultsView(ListView):
    model = City
    template_name = "cities/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(country__icontains=query)
        )
        return object_list
