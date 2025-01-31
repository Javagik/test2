from django.urls import path
from .views import HomePageView , AboutPageView, ContentListView, ContentDetailView, ContentCreateView, ContentUpdateView, ContentDeleteView, UserContentListView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('content-list/', ContentListView.as_view(), name='content'),
    path('content/<int:pk>', ContentDetailView.as_view(), name='content_detail'),
    path('content/create', ContentCreateView.as_view(), name='content_create'),
    path('content/<int:pk>/edit', ContentUpdateView.as_view(), name='content_update'),
    path('content/<int:pk>/delete', ContentDeleteView.as_view(), name='content_delete'),
    path('usercontent/', UserContentListView.as_view(), name='usercontent'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

]