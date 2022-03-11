from django.urls import path
from .views import FishDetailView,FishListView,FishCreateView,FishDeleteView,FishUpdateView

urlpatterns = [
    path('', FishListView.as_view(), name='fish_list' ),
    path('<int:pk>/', FishDetailView.as_view(), name='fish_detail'),
    path('new/', FishCreateView.as_view(), name='fish_create' ),
    path('<int:pk>/delete', FishDeleteView.as_view(), name='fish_delete'),
    path('<int:pk>/edit', FishUpdateView.as_view(), name='fish_update' ),
]