from django.shortcuts import render

emp_recs=[{'EmpNo':101,'Ename':'Amit','salary':50000.0,'HireDate':'August 27,2018'},
{'EmpNo':102,'Ename':'Sumit','salary':45000.0,'HireDate':'November 21,2018'}]


def  homePageView(request):
    context={'emplist':emp_recs}
    return render(request,'templateapp/index.html',context)
# Create your views here.


# Create your views here.
