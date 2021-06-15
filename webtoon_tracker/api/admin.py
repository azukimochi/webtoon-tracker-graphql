from django.contrib import admin
from . models import Webtoon, Author, DayOfRelease

# Register your models here.
admin.site.register(Webtoon)
admin.site.register(Author)
admin.site.register(DayOfRelease)