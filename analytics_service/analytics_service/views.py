from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Analytics
from .serializers import AnalyticsSerializer

@api_view(['GET', 'POST'])
def analytics_list(request):
    if request.method == 'GET':
        analytics = Analytics.objects.all()
        serializer = AnalyticsSerializer(analytics, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = AnalyticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def analytics_detail(request, id):
    try:
        analytics = Analytics.objects.get(pk=id)
    except Analytics.DoesNotExist:
        return JsonResponse({'error': 'Analytics entry not found'}, status=404)

    if request.method == 'GET':
        serializer = AnalyticsSerializer(analytics)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = AnalyticsSerializer(analytics, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        analytics.delete()
        return JsonResponse(status=204)
