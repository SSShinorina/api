from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from annotate.models import Writer, Book
from annotate.serializers import LoginSerializer, WriterSerializer, BookSerializer


class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            usr = serializer.validated_data['user']
            tok, created = Token.objects.get_or_create(user=usr)
            return Response({'token': tok.key}, status=status.HTTP_200_OK)


class Hello(APIView):
    def get(self, request):
        return Response({'message': 'Hello World'}, status=status.HTTP_200_OK)

    def post(self, request):
        pass


class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
