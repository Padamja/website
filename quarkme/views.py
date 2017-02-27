from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	return render(request, 'html/index.html')

def about(request):
	return render(request, 'html/about-us.html')

def faq(request):
	return render(request, 'html/faq.html')

def contact(request):
	return render(request, 'html/contact.html')

def careers(request):
	return render(request, 'html/careers.html')

def hit(request):
	return render(request, 'html/how-it-works.html')

def terms(request):
	return render(request, 'html/t&c.html')

def login(request):
	return render(request, 'html/login.html')

def streg(request):
	return render(request, 'html/student-registration.html')

def tereg(request):
	return render(request, 'html/tutor-registration.html')