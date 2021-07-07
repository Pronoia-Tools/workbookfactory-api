from django.contrib import admin
from .models import Workbook, Chapter, Page, Question, Answer

admin.site.register(Workbook)
admin.site.register(Chapter)
admin.site.register(Page)
admin.site.register(Question)
admin.site.register(Answer)