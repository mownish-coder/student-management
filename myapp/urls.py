from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.details_list,name='details_list'),
    path("details_create/",views.details_create,name='details_create'),
    path("update/<int:id>",views.details_update,name='details_update'),
    path("delete/<int:id>",views.details_delete,name='details_delete'),
]