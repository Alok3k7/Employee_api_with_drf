from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('logout/', views.logout_user),

    path('employees/', views.EmployeeListCreateView.as_view()),
    path('employees/all/', views.all_employees),
    path('employees/<int:pk>/', views.employee_detail),
    path('employees/<int:pk>/deactivate/', views.deactivate_employee),
    path('employees/<int:pk>/activate/', views.activate_employee),

    path('cities/', views.city_list),
]
