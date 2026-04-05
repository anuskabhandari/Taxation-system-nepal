from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_employee(request):
    return render(request, 'add_employee.html')

def update_employee(request):
    return render(request, 'update_employee.html')

def view_report(request):
    return render(request, 'report.html')