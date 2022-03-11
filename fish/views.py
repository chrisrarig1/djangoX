from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Fish

class FishListView(ListView):
    template_name = 'fishpage/fish_list.html'
    model = Fish


class FishDetailView(DetailView):
    template_name = 'fishpage/fish_detail.html'
    model = Fish

class FishCreateView(CreateView):
    template_name = 'fishpage/fish_create.html'
    model = Fish
    fields = ['species','angler','description']

class FishUpdateView(UpdateView):
    template_name = 'fishpage/fish_update.html'
    model = Fish
    fields = ['species','angler','description']

class FishDeleteView(DeleteView):
    template_name = 'fishpage/fish_delete.html'
    model = Fish
    success_url = reverse_lazy('fish_list')