from django.shortcuts import render
import datetime
# Create your views here.
def Template(request):
    date=datetime.datetime.now()
    name="NareshIT"
    dic={'date':date,'name':name}
    return render(request,'MyApp/Welcome.html',context=dic)
