
from django.contrib import admin
from django.urls import path, include

from schoolManagementApp import views
from knox import views as knox_views

from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register('schools', views.SchoolViewSet)
router.register('students', views.StudentViewSet)

school_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
school_router.register(r'students', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', views.RegisterAPI.as_view(), name='register'),
    path('auth/login/', views.LoginAPI.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('', include(school_router.urls)),
]
