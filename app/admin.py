from django.contrib import admin
from .models import Content, Author, Publisher, Unit

admin.site.register(Content)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Unit)