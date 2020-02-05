from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.views.generic import View

# Create your views here.


class Home(View):
	template='index.html'
	def get(self,request):
		return render(request,self.template)


class form1(View):
	template="form1.html"

	def get(self,request):
		form = Form1
		return render(request,self.template,{'form':form})
	
	def post(self,request):
		form = Form1(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponse("submitted successfully")
		return render(request,self.template,{'form':form})


class form2(View):
	template = "form2.html"

	def get(self, request):
		form = Form2
		return render(request, self.template, {'form': form})

	def post(self, request):
		form = Form2(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponse("submitted successfully")
		return render(request, self.template, {'form': form})


class form3(View):
	template = "form3.html"

	def get(self, request):
		form = Form3
		return render(request, self.template, {'form': form})

	def post(self, request):
		form = Form3(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponse("submitted successfully")
		return render(request, self.template, {'form': form})
