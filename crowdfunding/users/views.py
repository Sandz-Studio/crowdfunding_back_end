from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsUserOrReadOnly

from rest_framework.permissions import IsAuthenticated

class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    # A user cannot make another user but not sure how to fix.
    # POST Method to display error (403 Forbidden)?
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly
    ]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    # Update User Information
    def put(self, request, pk):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)  # Check permissions before updating

        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SessionUserDetailView(generics.RetrieveUpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     lookup_field = 'id'
#     serializer_class = CustomUserDetail

#     def get_object(self):
#         return self.request.user

#     # https://www.cdrf.co/3.13/rest_framework.generics/RetrieveUpdateDestroyAPIView.html

# Attempted to fix login issue - permission to delete project when owner and logged in.   
# class SessionUserDetailView(APIView):

#     permission_classes = [
#         permissions.IsAuthenticated]
    
#     def get_object(self):
#         try:
#             return self.request.user
#         except CustomUser.DoesNotExist:
#             raise Http404
#     def get(self, request):
#         print(request)
#         user = self.get_object()
#         serializer = CustomUserSerializer(user)
#         return Response(serializer.data)