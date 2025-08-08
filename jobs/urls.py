from django.urls import path
from . import views
from .views import my_jobs

urlpatterns = [
      path('', views.job_list, name='job_list'),
      path('post/', views.post_job, name='post_job'),
      path('my/', my_jobs, name='my_jobs'),
    

]
