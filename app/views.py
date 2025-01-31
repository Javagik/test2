from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Content, Author, Publisher
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import Content


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/About.html'

class ContentListView(LoginRequiredMixin, ListView):
    model = Content
    context_object_name = 'contents'
    template_name = 'app/content_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('usercontent')  # Redirect to 'usercontent' if not a superuser
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')

        # Filter content based on the search query
        if query:
            filtered_contents = Content.objects.filter(title__icontains=query).order_by('-pub_date')
        else:
            filtered_contents = Content.objects.all().order_by('-pub_date')

        context['contents'] = filtered_contents
        context['total_contents'] = filtered_contents.count()  # Filtered total
        context['total_authors'] = Author.objects.count()  # You can adjust this to count authors from filtered content
        context['total_publishers'] = Publisher.objects.count()  # Similarly for publishers
        User = get_user_model()
        context['total_users'] = User.objects.count()  # Adjust to reflect filtered content if needed
        context['search_query'] = query
        return context


class UserContentView(TemplateView):
    template_name = 'app/usercontent.html'

class UserContentListView(ListView):
    model = Content
    context_object_name = 'contents'
    template_name = 'app/usercontent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        
        if query:
            filtered_contents = Content.objects.filter(title__icontains=query).order_by('-pub_date')
        else:
            filtered_contents = Content.objects.all().order_by('-pub_date')

        context['contents'] = filtered_contents
        context['total_contents'] = Content.objects.count()
        context['total_authors'] = Author.objects.count()
        context['total_publishers'] = Publisher.objects.count()
        User = get_user_model()
        context['total_users'] = User.objects.count()
        context['search_query'] = query 
        return context

    

class ContentDetailView(DetailView):
    model = Content
    context_object_name = 'content'
    template_name = 'app/content_detail.html'

class ContentCreateView(CreateView):
    model = Content
    fields = ['title', 'user', 'body', 'author', 'rating','pub_date','publisher']
    template_name = 'app/content_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model() 
        context['users'] = User.objects.all()
        context['authors'] = User.objects.all()
        context['publishers'] = User.objects.all()
        return context

class ContentUpdateView(UpdateView):
    model = Content
    fields = ['title', 'user','body', 'author', 'rating','pub_date','publisher']
    template_name = 'app/content_update.html'


class ContentDeleteView(DeleteView):
    model = Content
    template_name = 'app/content_delete.html'
    success_url = reverse_lazy('home')