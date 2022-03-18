from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from super_types.models import Super_Type

@api_view(['GET', 'POST'])
def supers_list(request):
    supers = Super.objects.all()
    types_super = Super_Type.objects.all()

    custom_response_dictionary = {}

    if request.method == 'GET':
        type_of_super = request.query_params.get('type')
        blank = request.query_params.get('')

        if type_of_super:
            supers = supers.filter(super_type__type=type_of_super)

        else:
            for type_super in types_super:
                super_type_id = Super.objects.filter(super_type=type_super.id)
                super_serializer = SuperSerializer(super_type_id, many=True)
                custom_response_dictionary[type_super.type] = {
                    "Supers": super_serializer.data
                }
    
            return Response(custom_response_dictionary)

        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)

    if request.method == "GET":
        serializer = SuperSerializer(super)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


