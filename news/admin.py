from django.contrib import admin
from news.models import BookArrival, MediaCoverage, NewsDetail

@admin.register(BookArrival)
class BookArrivalAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'image')
    search_fields = ('title', 'author')

@admin.register(MediaCoverage)
class MediaCoverageAdmin(admin.ModelAdmin):
    list_display = ('title', 'coverage_period', 'description', 'image')
    search_fields = ('title',)
    
@admin.register(NewsDetail)
class NewsDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)