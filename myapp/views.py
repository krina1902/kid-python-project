from django.shortcuts import render

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