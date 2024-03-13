from django.http import JsonResponse
from .models import Task, User
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        JsonResponse(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['POST', 'PUT', 'DELETE'])
def create_or_modify_task(request, **kwargs):
    if request.method == "POST":
        print(type(request.data))
        request.data.update({"user": kwargs.get("user_id")})
        if request.data.get("task_id"): request.data.pop("task_id")
        if request.data.get("creation_time"): request.data.pop("creation_time")
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # elif request.method == "PUT":
