from django.conf.urls import url

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'', views.index, name='index'),

]
