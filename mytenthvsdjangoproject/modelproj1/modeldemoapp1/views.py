from django.shortcuts import render
from modeldemoapp1.models import Book
def allBooksView(request):
    b1=Book(book_Id=101,book_name="let Us C",bookprice=250.0,subject="c",pub_date='2001-01-15')
    b2=Book(book_Id=102,book_name="mastering c",bookprice=350.0,subject="c",pub_date='2014-10-21')
    b3=Book(book_Id=103,book_name="python projects",bookprice=150.0,subject="python",pub_date='2018-12-19')
    b1.save()
    b2.save()
    b3.save()
    total_rec=Book.objects.count()
    context={'count':total_rec}
    return render(request,'modeldemoapp1/result.html',context)

def showBooksView(request):
	all_books=Book.objects.all()
	book_list=[]
	for b in all_books:
		book_list.append(b)
	context={'book_list':book_list}
	return render(request,"modeldemoapp1/showbooks.html",context)





# Create your views here.
