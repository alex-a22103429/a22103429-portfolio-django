from django.shortcuts import render

# Create your views here.
#  hello/views.py

from django.shortcuts import render

def home_page_view(request):
	return render(request, 'portfolio/home.html')

def aboutme_page_view(request):
	return render(request, 'portfolio/about-me.html')

def home1_page_view(request):
	return render(request, 'portfolio/index-copy.html')

def home2_page_view(request):
	return render(request, 'portfolio/index.html')

def home3_page_view(request):
	return render(request, 'portfolio/indexcadeiras.html')

def home4_page_view(request):
	return render(request, 'portfolio/indexcalculadora.html')

def home5_page_view(request):
	return render(request, 'portfolio/indexcopy.html')

def home6_page_view(request):
	return render(request, 'portfolio/indexpresentation.html')

def home7_page_view(request):
	return render(request, 'portfolio/indeximagem.html')

def home8_page_view(request):
	return render(request, 'portfolio/index1.html')



