
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token 
from api import views
from api.auth import CustomAuthToken

router = DefaultRouter()

router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),  
    # to enable login in browsable API, we have
    # to use its built in URL 
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',CustomAuthToken.as_view()),
]
