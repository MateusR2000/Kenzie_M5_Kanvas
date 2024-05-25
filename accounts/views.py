from rest_framework.generics import CreateAPIView, ListCreateAPIView
from .models import Account
from .serializers import AccountSerialzier

class ListCreateAccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerialzier