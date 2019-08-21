from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import refridgerator_display_system,history

class get_all_user(APIView):
    def get(self,request):
        try:
            get_id = self.request.query_params.get('id')
            thisID = refridgerator_display_system.objects.get(id=get_id)
        except:
            print("There is Invalid ID trying to access : "+str(get_id))
            return Response({"id": get_id,"OK": False})
        else:
            history.objects.create(ref_id=thisID)
            print("making History")
            return Response({"id": get_id,"OK": True})