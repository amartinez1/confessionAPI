from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRoot(APIView):
    def get(self, request):
        return Response({
            'confessions': reverse('confessions-list', request=request),
            'confession': reverse('confession-detail', request=request),
        })
