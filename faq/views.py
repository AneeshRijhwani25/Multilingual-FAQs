from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faq_{lang}'
        
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()

        try:
            translated_data = [
                {
                    'id': faq.id,
                    'question': faq.get_translated_question(lang),
                    'answer': faq.get_translated_answer(lang),
                }
                for faq in faqs
            ]
        except Exception as e:
            return Response(
                {"error": "Translation failed", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        cache.set(cache_key, translated_data, timeout=60)

        return Response(translated_data)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.clear()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FAQDetailView(APIView):
    def get_object(self, pk):
        try:
            return FAQ.objects.get(pk=pk)
        except FAQ.DoesNotExist:
            return None

    def get(self, request, pk):
        faq = self.get_object(pk)
        if not faq:
            return Response({"error": "FAQ not found"}, status=status.HTTP_404_NOT_FOUND)

        lang = request.query_params.get('lang', 'en')

        try:
            translated_data = {
                'id': faq.id,
                'question': faq.get_translated_question(lang),
                'answer': faq.get_translated_answer(lang),
            }
        except Exception as e:
            return Response(
                {"error": "Translation failed", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(translated_data)

    def put(self, request, pk):
        faq = self.get_object(pk)
        if not faq:
            return Response({"error": "FAQ not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FAQSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.clear()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        faq = self.get_object(pk)
        if not faq:
            return Response({"error": "FAQ not found"}, status=status.HTTP_404_NOT_FOUND)

        faq.delete()
        cache.clear()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "FAQ deleted"})