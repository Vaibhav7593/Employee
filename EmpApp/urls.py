
from atexit import register
from EmpApp import views
from django.urls import path

urlpatterns = [
    path('home/',views.home),
    path('add/',views.add_employee),
    path('list/',views.list_emp),
    path('detail/<int:id>/',views.emp_detail),
    path('update/<int:id>/',views.emp_update),
    path('delete/<int:id>/',views.emp_delete),
    path('register/',views.register_view)
]
