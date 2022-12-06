from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('getReviewPopup/', views.ajax_get_review_popup),
    path('getReviewDetail/', views.ajax_get_review_detail),
    path('writeReview/', views.ajax_write_review),
]
