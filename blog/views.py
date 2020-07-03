# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Chemie, German, Russian, English
from .forms import PostForm, ChemieForm, GermanForm, RussianForm, EnglishForm
from django.shortcuts import redirect

# Create your views here.

def home_page(request):
	return render(request, 'blog/home_page.html')

def science(request):
	return render(request, 'blog/science.html')

def languages(request):
	return render(request, 'blog/languages.html')

def welcome(request):
	return render(request, 'blog/welcome.html')

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def chemistry(request):
	chemies = Chemie.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/chemistry.html', {'chemies':chemies})

def english(request):
	englishs = English.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/english.html', {'englishs':englishs})

def english_detail(request, eng):
	english = get_object_or_404(English, pk=eng)
	return render(request, 'blog/english_detail.html', {'english': english})

def german(request):
	germans = German.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/german.html', {'germans':germans})

def russian(request):
	russians = Russian.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/russian.html', {'russians':russians})

def chemistry_detail(request, cm):
	chemie = get_object_or_404(Chemie, pk=cm)
	return render(request, 'blog/chemistry_detail.html', {'chemie': chemie})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def german_detail(request, gm):
	german = get_object_or_404(German, pk=gm)
	return render(request, 'blog/german_detail.html', {'german': german})

def russian_detail(request, rn):
	russian = get_object_or_404(Russian, pk=rn)
	return render(request, 'blog/russian_detail.html', {'russian': russian})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form}) 

def chemistry_new(request):
	if request.method == "POST":
		form = ChemieForm(request.POST)
		if form.is_valid():
			chemie = form.save(commit=False)
			chemie.author = request.user
			chemie.published_date = timezone.now()
			chemie.save()
			return redirect('chemistry_detail', cm=chemie.pk)
	else:
		form = ChemieForm()
	return render(request, 'blog/chemistry_new.html', {'form':form})

def german_new(request):
	if request.method == "POST":
		form = GermanForm(request.POST)
		if form.is_valid():
			german = form.save(commit=False)
			german.author = request.user
			german.published_date = timezone.now()
			german.save()
			return redirect('german_detail', gm=german.pk)
	else:
		form = GermanForm()
	return render(request, 'blog/german_new.html', {'form': form})

def russian_new(request):
	if request.method == "POST":
		form = RussianForm(request.POST)
		if form.is_valid():
			russian = form.save(commit=False)
			russian.author = request.user
			russian.published_date = timezone.now()
			russian.save()
			return redirect('russian_detail', rn=russian.pk)
	else:
		form = RussianForm()
	return render(request, 'blog/russian_new.html',  {'form': form})

def english_new(request):
	if request.method == "POST":
		form = EnglishForm(request.POST)
		if form.is_valid():
			english = form.save(commit=False)
			english.author = request.user
			english.published_date = timezone.now()
			english.save()
			return redirect('english_detail', eng=english.pk)
	else:
		form = EnglishForm()
	return render(request, 'blog/english_new.html', {'form': form})

def about(request):
	return render(request, 'blog/about.html')


	



