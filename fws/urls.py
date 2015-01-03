from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]