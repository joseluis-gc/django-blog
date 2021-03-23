from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    #path('blog/', include('blog.urls')),
]