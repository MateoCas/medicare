from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from home_care.models import Person
from home_care.serializers.person_serializer import PersonSerializer

# Routes for Person resource
"""
home-care/api/person/  - GET
home-care/api/person/{id} - GET
home-care/api/person/ - POST
home-care/api/person/{id} UPDATE
home-care/api/person/{id} DELETE
"""


class PersonApiView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        persons = Person.objects.all()
        persons_serializer = PersonSerializer(persons, many=True)
        return Response(persons_serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):
        person_data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'adress_personal': request.data.get('adress_personal'),
            'phone_number': request.data.get('phone_number'),
            'identification': request.data.get('identification'),
            'active': True
        }

        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            response = {
                'code': status.HTTP_201_CREATED,
                'message': 'Person was added successfully',
                'person': person_serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)

        response = {
            'code': status.HTTP_400_BAD_REQUEST,
            'person': person_serializer.data,
            'message': "La persona no fue agregada, por favor verificar los datos enviados",
            'technical_error': person_serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

