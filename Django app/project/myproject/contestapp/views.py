from django.shortcuts import render
import datetime
from contestapp.models import Contest

def homepageview(request):
    return render(request,'templateapp/home.html')
   # curr_date=datetime.datetime.now()
    #curr_date_str=curr_date.strftime("%d-%b-%Y")
    #return render(request,"templateapp/data.html",{'today':curr_date_str})
def showdateview(request):
    curr_date=datetime.datetime.now()
    curr_date_str=curr_date.strftime("%d-%b-%Y")
    return render(request,"templateapp/data.html",{'today':curr_date_str})

def addcontestview(request):
	contest1=Contest(contest_name="google",book_name="Hackerearth",starting="2019-01-10",ending="2019-02-21")
	contest1.save()
	contest2=Contest(contest_name="facebook",book_name="Interviewbit",starting="2019-01-11",ending="2019-02-22")
	contest2.save()
	contest3=Contest(contest_name="twiter",book_name="codchef",starting="2019-01-12",ending="2019-03-23")
	contest3.save()
	total_contest=Contest.objects.count()
	context={'count':total_contest}
	return render(request,"templateapp/insert.html",context)

def getcontestview(request):
	all_record=Contest.objects.all()
	my_list=[]
	for b in all_record:
		my_list.append(b)
	context={'my_list':my_list}
	return render(request,"templateapp/home.html",context)



# Create your views here.
