from django.urls import path
from . import views

urlpatterns = [
    path("campaigns/", views.CampaignListAPIView.as_view(), name="campaigns"),
    path("campaigns/<str:slug>/", views.CampaignDetailAPIView.as_view(), name="campaign"),
    path("subscribe/", views.SubscribeToCampaignAPIView.as_view(), name="subscribe"),
]
