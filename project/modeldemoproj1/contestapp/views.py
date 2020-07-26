from django.shortcuts import render
from contestapp.models import Contest

def addcontestview(request):
	contest1=Contest(conest_name="google",contest_type="coding",contest_site="Hackerearth",starting="2019-01-10",ending="2019-02-21")
	contest1.save()
	contest2=Contest(conest_name="facebook",contest_type="coding",contest_site="Interviewbit",starting="2019-01-11",ending="2019-02-22")
	contest2.save()
	contest3=Contest(conest_name="twiter",contest_type="coding",contest_site="codchef",starting="2019-01-12",ending="2019-03-23")
	contest3.save()
	total_contest=Contest.objects.count()
	context={'count':total_contest}
	return render(request,"templateapp/result.html",context)

def getcontestview(request):
	all_record=Contest.objects.all()
	my_list=[]
	for b in all_record:
		my_list.append(b)
	context={'my_list':my_list}
	return render(request,"templateapp/index.html",context)


# Create your views here.
