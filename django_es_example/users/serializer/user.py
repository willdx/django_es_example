from rest_framework import serializers

from django_es_example.users.models import User


class UserElasticInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'address', 'birthday', 'description')
