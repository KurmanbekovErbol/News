from rest_framework import viewsets
from news.models import BookArrival, MediaCoverage, NewsDetail
from news.serializers import BookArrivalSerializer, MediaCoverageSerializer, NewsDetailSerializer

class BookArrivalViewSet(viewsets.ModelViewSet):
    queryset = BookArrival.objects.all()
    serializer_class = BookArrivalSerializer

class MediaCoverageViewSet(viewsets.ModelViewSet):
    queryset = MediaCoverage.objects.all()
    serializer_class = MediaCoverageSerializer

class NewsDetailViewSet(viewsets.ModelViewSet):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailSerializer
