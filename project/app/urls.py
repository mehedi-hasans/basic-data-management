
from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name='home' ),
  path('delete/<str:id>', views.detetePage, name='deletePage' ),
  path('editPage/<str:id>', views.editPage, name='editPage' ),
  path('updatePage/<str:id>', views.updatePage, name='updatePage' )
]


# path('myAdmin/Student/deleteStudent/<str:id>', views.deleteStudent,name="deleteStudent"),