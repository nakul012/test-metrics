from .models import Metrics
from .serializers import (
    MetricsSerializer,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


class MetricsListView(APIView):
    serializer_class = MetricsSerializer
    queryset = Metrics.objects.all()

    def get(self, request, *args, **kwargs):
        params = request.query_params
        start = params.get("start", None)
        end = params.get("end", None)
        if not start and end:
            return Response({"error": "No start and end date provided"}, status=400)
        queryset = Metrics.objects.filter(
            Q(time__gte=start) & Q(time__lte=end)
        )
        return Response(MetricsSerializer(queryset, many=True).data, status=200)

    def post(self, request):
        data = request.data
        serializer = MetricsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
