from django.urls import path
from .views import KursCreate, KursDetail, KursRetrieve, KursUpdate, KursDelete

app_name = 'kurs'


urlpatterns = [
    path('', KursCreate.as_view(), name='KursCreate'),
    path('retrieves/', KursRetrieve.as_view(), name='KursRetrieve'),
    path('<int:pk>', KursDetail.as_view(), name='KursDetail'),
    path('<int:pk>/update/', KursUpdate.as_view(), name='KursUpdate'),
    path('<int:pk>/delete/', KursDelete.as_view(), name='KursDelete'),
]
