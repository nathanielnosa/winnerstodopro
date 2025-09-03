from rest_framework.views import APIView
from rest_framework import status,serializers
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from . models import Todo
from . serializers import TodoSerializer


# C - post
# R - get
# U - update
# D -  delete

# :::: CREATE & RETRIEVE ::::::
class TodoView(APIView):
    # create
    def post(self,request):
        try:
            serializers = TodoSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({"Message":"Todo created successfully"}, status=status.HTTP_201_CREATED)
            return Response({"error":serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # retrieve all
    def get(self,request):
        try:
            todos = Todo.objects.all()
            serializers = TodoSerializer(todos, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class TodoView(ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

class DetailTodoView(APIView):
    # retrieve single
    def get(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializer(todo)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # # update
    def put(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializer(todo, data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response({"Message":"Todo updated successfully"}, status=status.HTTP_200_OK)
            return Response({"error":serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    #  delete
    def delete(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({"Message":"Todo deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
