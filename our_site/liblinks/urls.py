from django.urls import path

from .views import *

urlpatterns = [
   path('', LiblinksCreate.as_view(), name='LiblinksCreate'),
   path('retrieves/', LiblinksRetrieve.as_view(), name='LiblinksRetrieve'),
   path('<int:pk>', LiblinksDetail.as_view(), name='LiblinksDetail'),
   path('<int:pk>/update/', LiblinksUpdate.as_view(), name='LiblinksUpdate'),
   path('<int:pk>/delete/', LiblinksDelete.as_view(), name='LiblinksDelete'),
]
