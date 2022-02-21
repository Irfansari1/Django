from django.db.models import fields
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

# https://www.django-rest-framework.org/api-guide/views/#function-based-views

