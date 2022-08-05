from django.urls import path, include
from api import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('resume/', views.ProfileView.as_view()),
    path('list/', views.ProfileView.as_view()),
    path('<int:id>/', views.ProfileView.as_view()),

]
