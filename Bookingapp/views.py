from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Bookingapp.serializers import BookingSerializer
from Bookingapp.models import Booking

@csrf_exempt
def bookingApi(request,id=0):
    if request.method=='GET':
        booking = Booking.objects.all()
        booking_serializer=BookingSerializer(booking,many=True)
        return JsonResponse(booking_serializer.data,safe=False)
    elif request.method=='POST':
        booking_data=JSONParser().parse(request)
        booking_serializer=BookingSerializer(data=booking_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        booking_data=JSONParser().parse(request)
        booking=Booking.objects.get(id=id)
        booking_serializer=BookingSerializer(booking,data=booking_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        booking=Booking.objects.get(id=id)
        booking.delete()
        return JsonResponse("Deleted Successfully",safe=False)