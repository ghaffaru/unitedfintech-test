from django.urls import path
from .views import authViews, employeeCrudViews
urlpatterns = [

    path('login', authViews.LoginView.as_view()),

    path('employee', employeeCrudViews.EmployeeView.as_view()),

    path('employee/<id>', employeeCrudViews.FetchOneEmployee.as_view()),

    path('employeeUpdate/<id>', employeeCrudViews.UpdateOneEmployee.as_view()),

    path('employeeDelete/<id>', employeeCrudViews.DeleteEmployee.as_view())
]