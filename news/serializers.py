from rest_framework import serializers
from news.models import BookArrival, MediaCoverage, NewsDetail

class BookArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookArrival
        fields = ['title', 'author', 'description', 'image']

class MediaCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaCoverage
        fields = ['title', 'coverage_period', 'description', 'image']

class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetail
        fields = ['title', 'description', 'image']
