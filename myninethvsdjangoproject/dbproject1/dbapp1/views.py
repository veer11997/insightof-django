from django.shortcuts import render
import cx_Oracle
def showBooksView(request):
    bookrecords=[]
    errormsg=""
    context={}
    conn=None
    try:
        conn=cx_Oracle.connect("system/abc@127.0.0.1/xe")   
        cur=conn.cursor()
        cur.execute("select bookname,bookprice from all_books")
        booklist=cur.fetchall()
        for name,price in booklist:
            bookrecords.append({'bookname':name,'bookprice':price})
        context['records']=bookrecords
    except:
        print("exception occured")
        errormsg="some problem in Db"
        context['error']=errormsg
        

    finally:
        if cur is not None:
            cur.close()

        if conn is not None:
            conn.close

        return render(request,'dbapp1/showbooks.html',context)                    

# Create your views here.
#mapping key value pair