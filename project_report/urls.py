from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('tracker.urls')),
    path('', RedirectView.as_view(pattern_name='tracker:list', permanent=False)),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='tracker/login.html'
    ), name='login'),

    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
