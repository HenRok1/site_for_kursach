from django.urls import path
from .views import upload_resume, SearchResultsView


urlpatterns = [
    path('',upload_resume, name = "files"),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
]