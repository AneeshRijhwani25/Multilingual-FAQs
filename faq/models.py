from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = models.TextField(blank=True, null=True)
    answer_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        self.question_hi = translator.translate(self.question, dest='hi').text
        self.question_bn = translator.translate(self.question, dest='bn').text
        self.answer_hi = translator.translate(self.answer, dest='hi').text
        self.answer_bn = translator.translate(self.answer, dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        translations = {
            'en': self.question,
            'hi': self.question_hi or self.question,
            'bn': self.question_bn or self.question,
        }
        if lang not in translations:
            try:
                translator = Translator()
                return translator.translate(self.question, dest=lang).text
            except Exception:
                return self.question  
        return translations.get(lang, self.question)

    def get_translated_answer(self, lang='en'):
        translations = {
            'en': self.answer,
            'hi': self.answer_hi or self.answer,
            'bn': self.answer_bn or self.answer,
        }
        if lang not in translations:
            try:
                translator = Translator()
                return translator.translate(self.answer, dest=lang).text
            except Exception:
                return self.answer  
        return translations.get(lang, self.answer)

    def __str__(self):
        return self.question