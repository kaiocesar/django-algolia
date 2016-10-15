from django.conf.urls import url

from searchapp import views

urlpatterns = [
	url(r'^$', views.index, name='blog.index'),
	url(r'^show/(?P<id>[\d]+)', views.show, name='blog.show'),
]