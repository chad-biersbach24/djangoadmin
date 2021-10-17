from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from api.views import ApiViews
from rest_framework.authtoken import views

from rest_framework import routers

route = routers.DefaultRouter()

route.register("", ApiViews, basename="ContactView")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('', TemplateView.as_view(template_name='index.html')),
    path('get/',TemplateView.as_view(template_name='index2.html')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')

]
