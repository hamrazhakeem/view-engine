from . import views
from django.urls import path

urlpatterns = [
    path('',views.home_view,name='home'),
    path('cards',views.cards_view,name='cards'),
    path('tables',views.tables_view,name='tables')
]