from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from rest_framework.response import Response
from .serializers import PersonSerializer

# Create your views here.
@api_view(['GET'])
def get_person_dni(request, person_id):
    try:
        person = Person.objects.get( id = person_id )
    except Person.DoesNotExist:
        return Response({"message": "La persona no existe"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(person)
    return Response(serializer.data)