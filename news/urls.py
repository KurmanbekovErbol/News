from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news import views

router = DefaultRouter()
router.register(r'book_arrivals', views.BookArrivalViewSet)
router.register(r'media_coverages', views.MediaCoverageViewSet)
router.register(r'news_details', views.NewsDetailViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
