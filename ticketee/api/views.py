from rest_framework.response import Response
from rest_framework.decorators import api_view
from events.models import Event
from .serializers import EventSerializer

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()