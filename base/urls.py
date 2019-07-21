from django.contrib import admin
from django.urls import path

from base.views import HomeView, ProjectsView, EmployeesView, ProfileView, ScopeView, loginView, logoutView, base_login, get_photo, upload_photo

urlpatterns = [
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('scope/<int:scope_id>/', base_login(ScopeView.as_view()), name='scope'),
    path('photo/', base_login(get_photo), name='photo'),
    path('upload_photo/', base_login(upload_photo), name='upload_photo'),
    path('projects/', base_login(ProjectsView.as_view()), name='projects'),
    path('employees/', base_login(EmployeesView.as_view()), name='employees'),
    path('',  base_login(ProjectsView.as_view()), name='home'),
]