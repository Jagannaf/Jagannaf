from django.urls import path
from .views import NewsList, PostDetail

urlpatterns = [
   path('news', NewsList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
]