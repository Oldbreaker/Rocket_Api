from rest_framework import serializers
from .models import MyUser
"""
Serializador utilizado en nuestras vistas
al estar usando el modeleo User heredado en nuestro modelo MyUser determinamos los
fields que son importantes para nuestra apliacación.
"""


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',)
        extra_kwargs = {'username': {'required': True, 'allow_blank': False},
                        'password': {'required': True, 'allow_blank': False},
                        'email': {'required': True, 'allow_blank': False},
                        'first_name': {'required': True, 'allow_blank': False},
                        'last_name': {'required': True, 'allow_blank': False}, }

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.set_password(validated_data['password'])
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.save()
        return instance
