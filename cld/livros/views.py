from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Livro
from . import urls
from .forms import LivroForm
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're from the coins index")

def livro_list(request):
	livros = Livro.objects.order_by('titulo')
	return render(request, 'livros/livro_list.html', {'livros': livros}) 

def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk) #Livro.objects.get(pk=pk)
    return render(request, 'livros/livro_detail.html', {'livro': livro}) 

def livro_new(request):
     if request.method == "POST":
         form = LivroForm(request.POST)
         if form.is_valid():
             livro = form.save(commit=False)
             #post.author = request.user
             #post.published_date = timezone.now()
             livro.save()
             return redirect('livro_detail', pk=livro.pk)
     else:
         form = LivroForm()
     return render(request, 'livros/livro_edit.html', {'form': form})

def livro_edit(request, pk):
     livro = get_object_or_404(Livro, pk=pk)
     if request.method == "POST":
         form = LivroForm(request.POST, instance=livro)
         if form.is_valid():
             livro = form.save(commit=False)
             livro.save()
             return redirect('livro_detail', pk=livro.pk)
     else:
         form = LivroForm(instance=livro)
     return render(request, 'livros/livro_edit.html', {'form': form})

def livro_delete(request, pk): 
	livro = get_object_or_404(Livro, pk=pk)
	if request.method == "POST":
		livro.delete()
		return redirect('livro_list')
	else:
		form = LivroForm(instance=livro)
	return render(request, 'livros/livro_delete.html', {'livro': livro})
    
#def livro_delete(request, pk):
#    livro = get_object_or_404(Livro, pk=pk) #Livro.objects.get(pk=pk)
#    livro.delete()
#    return render(request, '../../../', {'pk': pk}) 
 
