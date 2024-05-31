# urls.py
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from . import views
urlpatterns = [

    path('token/', views.MyTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("",views.index, name="index" ),
    path("add_data/",views.AddstatsticsData.as_view(), name="add_data" ),
    path("statsics/",views.StatsticsListView.as_view(), name="statsics-list" ),
    path("dashboard/",views.DashboardDataView.as_view(), name="dashboard" ),
]   
