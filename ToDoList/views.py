from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import models
# Create your views here.

def todoList(request):
    TaskList = models.Task.objects.order_by('status', 'id').all().values()
     
    # print(list(TaskList))
    return render(request,"home.html",{'TaskList': list(TaskList)})

def addList(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        # print(text)
        if text:
            models.Task.objects.create(list=text)
            return JsonResponse({'message': 'Task added successfully!'})
            

        return JsonResponse({'error': 'Text is required!'}, status=400)
    return render(request,"home.html")

def deleteTask(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = models.Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully!'})
    return render(request,"home.html")

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
        task = models.Task.objects.get(id=task_id)
        task.status = status
        task.save()
        return redirect('ToDoList:home')
        # print(task)
        # task = get_object_or_404(Task, id=task_id)
    return render(request,"home.html")