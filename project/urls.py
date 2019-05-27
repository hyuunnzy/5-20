from django.contrib import admin
from django.urls import path, include
import blog.views
import accouts.views
import word.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name="home"),
    path('blog/', include('blog.urls')),
    path('accouts/', include('accouts.urls')),
    path('word/', include('word.urls')),
]
