from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/whats-new/', views.category_whats_new, name='whats_new'),
    path('category/funny/', views.category_funny, name='funny'),
    path('category/learning/', views.category_learning, name='learning'),
    path('category/fake-news/', views.category_fake_news, name='fake_news'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', 
         views.post_detail, name='post_detail'),
]
