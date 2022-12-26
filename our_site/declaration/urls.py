from django.urls import path
from .views import *

app_name = 'declaration'


urlpatterns = [
    path('', DeclarationCreate.as_view(), name='DeclarationCreate'),
    path('retrieves/', DeclarationRetrieve.as_view(), name='DeclarationRetrieve'),
    path('<int:pk>', DeclarationDetail.as_view(), name='DeclarationDetail'),
    path('<int:pk>/update/', DeclarationUpdate.as_view(), name='DeclarationUpdate'),
    path('<int:pk>/delete/', DeclarationDelete.as_view(), name='DeclarationDelete'),
]
