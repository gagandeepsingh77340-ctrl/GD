"""
URL configuration for GD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myapp import views
from myapp.views import chatbot 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show),
   
    path('counselling/', views.counselling, name='counselling'),
    path('counselling.html', views.counselling, name='counselling_html'),

    path('class10/', views.class10, name='class10'),
    path('class10.html', views.class10, name='class10_html'),

    path('output_10', views.output_10, name='output'),
    path('output.html', views.output_10, name='output_html'),

    path('class12/', views.class12, name='class12'),
    path('class12.html', views.class12, name='class12_html'),

    path('Arts/', views.Arts, name='Arts'),
    path('Arts.html', views.Arts, name='Arts.html'),

    path('Commerce/', views.Commerce, name='Commerce'),
    path('Commerce.html', views.Commerce, name='Commerce.html'),

    path('PCM/', views.PCM, name='PCM'),
    path('PCM.html', views.PCM, name='PCM.html'),

    path('PCB/', views.PCB, name='PCB'),
    path('PCB.html', views.PCB, name='PCB.html'),

    path('output_PCB', views.output_PCB, name='output_PCB'),
    path('output_PCB.html', views.output_PCB, name='output_PCB_html'),

    path('output_PCM', views.output_PCM, name='output_PCM'),
    path('output_PCM.html', views.output_PCM, name='output_PCM_html'),

    path('output_COM', views.output_COM, name='output_COM'),
    path('output_COM.html', views.output_COM, name='output_COM_html'),

    path('output_ARTS', views.output_ARTS, name='output_ARTS'),
    path('output_ARTS.html', views.output_ARTS, name='output_ARTS_html'),

    # chatbot here
    path('chatbot/',chatbot),

]