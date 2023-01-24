from rest_framework import generics
from quotes.api.serializers import QuoteSerializer
from quotes.models import Quote
from quotes.api.permissions import IsAdminUserOrReadonly


class QuoteListViewCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadonly]


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadonly]
