from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin  # Corrected import
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views import View
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.views.generic import *
from django.views.generic.edit import UpdateView, DeleteView



# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'app/home.html')

class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'app/signup.html', {'form':form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'app/signup.html', {'form':form})
    
class LoginView(DjangoLoginView):
    form_class = AuthenticationForm
    template_name = 'app/login.html'
    
    def get_success_url(self):
        return reverse_lazy('blog_list')
    
    def form_invalid(self, form):
        print("Login is unsuccessfull")
        return render(self.request, self.template_name, {'form':form})
    
    
    
class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'app/blog_list.html'
    context_object_name = 'blogs'
    login_url = '/login/'
    
    def get_queryset(self):
        search_query = self.request.GET.get('q')
        if search_query:
            return Blog.objects.filter(title__icontains=search_query)
        else:
            return Blog.objects.all()
    
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'app/blog_form.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog_list')
    login_url = '/login/'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        
class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Blog
    template_name = 'app/blog_detail.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'
    login_url = '/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = context['blog']
        context['comments'] = Comment.objects.filter(blog = blog)
        context['comment_form'] = CommentForm()
        return context 
    
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'app/blog_update.html'
    fields = ['title','content']
    login_url = '/login/'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner = self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs = {'pk' :self.object.pk })

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('blog_list')
    login_url = '/login/'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner = self.request.user)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'app/comment_form.html'
    form_class = CommentForm
    login_url = '/login/'
    
    def form_valid(self, form):
        blog = get_object_or_404(Blog, pk = self.kwargs['pk'])
        form.instance.blog = blog
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs = {'pk':self.kwargs['pk']})


from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from .forms import CommentForm

class CommentEditView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'app/comment_form.html'
    form_class = CommentForm
    login_url = '/login/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs['pk'], user=self.request.user)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.save()
        return redirect('blog_detail', pk=comment.blog.pk)



class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'app/comment_delete.html'
    login_url = '/login/'
     
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk = self.kwargs['pk'], user = self.request.user)
    
    def get_success_url(self):
        blog = self.object.blog
        return reverse_lazy('blog_detail', kwargs = {'pk': blog.pk})