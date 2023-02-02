from rest_framework import serializers
from Capstone_Project2 import models
from enumchoicefield import EnumChoiceField
from Capstone_Project2.models import privacy, item_type, gender
from rest_framework import serializers

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

# serializer converts models to a json type
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'

    gender = EnumChoiceField(enum_class=gender)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'

    item_type = EnumChoiceField(enum_class=item_type)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genres
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    thumbnail = Base64ImageField(max_length=None, use_url=True)
    class Meta:
        model = models.Records
        fields = '__all__'

    privacy = EnumChoiceField(enum_class=privacy)


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friends
        fields = '__all__'


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendRequest
        fields = '__all__'