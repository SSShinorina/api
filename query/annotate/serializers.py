from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from annotate.models import Writer, Book


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        usr = self.authenticate(username=username, password=password)

        if not usr:
            raise AuthenticationFailed('Invalid User')
        attrs['user'] = usr
        return attrs


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    writer = serializers.PrimaryKeyRelatedField(queryset=Writer.objects.all())

    writer_detail = serializers.SerializerMethodField()

    def get_writer_detail(self,obj):
        serializer = WriterSerializer(obj.writer)
        return serializer.data


    class Meta:
        model = Book
        fields = "__all__"
