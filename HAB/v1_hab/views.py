# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from v1_hab.models import HouseholdAccountBook
# from v1_hab.serializers import HouseholdAccountBookSerializer
#
#
# # @api_view(['GET', 'POST'])
# # def list(request):
# #     if request.method == 'GET':
# #         householdAccountBook = HouseholdAccountBook.objects.all()
# #         serializer = HouseholdAccountBookSerializer(householdAccountBook, many=True)
# #         return Response(serializer.data)
# #
# #     elif request.method == 'POST':
# #         serializer = HouseholdAccountBookSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
#
# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
# @csrf_exempt
# def list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         householdAccountBook = HouseholdAccountBook.objects.all()
#         serializer = HouseholdAccountBookSerializer(householdAccountBook, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = HouseholdAccountBookSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#
#
#
# @csrf_exempt
# def detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         householdAccountBook = HouseholdAccountBook.objects.get(pk=pk)
#     except HouseholdAccountBook.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = HouseholdAccountBookSerializer(householdAccountBook)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = HouseholdAccountBookSerializer(householdAccountBook, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         householdAccountBook.delete()
#         return HttpResponse(status=204)
