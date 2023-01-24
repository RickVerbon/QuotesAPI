from quotes.api.views import QuoteListViewCreateAPIView, QuoteDetailAPIView
from django.urls import path


urlpatterns = [
    path("quotes/", QuoteListViewCreateAPIView.as_view(), name="quotes-list"),
    path("quotes/<int:pk>", QuoteDetailAPIView.as_view(), name="quotes-detail")
]
