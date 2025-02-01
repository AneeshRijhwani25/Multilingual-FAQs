from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer','translated_question_hi', 'translated_question_bn', 'translated_answer_hi', 'translated_answer_bn')
    search_fields = ('question', 'answer')

    def translated_question_hi(self, obj):
        return obj.get_translated_question('hi') or obj.question
    translated_question_hi.short_description = 'Hindi Question'

    def translated_question_bn(self, obj):
        return obj.get_translated_question('bn') or obj.question
    translated_question_bn.short_description = 'Bengali Question'

    def translated_answer_hi(self, obj):
        return obj.get_translated_answer('hi') or obj.answer
    translated_answer_hi.short_description = 'Hindi Answer'

    def translated_answer_bn(self, obj):
        return obj.get_translated_answer('bn') or obj.answer
    translated_answer_bn.short_description = 'Bengali Answer'