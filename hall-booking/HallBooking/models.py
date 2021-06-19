from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver


# Create your models here.

class User(AbstractUser):
	g = [('M','Male'),('F','Female'),('O','Others')]
	gender = models.CharField(max_length=10,choices=g)
	age = models.IntegerField(default=18)
	mobile_no = models.CharField(max_length=10)
	dob = models.DateField(null=True)
	pid_no=models.CharField(max_length=10) 
	address_line1=models.CharField(max_length=200)
	address_line2=models.CharField(max_length=200)
	city=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	country=models.CharField(max_length=30)
	im = models.ImageField(upload_to="Profile_pics/",default="avatar.png")
	r = [(0,'guest'),(1,'user'),(2,'manager')]
	role = models.IntegerField(choices=r,default=0)

# @receiver(post_save,sender=User)
# def CrtPfle(sender,instance,created,**kwargs):
# 	 if created: 
# 	 	Updf.objects.create(pr=instance)

class RoleRqst(models.Model):
	t=[(1,'user'),(2,'manager')]
	uname= models.CharField(max_length=30)
	roletype = models.PositiveIntegerField(choices=t)
	proof = models.ImageField(blank=True)
	is_checked=models.BooleanField(default=0)
	uid= models.OneToOneField(User,on_delete=models.CASCADE)

class AdHl(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=70)
	landmark = models.CharField(max_length=50)
	h = [('Marriage','Marriage'),('Seminar','Seminar'),('Event','Event')]
	halltype = models.CharField(choices=h,max_length=10,default="Event")
	a = [('AC','Ac'),('Non-AC','Non-AC')]
	aircond = models.CharField(choices=a,max_length=10,default="Non-AC")
	ACHall_Amount = models.CharField(max_length=30,default="25000 per hour")
	NonACHall_Amount = models.CharField(max_length=30,default="20000 per hour")
	occupancy = models.IntegerField(null=True)
	rooms = models.IntegerField(default=0)
	ACRoom_Cost = models.CharField(max_length=30,default="5000 per hour")
	NonACRoom_Cost = models.CharField(max_length=30,default="3000 per hour")
	area = models.CharField(max_length=20)
	advance = models.IntegerField(default=300)
	status = models.CharField(max_length=50,default="Available")
	fil = models.FileField(upload_to="Hall_Images/")
	add = models.ForeignKey(User,on_delete=models.CASCADE)


class Booking(models.Model):
	contact = models.IntegerField()
	your_address = models.CharField(max_length=70)
	occupation = models.CharField(max_length=30)
	male_birthc = models.FileField(upload_to="CertificateProofs/")
	female_birthc = models.FileField(upload_to="CertificateProofs/")
	rooms_needed = models.IntegerField(default=2)
	date = models.DateField(null=True)
	timings = models.CharField(max_length=30,default="AM to PM")
	noof_hours = models.IntegerField(default=3)
	cardno = models.CharField(default="XXXXXXXXXXXXX",max_length=13)
	cvv = models.CharField(default="XXX",max_length=3)
	m = [('1','January'),('2','February'),('3','March'),('4','April'),('5','May'),('6','June'),('7','July'),('8','August'),('9','September'),('10','October'),('11','November'),('12','December'),]
	y = [('1','2021'),('2','2022'),('3','2023'),('4','2024'),('5','2025'),('6','2026'),('7','2017'),('8','2028')]
	expmonth = models.IntegerField(choices=m,null=True)
	expyear = models.IntegerField(choices=y,null=True)
	amount = models.IntegerField(default=25000)

	c = models.ForeignKey(User,on_delete=models.CASCADE)



	
	
	





