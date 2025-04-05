from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Maps the root URL to the home view
    path('tuf/', views.tuf, name='tuf'),
    path('zephyrus/', views.zephyrus, name='zephyrus'),
    path('zenbook/', views.zenbook, name='zenbook'),
    path('strix/', views.strix, name='strix'),
    path('vivobook/', views.vivobook, name='vivobook'),
    path('feedback/delete/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
]

