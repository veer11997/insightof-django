from django.shortcuts import render
from django.http import HttpResponse
from formdemoapp1.models import Book

def addBooksView(request):
    book1=Book(book_id=101,book_name="Let Us C",book_price=250.0,subject="C",pub_date="2001-01-15")
    book1.save()
    book2=Book(book_id=102,book_name="Mastering Python",book_price=450.0,subject="Python",pub_date="2014-10-21")
    book2.save()
    book3=Book(book_id=103,book_name="Python Projects",book_price=350.0,subject="Python",pub_date="2016-04-19")
    book3.save()
    book4=Book(book_id=104,book_name="Let Us C++",book_price=350.0,subject="C++",pub_date="2006-04-19")
    book4.save()
    book5=Book(book_id=105,book_name="Mastering C",book_price=340.0,subject="C",pub_date="2014-12-22")
    book5.save() 
    book6=Book(book_id=106,book_name="Learning Java",book_price=650.0,subject="Java",pub_date="2018-11-19")
    book6.save()
    total_books=Book.objects.count()
    context={'count':total_books}
    return render(request,'formdemoapp1/addbook_result.html',context)
    
def searchFormView(request):
    return render(request,"formdemoapp1/search_form.html")

def searchView(request):
    subj=request.GET['subject']
    booklist=Book.objects.filter(subject__icontains=subj)
    context={'subject':subj,'books':booklist}
    return render(request,"formdemoapp1/search_result.html",context)

# Create your views here.
