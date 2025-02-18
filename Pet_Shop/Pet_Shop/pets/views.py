from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view

from .models import Items, Users, Orders, ItemsOrders
from .permissions import IsThisUser, IsOwner
from .serializers import (
    ItemsSerializer,
    UsersSerializer,
    OrdersSerializer,
    AllOrdersOfUser,
)


class ItemView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def get(self, requset, *args, **kwargs):
        return self.list(requset, *args, **kwargs)

    def post(self, requset, *args, **kwargs):
        return self.create(requset, *args, **kwargs)


class ItemDetail(generics.RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer



class UsersList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAdminUser]


class UserListRegister(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated, IsThisUser]


class AllOrdersList(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAdminUser]


class OrdersList(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user, status="Pending")


class OrderDetail(generics.RetrieveDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class OrderUpdate(generics.RetrieveUpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAdminUser]

    #TODO: It is a bug, because if admin updates order it will asign it to him.
    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)


class AllOrdersOfUser(generics.ListAPIView):
    serializer_class = AllOrdersOfUser
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Orders.objects.filter(user_id=self.request.user)


class CustomAPIToken(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


@api_view(["POST"])
def check_user_email(request):
    email = request.data["email"]
    user = Users.objects.filter(email=email)

    if user.exists():
        return Response({"User with this email already exists!"})
    return Response({"Email is good to go"})
