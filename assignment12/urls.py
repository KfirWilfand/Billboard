from django.conf.urls import include, url
from django.contrib import admin
from billboard import views


urlpatterns = [
    url(r'^$', include('billboard.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^register', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/$', views.logout, kwargs={'next_page': '/'},
        name='logout'),

]
