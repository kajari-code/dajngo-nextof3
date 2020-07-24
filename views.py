from django.shortcuts import render
from insert.models import Customer

# Create your views here.
def displaypage(request):
    obj=Customer.objects.all()
    return render(request,"display.html",{'details':obj})