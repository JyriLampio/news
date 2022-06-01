"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rss import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rss/', views.RssListView.as_view()),
	#path('rss/<int:pk>', views.RssDetailView.as_view()),
    path('rss/<int:pk>/', views.index),
    path('rss/create/', views.RssCreateView.as_view()),
	path('rss/<int:pk>/update', views.RssUpdateView.as_view()),
	path('rss/<int:pk>/delete', views.RssDeleteView.as_view()),

	# Authentication
	path('accounts/login/', LoginView.as_view()),
	path('accounts/logout/', LogoutView.as_view()),
    path('accounts/register/', views.RegisterView.as_view())    
]
