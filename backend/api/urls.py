from django.urls import path
from .views import TODOList, TODOUpdateDelete

urlpatterns = [
    path('', TODOList.as_view()),
    path('<int:pk>', TODOUpdateDelete.as_view())
]
