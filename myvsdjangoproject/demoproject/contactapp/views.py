from django.shortcuts import render
from django.http import HttpResponse

def ContactPageView(request):
   browser=request.META['HTTP_USER_AGENT']
   if browser.find("chrome")!=-1:
      browser="chrome"
   elif browser.find("fireFox")!=-1:
      browser="firfox"
   else:
      browser="unknown browser"

   html=[]
   html.append("<html><head><title>Request Headers</title></head>")
   html.append("<body>")
   html.append("<h3>Following are Http header and their values </h3>")
   html.append("<table border='1'>")
   html.append("<tr><th>Header Name</th><th>Header valuse </th></tr>")
   for k,v in request.META.items():
      html.append(f"<tr><td>{k}</td><td>{v}</td></tr>")
   html.append("</table></body></html>")
   str=f"Your Browser is {browser}"
   str1=f"Current Web  page is{request.path}"
   return HttpResponse(html)
  # return HttpResponse(str+"     "+str1+"<h2>You Can Contact Us At scalive4u@gmail.com</h2>")  


# Create your views here.
