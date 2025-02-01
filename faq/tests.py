from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation(self):
        faq = FAQ.objects.create(question="What is your name?", answer="<p>My name is John.</p>")
        self.assertIsNotNone(faq.question_hi)
        self.assertIsNotNone(faq.question_bn)