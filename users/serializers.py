from rest_framework import serializers
from .models import User

# create instance of User (schema)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password'] 
        # respond do not contain password for security!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
        
    # hashing the password for security
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance