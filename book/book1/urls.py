from django.conf import settings
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
  path('',views.f1,name="welcome"),
    path('home/', views.f5, name="home"),
    path('books/<str:name>/',views.f2,name="books"),
    path('authors/', views.f4, name="authors"),
    path('login-registration/', views.f3 , name="login-registration"),
    path('about/',views.f7,name="about"),
    path('cart/',views.f6,name="cart")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

