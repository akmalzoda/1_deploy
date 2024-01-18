from django.urls import path

from news.views import home_page, news_detail_view

urlpatterns = [
    path('', home_page, name='home'),
    path('news/<int:id>/', news_detail_view, name='detail'),


]
