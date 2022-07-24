    # class RegisterAPI(generics.GenericAPIView):


#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#
#     def post(self, request, *args, **kwargs):
#         import pdb;
#         pdb.set_trace()
#         given_data = request.data
#         # instance = self.get_object()
#         get_user, created = self.queryset.get_or_create(email=given_data['email'],
#                                                         username=given_data['username'],
#                                                         password=given_data['password'])
#
#         if created:
#             serializer = self.get_serializer(get_user, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             if serializer.is_valid():
#                 password = serializer.validated_data.get('password')
#                 serializer.validated_data['password'] = make_password(password)
#                 new_user = serializer.save()
#                 if new_user:
#                     return Response({
#                         'message': 'user successfully register',
#                         "data": serializer.data
#                     }, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             import pdb; pdb.set_trace()
#             get_user.is_active = True
#             get_user.save()
#             serializer = self.serializer_class(get_user, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({
#                 'message': 'user already exist',
#                 "data": serializer.data
#             }, status=status.HTTP_201_CREATED)
#
#             # serializer = self.serializer_class(get_user, data=request.data, partial=True)
#             # import pdb; pdb.set_trace()
#             # serializer.is_valid(raise_exception=True)
#             # serializer.save()
#             # return Response({
#             #     'message': 'user successfully register',
#             #     'data': serializer.data
#             # }, status=status.HTTP_201_CREATED)
#     # def post(self, request, *args, **kwargs):
#     #     serializer = self.get_serializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     user = serializer.save()
#     #     return Response({
#     #         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#     #         "token": AuthToken.objects.create(user)[1]
#     #     })