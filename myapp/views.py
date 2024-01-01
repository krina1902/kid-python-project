from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def classes(request):
	return render(request,'class.html')

def team(request):
	return render(request,'team.html')

def gallery(request):
	return render(request,'gallery.html')

def blogdetail(request):
	return render(request,'blogdetail.html')

def bloggrid(request):
	return render(request,'bloggrid.html')


def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email is already registered!!!!!"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST["password"]==request.POST["cpassword"]:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=request.POST['password']
					)
				msg="Sign Up Successfully!!!!!"
				return render(request,'signup.html',{'msg':msg})
			else:
				msg="Password & Confirm Password does not Matched..."
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')