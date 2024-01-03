from django.shortcuts import render,redirect
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
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic']
					)
				msg="Sign Up Successfully!!!!!"
				return render(request,'signup.html',{'msg':msg})
			else:
				msg="Password & Confirm Password does not Matched..."
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'])
			if request.POST['password']==user.password:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				return render(request,'index.html')
			else:
				msg="Incoreect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg='Email not registered'
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	del request.session['email']
	del request.session['fname']
	return render (request,'login.html')

def changepassword (request):
	if request.method =='POST':
		user=User.objects.get(email=request.session['email'])
		if user.password == request.POST['oldpassword']:
			if request.POST['npassword'] == request.POST['cnpassword']:
				user.password = request.POST['npassword']
				user.save()
				return redirect('logout')
			else:
				msg='New Password & Confirm New Password does not Matched'
				return render (request,'changepassword.html',{'msg':msg})
		else:
			msg=' Old Password does not Matched'
			return render (request,'changepassword.html',{'msg':msg})
	else:
		return render (request,'changepassword.html')









