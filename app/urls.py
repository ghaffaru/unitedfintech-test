from django.urls import path
from .views import authViews, employeeCrudViews
urlpatterns = [

    path('login', authViews.LoginView.as_view()),

    path('add_employee', employeeCrudViews.AddEmployeeView.as_view())

]