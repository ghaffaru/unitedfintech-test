from django.urls import path
from .views import authViews, employeeCrudViews
urlpatterns = [

    path('login', authViews.LoginView.as_view()),

    path('employee', employeeCrudViews.EmployeeView.as_view())

]