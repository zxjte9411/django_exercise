from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


class ChoiseInline(admin.TabularInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin_Fieldsets(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiseInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['question_text', 'pub_date']
    search_fields = ['question_text']
    
# admin.site.register(Question, QuestionAdmin_Fieldsets)