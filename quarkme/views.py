from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	return render(request, 'html/index.html')

def about(request):
	return render(request, 'html/about-us.html')