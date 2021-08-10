from django.urls import path
from . import views

urlpatterns = [
    path('main-page', views.main_page, name='main'),
    path('about-me', views.page_about_me, name='about_me'),
    path('skills', views.page_skills, name='page_skills'),
    path('causes', views.page_cause, name='page_causes'),
    path('feedback', views.FeedbackCreateView.as_view(), name='feedback'),
]