from django.shortcuts import render

from books.models import Book
from books.functions import get_adjacent_dates


def books_view(request):
    book_objects = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': book_objects,
    }
    return render(request, template, context)

def books_view_date(request, pub_date):
    pub_dates_query = Book.objects.order_by('pub_date').values(
                    'pub_date').distinct()
    pub_dates = [str(entry['pub_date']) for entry in pub_dates_query]
    previous_date, next_date = get_adjacent_dates(pub_date, pub_dates)

    book_objects = Book.objects.filter(pub_date=pub_date)
    template = 'books/books_list_by_date.html'
    context = {
        'books': book_objects,
        'previous_date': previous_date,
        'next_date': next_date,
    }
    return render(request, template, context)
