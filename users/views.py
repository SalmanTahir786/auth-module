from django.contrib.auth import login
from django.contrib.auth.models import User
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response

from .serializers import UserSerializer, RegisterSerializer


class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    allowed_methods = ('POST',)

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        try:
            check_is_active = User.objects.get(email=email)
            if not check_is_active.is_active:
                check_is_active.is_active = True
                check_is_active.save()
                data = {'username': check_is_active.username,
                        'email': check_is_active.email}
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {'username': check_is_active.username,
                        'email': check_is_active.email}
                return Response(data, status=status.HTTP_200_OK)
        except:
            serializer = RegisterSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                account = serializer.save()
                data['email'] = account.email
                data['username'] = account.username
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                data = serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        filter_obj = User.objects.filter(username=request.data['username']).get()
        if filter_obj.is_active is True:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)
            return super(LoginAPI, self).post(request, format=None)
        else:
            return Response({
                "error": "Inactive user not able to login",
            })


class UpdateIsActiveAPIView(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.queryset.filter(id=self.kwargs['pk']).first()
        instance.is_active = False
        instance.save()
        return Response({"message": "user successfully deleted"},
                        status=status.HTTP_200_OK)
