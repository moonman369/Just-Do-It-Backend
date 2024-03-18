from django.http import JsonResponse
from .models import Task, User
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import uuid_task


@api_view(['GET'])
def get_tasks_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse({"count": len(serializer.data), "tasks": serializer.data}, safe=False)

@api_view(['GET'])
def get_tasks_by_user(request, **kwargs):
    # user_id = request.GET.get("user")
    user_id = kwargs.get("user_id")
    # print(request.GET)
    try:
        tasks = Task.objects.filter(user=user_id)
    except Task.DoesNotExist:
        JsonResponse(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse({"count": len(serializer.data), "tasks": serializer.data}, safe=False)

@api_view(['GET'])
def get_task_detail(request, **kwargs):
    task_id = kwargs.get("task_id")
    print(task_id)
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return JsonResponse({"message": "Resource not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['POST', 'PUT', 'DELETE'])
def create_or_modify_task(request, **kwargs):
    if request.method == "POST":
        # print(request.headers)
        request.data.update({"user": kwargs.get("id")})
        request.data.update({"task_id": uuid_task()})
        request.data.update({"status": "Pending"})
        if request.data.get("creation_time"): request.data.pop("creation_time")
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == "PUT":
        operation = request.headers.get("operation")
        task_id = kwargs.get("id")
        print(operation)
        print(request.data)
        if(operation.lower() == "updatedeadline"):
            task = Task.objects.get(pk=task_id)
            if request.data.get("deadline") == None:
                return Response({"message": "Missing field `deadline`"}, status=status.HTTP_400_BAD_REQUEST)
            task.deadline = request.data["deadline"]
            task.save()
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        elif(operation.lower() == "updatedescription"):
            task = Task.objects.get(pk=task_id)
            if request.data.get("description") == None:
                return Response({"message": "Missing field `description`"},status=status.HTTP_400_BAD_REQUEST)
            task.description = request.data["description"]
            task.save()
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        elif(operation.lower() == "updatestatus"):
            task = Task.objects.get(pk=task_id)
            if request.data.get("status") == None:
                return Response({"message": "Missing field `status`"},status=status.HTTP_400_BAD_REQUEST)
            if request.data.get("status") not in ["Pending", "Completed", "Archived"]:
                return Response({"message": "Incorrect value for field `status`"},status=status.HTTP_400_BAD_REQUEST)
            task.status = request.data["status"]
            task.save()
            print(task.__dict__)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
            # return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("ELSE check")
            return Response({"message": "Invalid operation in header"}, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        task_id = kwargs.get("id")
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


