from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import List_items
from .forms import PostForm
from django import forms
def post_list(request):
    posts = List_items.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'items/post_list.html', {'posts': posts})

def post_detail(request, pk):
	#event = Event.objects.get(pk=pk)   
    post = get_object_or_404(List_items, pk=pk)
    #post = List_items.objects.get(pk=pk)
    return render(request, 'items/post_detail.html', {'post': post})
  

