from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/book/book/')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})