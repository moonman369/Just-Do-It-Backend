from django.http import JsonResponse
from .models import Task, User
from .serializers import TaskSerializer


def tasks_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse({"tasks": serializer.data}, safe=False)

def get_task_by_user(request):
    user_id = request.GET.get("user")
    tasks = Task.objects.filter(user=user_id)
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse({"tasks": serializer.data}, safe=False)