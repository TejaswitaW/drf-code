
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,\
TokenRefreshView,TokenVerifyView


router = DefaultRouter()

router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken1'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken1'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verifytoken1'),
]
