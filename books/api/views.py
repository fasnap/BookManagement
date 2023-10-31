from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer
from django.http import Http404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

# To create a new book and list all books
class BookList(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
# To update,delete and retrieve a specific book
class BookDetail(APIView):
    
    def get(self,request,pk):
        try:
            book=Book.objects.get(pk=pk)
        except:
            return Response({"error":"Book not found"}, status=status.HTTP_204_NO_CONTENT)
        serializer=BookSerializer(book)
        return Response(serializer.data)
    
    def put(self,request,pk):
        book=Book.objects.get(pk=pk)
        serializer=BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        book=Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TokenObtainAndRetrieveView(APIView):
    def post(self, request):
        # Obtain the credentials from the request
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Check if the user already exists
        user = User.objects.filter(username=username).first()
        
        if user is None:
            user = User.objects.create_user(username=username, password=password)
        elif not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # generate jwt token for user
        refresh = RefreshToken.for_user(user)
        token_data = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

        return Response(token_data, status=status.HTTP_200_OK)