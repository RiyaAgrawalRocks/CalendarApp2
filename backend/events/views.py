from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Event, User
from .serializers import EventSerializer, UserSerializer

# Show all events
@api_view(['GET'])
def show_all(request):
    try:
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

# Create a new event
@api_view(['POST'])
def create(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Edit an existing event
@api_view(['GET','PUT', 'PATCH'])
def edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    serializer = EventSerializer(event, data=request.data, partial=True)  # Partial=True allows updating some fields
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete an event
@api_view(['DELETE'])
def delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return Response({"message": "Event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Show a specific event
@api_view(['GET'])
def show_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    serializer = EventSerializer(event)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Show the user who created the event (assuming `organiser` is the user's name)
@api_view(['GET'])
def show_user(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = get_object_or_404(User, name=event.posted_by)  # Assuming `organiser` stores the user's name
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def callback(request):
    
    return







