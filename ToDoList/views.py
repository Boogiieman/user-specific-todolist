from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from . import models
# Create your views here.

@login_required
def todoList(request):
    TaskList = models.Task.objects.filter(user=request.user).order_by('status', 'id').values()
     
    # print(list(TaskList))
    return render(request,"home.html",{'TaskList': list(TaskList)})

@login_required
def addList(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        # print(text)
        if text:
            models.Task.objects.create(user = request.user, list=text)
            return JsonResponse({'message': 'Task added successfully!'})
            

        return JsonResponse({'error': 'Text is required!'}, status=400)
    return render(request,"home.html")

@login_required
def deleteTask(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = models.Task.objects.get(id=task_id, user=request.user)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully!'})
    return render(request,"home.html")

@login_required
def update_task_status(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        status = request.POST.get('status')
        # print(status,task_id)
        if status:
            status= True
        else:
            status= False
        # print(status)
        task = models.Task.objects.get(id=task_id, user=request.user)
        task.status = status
        task.save()
        return redirect('ToDoList:home')
        # print(task)
        # task = get_object_or_404(Task, id=task_id)
    return render(request,"home.html")