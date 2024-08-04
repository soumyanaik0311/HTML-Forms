from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

\

def insert_dept(request):

    if request.method == 'POST':
        deptno=request.POST['deptno']
        dname=request.POST['dname']
        dloc=request.POST['dloc']

        DO=Dept.objects.get_or_create(deptno=deptno,dname=dname,dloc=dloc)[0]
        DO.save()
        return HttpResponse('Department table is created...')
    return render(request,'insert_dept.html')


def insert_emp(request):
    LDO=Dept.objects.all()
    LEO=Emp.objects.all()
    d={'LDO':LDO,'LEO':LEO}

    if request.method == 'POST':
        empno=request.POST['empno']
        ename=request.POST['ename']
        job=request.POST['job']
        sal=request.POST['sal']
        comm=request.POST['comm'] 
        
        hiredate=request.POST['hiredate']
        dn=request.POST['deptno']
        mgr=request.POST['mgr']

        DO=Dept.objects.get(deptno=dn)
        MO=Emp.objects.get(empno=mgr) if mgr else None
        comm = comm if comm else None

        EO=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,sal=sal,comm=comm,hiredate=hiredate,deptno=DO,mgr=MO)[0]
        EO.save()
        return HttpResponse('Employee table is created...')


    return render(request,'insert_emp.html',d)

def retrieve_emp(request):
    LEO=Emp.objects.all()
    d={'LEO':LEO}
    return render(request,'retrieve_emp.html',d)