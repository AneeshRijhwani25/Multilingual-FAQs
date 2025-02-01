from django.urls import path
from django.contrib import admin
from faq.views import FAQListView, FAQDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/faqs/', FAQListView.as_view(), name='faq-list'),
    path('api/faqs/<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)