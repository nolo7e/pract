from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Borrowing
from .serializers import BorrowingSerializer

@api_view(['GET', 'POST'])
def borrowing_list(request):
    if request.method == 'GET':
        borrowings = Borrowing.objects.all()
        serializer = BorrowingSerializer(borrowings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = BorrowingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def borrowing_detail(request, id):
    try:
        borrowing = Borrowing.objects.get(pk=id)
    except Borrowing.DoesNotExist:
        return JsonResponse({'error': 'Borrowing not found'}, status=404)

    if request.method == 'GET':
        serializer = BorrowingSerializer(borrowing)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = BorrowingSerializer(borrowing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        borrowing.delete()
        return JsonResponse(status=204)
