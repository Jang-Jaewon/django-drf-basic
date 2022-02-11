from django.http import JsonResponse

from .models import Employee

def employeeView(request):
    data = Employee.objects.all()
    response = {'Employees' : list(data.values('name', 'sal'))}
    return JsonResponse(response)
