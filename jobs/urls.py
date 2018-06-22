from django.urls import path,include
import jobs.views

urlpatterns = [
    path('',jobs.views.home,name='home'),
    path('blog/', include('blog.urls'),name='blog'),
]
