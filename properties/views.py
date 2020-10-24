from django.http import JsonResponse, HttpResponse
from .models import Property

# GET ALL PROPERTIES.
def getPropertyList(request):
    try:
        props = list(Property.objects.values().order_by("priority"))
        return JsonResponse(props, safe=False)
    except:
        return JsonResponse({"Error": "Server Error"}, status=500)


def getProperty(request, pk):
    try:
        props = list(Property.objects.values().filter(property_id=pk))
        return JsonResponse(props, safe=False)
    except:
        return JsonResponse({"Error": "Server Error"}, status=500)
