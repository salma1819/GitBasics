from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	age = models.IntegerField(default=20)
	mobilenumber = models.CharField(max_length=10,null=True)
	uimg = models.ImageField(upload_to='Profilepics/',default='logo.jpg')
	t = [(1,'Guest'),(2,'Manager'),(3,'User')]
	role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
	f = [(2,'Manager'),(3,'User')]
	rltype = models.IntegerField(choices=f)
	pfl = models.ImageField(upload_to='Rolereqpics/',default='logo.jpg')
	is_checked = models.BooleanField(default=False)
	uname = models.CharField(max_length=50)
	ud = models.OneToOneField(User,on_delete=models.CASCADE)

class Restaurant(models.Model):
	Rname = models.CharField(max_length=30)
	Nitems = models.IntegerField()
	timings = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	rsimg = models.ImageField(upload_to='Restaurantimages/',default="logo.jpg")
	uid = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.Rname




class Itemlist(models.Model):
	y = [('NV','Non-Veg'),('VG','Veg'),('Df','Select Item Type')]
	p =[('AV','Available'),('NA','Not Available'),('Sl','Select Availability')]
	iname = models.CharField(max_length=50)
	icategory = models.CharField(choices=y,default="DF",max_length=12)
	price = models.DecimalField(decimal_places=3,max_digits=8)
	iimage = models.ImageField(upload_to='Itemimages/',default='item1.jpg')
	itavailability = models.CharField(choices=p,default="Sl",max_length=20)
	rsimg = models.ImageField(upload_to='Itemimages/',default="item1.jpg")
	rsid = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

