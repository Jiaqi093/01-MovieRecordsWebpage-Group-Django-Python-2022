from rest_framework import viewsets
from rest_framework.response import Response
from Capstone_Project2 import models
from .serializers import AccountSerializer,ItemSerializer,RecordSerializer, GenreSerializer, FriendSerializer, FriendRequestSerializer
from rest_framework.decorators import action
import re
from rest_framework.parsers import MultiPartParser, FormParser

class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = AccountSerializer

    #get all accounts which has not deleted
    @action(detail=False, methods=['get'])
    def get_not_delete(self, request):
        queryset = models.Account.objects.filter(is_delete=False)
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    # get account (id) from the corresponding user id
    @action(detail=True, methods=['get'])
    def get_account(self, request, pk=None):
        user_id = str(request)
        user_id = re.findall(r'(\d+)', user_id)[0]
        queryset = models.Account.objects.filter(user_id=user_id)
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    # get all records in one account through account id, needs modify!!!!!!!!!!!!!!!!
    @action(detail=True, methods=['get'])
    def get_account_record(self,request,pk=None):
        account_id = str(request)
        account_id = re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',account_id)[0]
        queryset = models.Records.objects.filter(account_id=account_id)
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data)



class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = ItemSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genres.objects.all()
    serializer_class = GenreSerializer


class RecordViewSet(viewsets.ModelViewSet):

    queryset = models.Records.objects.all()
    serializer_class = RecordSerializer

    #get one specific record through record id
    @action(detail=True, methods=['get'])
    def get_one_record(self, request, pk=None):
        record_id = str(request)
        record_id = re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', record_id)[0]
        queryset = models.Records.objects.filter(records_id=record_id)
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_all_records(self, request):
        queryset = models.Records.objects.all()
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data)


class FriendsViewSet(viewsets.ModelViewSet):
    queryset = models.Friends.objects.all()
    serializer_class = FriendSerializer

class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = models.FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
