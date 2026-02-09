from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("resume/", views.resume, name="resume"),
    path("achievements/", views.achievements, name="achievements"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("contact/", views.contact, name="contact"),
    path("contacts/", views.contact_list, name="contacts"),
    path('portfolio/add/', views.add_project, name='add_project'),
    path('portfolio/<str:project_name>/', views.detailedPortfolio, name = 'detailed_portfolio'),
    path('login/', auth_views.LoginView.as_view(template_name='PortfolioDatabase/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('portfolio/edit/<int:project_id>/', views.edit_project, name='edit_project'),
    path('portfolio/delete/<int:project_id>/', views.delete_project, name='delete_project'),


]

