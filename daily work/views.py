from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("Hi Good Evening to All...")

def htmltag(y):
	return HttpResponse("<h2>Hi Weclome to APSSDC Programs</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi Weclome <span styles'color:green'> {}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;backgroung-color:green'>Hi User <span style='color:yellow'> {}</span> and your age is: <span style='color.red'>{}<span></h3>".format(un,ag))

def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('Hi Weclome {}')</script><h3>Hi Welcome {} and your age is: {} and your id is: {} </h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internalJS(request):
	return render(request,'html/internalJS.html')

def myform(req):
	if req.method=="POST":
		#print(req.POST)
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get('email')
		#print(uname,rollno,email)
		data = {'username':uname,'rno':'rollno','emailId':email}
		return render(req,'html/display.html',data)
	return render(req,'html/myform.html')

def register(req):
	if req.method=="POST":
		fname = req.POST['fname']
		lname = req.POST['lname']
		email = req.POST.get('email')
		phno = req.POST['phno']
		gender = req.POST['gender']
		address = req.POST['address']
		Languages = req.POST.get('Languages')
		data = {'firstname':fname,'lastname':lname,'email':email,'phoneno':phno,'gender':gender,'address':address,'Languages':Languages}
		return render(req,'html/show.html',data)
	return render(req,'html/register.html')	

def bootstrapfun(request):
	return render(request,'html/sampleboot.html')
