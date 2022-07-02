

from django.urls import path

from .views import JobsListCreateAPIView,JobsDetailAPIView

urlpatterns = [
    path('jobs/', JobsListCreateAPIView.as_view(), name='jobs-list'),
    path('jobs/<int:pk>', JobsDetailAPIView.as_view(), name='jobs-detail')

]