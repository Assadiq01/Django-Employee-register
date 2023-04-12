from django.urls import path 
from .views import employee_list, employee_detail, department_list, department_detail, add_employee, update_employee, index, read_more, delete_employee

app_name = 'employee_register'

urlpatterns = [ 
    path('', index, name='index'),
    path('employee_list/', employee_list, name='employee_list'),
    path('read_more/', read_more, name='read_more'), 
    path('detail/<int:pk>/', employee_detail, name='detail'), 
    path('add_employee/', add_employee, name='add_employee'),
    path('update_employee/<int:pk>/', update_employee, name='update_employee'),
    path('department/', department_list, name='department_list'), 
    path('department_detail/<int:pk>/', department_detail, name='department_detail'),
    path('delete_employee/<int:pk>/', delete_employee, name='delete_employee'), 
]