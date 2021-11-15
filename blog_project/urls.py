from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('profiles/', include('profiles.urls', namespace='profiles ')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    url('auth/', include('djoser.urls.jwt')),

    ]

