from django.urls import path
from . import views
urlpatterns=[
    path('',views.intro_view,name='intro-view'),
    path('home/',views.home,name='home'),
    path('add-contact',views.addContact,name='add-contact'),
    path('update-contact/<int:id>',views.updateContact,name='update-contact'),
    path('delete-contact/<int:id>',views.deleteContact,name='delete-contact'),
]