from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm
from RestApp.models import Restaurant
# Create your views here.
def home(request):
	return render(request,'app/home.html')

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')

def login(request):
	if request.method=="POST":
		Name = request.POST['Name']
		email = request.POST['email']
		password = request.POST['password']
	return render(request,'app/login.html')

def restlist(request):
	y = Restaurant.objects.all()
	if request.method == "POST":
		t = ReForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/rlist')
	t = ReForm()
	return render(request,'app/restaurantlist.html',{'q':t,'a':y})	

def rstup(request,m):
	k = Restaurant.objects.get(id=m)
	if request.method == "POST":
		e = ReForm(request.POST,instance=k)
		if e.is_valid():
			e.save()
			return redirect('/rst')
	e = ReForm()	
	return render(request,'app/restupdate.html',{'x':e})

def rstd(request,n):
	s = Restaurant.objects.get(id=n)
	if request.method == "POST":
		r = ReForm(request.POST,instance=s)
		if r.is_valid():
			r.save()
			return redirect('/rsd')
	r = ReForm()	
	return render(request,'app/restdelete.html',{'y':r})
