from django.shortcuts import render


def homePage(request):
    return render(request,'templateapp/index.html')
def  homePageView(request):
     djtext = request.POST.get('text', 'default')
     context={'task':djtext}
     return render(request,'templateapp/result.html',context)
# Create your views here.


# Create your views here.
