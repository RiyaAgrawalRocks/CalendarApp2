from rest_framework import serializers
from .models import *

class BodyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyCategory
        fields = '__all__'


class BodySerializer(serializers.ModelSerializer):
    category = BodyCategorySerializer(read_only=True)  # Nested serializer for category
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=BodyCategory.objects.all(), source='category', write_only=True
    )  # Allows assigning category by ID

    class Meta:
        model = Body
        fields = ['id', 'name', 'category', 'category_id', 'contact_email']


class UserSerializer(serializers.ModelSerializer):
    body = BodySerializer(read_only=True)  # Nested serializer for body
    body_id = serializers.PrimaryKeyRelatedField(
        queryset=Body.objects.all(), source='body', write_only=True
    )  # Allows assigning body by ID

    class Meta:
        model = User
        fields = ['id', 'name', 'roll_number', 'department', 'degree', 'body', 'body_id']


class EventSerializer(serializers.ModelSerializer):
    organiser = BodySerializer(read_only=True)  # Nested serializer for organiser
    organiser_id = serializers.PrimaryKeyRelatedField(
        queryset=Body.objects.all(), source='organiser', write_only=True
    )  # Allows assigning organiser by ID

    posted_by = UserSerializer(read_only=True)  # Nested serializer for posted_by
    posted_by_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='posted_by', write_only=True
    )  # Allows assigning posted_by by ID

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'organiser', 'organiser_id', 'posted_by',
            'posted_by_id', 'venue', 'start_time', 'end_time', 'recurrence', 'recur_start', 'recur_end'
        ]
