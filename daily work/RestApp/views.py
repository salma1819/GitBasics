from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm,ItemsForm,UsgForm
from RestApp.models import Restaurant,Itemlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	w = Restaurant.objects.filter(uid_id=request.user.id)
	return render(request,'app/home.html',{'c':w})

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')

#def login(request):
#	return render(request,'app/login.html')
@login_required
def restlist(request):
	y = Restaurant.objects.filter(uid_id=request.user.id)
	if request.method == "POST":
		t = ReForm(request.POST,request.FILES)
		if t.is_valid():
			c = t.save(commit=False)
			c.uid_id = request.user.id
			c.save()
			messages.success(request,"Restaurant Added Successfully")
			return redirect('/rlist')
	t = ReForm()
	return render(request,'app/restaurantlist.html',{'q':t,'a':y})	

@login_required
def rstup(request,m):
	k = Restaurant.objects.get(id=m)
	if request.method == "POST":
		e = ReForm(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Restaurant Updated Successfully".format(k.Rname))
			return redirect('/rlist')
	e = ReForm()	
	return render(request,'app/restupdate.html',{'x':e})

def rstdl(request,n):
	s = Restaurant.objects.get(id=n)
	if request.method == "POST":
		messages.info(request,"{} Restaurant Deleted Successfully".format(s.Rname))
		s.delete()
		return redirect('/rlist')	
	return render(request,'app/restdelete.html',{'y':s})

def rstvw(request,a):
	v = Restaurant.objects.get(id=a)
	return render(request,'app/restview.html',{'z':v})


def itlist(request):
	m = Itemlist.objects.all()
	if request.method == "POST":
		k = ItemsForm(request.POST,request.FILES)
		if k.is_valid():
			n = k.save(commit=False)
			messages.success(request,'{} Item is Added Successfully'.format(n.iname))
			n.save()
			return redirect('/ilist')
	k = ItemsForm()		
	return render(request,'app/itmlist.html',{'r':k,'s':m})

def usrreg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d = UsgForm()		
	return render(request,'app/usrregister.html',{'t':d})

def itup(request,s):
	k = Itemlist.objects.get(id=s)
	if request.method == "POST":
		e = ItemsForm(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Itemlist Updated Successfully".format(k.iname))
			return redirect('/ilist')
	e = ItemsForm()	
	return render(request,'app/itemupdate.html',{'x':e})

def itdl(request,p):
	s = Itemlist.objects.get(id=p)
	if request.method == "POST":
		messages.info(request,"{} Itemlist Deleted Successfully".format(s.iname))
		s.delete()
		return redirect('/rlist')	
	return render(request,'app/itemdelete.html',{'y':s})

def itvw(request,b):
	v = Itemlist.objects.get(id=b)
	return render(request,'app/itemview.html',{'z':v})
