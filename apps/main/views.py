from django.shortcuts import render
from django.views import generic

from apps.main.models import Page


def index(request):
    return render(request, 'index.html')


class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    queryset = Page.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'breadcrumbs': {'current': self.object}})
        return context
