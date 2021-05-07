from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import NewBookForm, BorrowBookForm
from .models import Book

# Create your views here.

def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def books(request):
    data = { 'books': Book.objects.all() }
    return render(request, 'books.html', data)

@login_required
def create(request):
    if request.method == 'POST':
        book = NewBookForm(request.POST)
        if book.is_valid():
            book_id = book.save().id
            return redirect("library-show", book_id=book_id)
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(request, 'newbook.html', data)

@login_required
def show(request, book_id):
    try:
        # book = Book.objects.get(pk=book_id)
        # data = { 'book': book }
        # return render(request, 'show.html', data)
        book = get_object_or_404(Book, pk=book_id)
        if request.method == 'POST':
            form = BorrowBookForm(request.POST)
            if form.is_valid():
                book.borrower = request.user
                book.save()
                return redirect("library-show", book_id=book_id)
        else:
            form = BorrowBookForm(initial={'borrower': request.user})
        data = {
            'book': book,
            'form': form
        }
        return render(request, 'show.html', data)
    except:
        raise Http404('We don\'t have that book here!')

