from django.urls import path
from .views import BookList,BookDetail,TokenObtainAndRetrieveView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainAndRetrieveView.as_view(), name='token_obtain_pair'),
    path('api/books/', BookList.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]