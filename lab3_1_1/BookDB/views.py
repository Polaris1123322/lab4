# -*- coding: utf-8 -*-
# Create your views here.
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
from models import Book, Author
def books(request):
    t = get_template('books.html')
    if 'author'  in request.GET and request.GET['author'] != '':
        try:
            author = Author.objects.get(name=request.GET['author'])
            book_list = Book.objects.filter(author_id=author)
        except:
            book_list = []
    else:
        book_list = Book.objects.all()
    books = []
    for book in book_list:
        bk = {}
        bk['title'] = book.title
        bk['link'] = '/book_detail/'+str(book.ISBN)
        bk['del'] = '/book_delete/'+str(book.ISBN)
        bk['edi'] = '/book_editor/'+str(book.ISBN)
        bk['author'] = book.author_id.name
        bk['publisher'] = book.publisher
        bk['price'] = book.price
        books.append(bk)
    html = t.render(Context({'item_list': books}))
    return HttpResponse(html)

def book_detail(request):
    t = get_template('book_detail.html')
    path = request.path
    book_id = path.split('/')[2]
    book = Book.objects.get(ISBN = book_id)
    author = book.author_id
    del_link = '/book_delete/'+str(book.ISBN)
    edi_link = '/book_editor/'+str(book.ISBN)
    html = t.render(Context({'book':book, 'author':author, 'del_link':del_link, 'edi_link':edi_link}))
    return HttpResponse(html)

def book_delete(request):
    t = get_template('feedback.html')
    try:
        path = request.path
        book_id= path.split('/')[2]
        book = Book.objects.get(ISBN=book_id)
        author = book.author_id
        book.delete()
        books = Book.objects.filter(author_id = author)
        if len(books) <= 0:
            author.delete()
        html = t.render(Context({'text':'删除成功'}))
    except:
        html = t.render(Context({'text':'删除失败'}))
    return HttpResponse(html)
    
def add_book(request):
    t = get_template('add_book.html')
    authors = Author.objects.all()
    author_names = []
    for author in authors:
        author_names.append(author.name)
    html = t.render(Context({'authors':author_names}))
    return HttpResponse(html)

def new_book(request):
     t = get_template('feedback.html')
     try:

        author = Author.objects.get(name = request.GET['author'])
        date = request.GET['year']+'-'+request.GET['month']+'-'+request.GET['day']
        book = Book(title=request.GET['title'], author_id = author, publisher=request.GET['publisher'],
                    publish_date=date, price=request.GET['price'])
        book.save()
        html = t.render(Context({'text':'操作成功'}))
     except:
         html = t.render(Context({'text':'操作失败'}))
     return HttpResponse(html)

def add_author(request):
    t = get_template('add_author.html')
    return HttpResponse(t.render(Context()))
    
def new_author(request):
     t = get_template('feedback.html')
     try:
        Author.objects.get(name=request.GET['name'])
        html = t.render(Context({'text':'作家已经存在'}))
     except:
         try:
             author = Author(name=request.GET['name'], 
                             age=request.GET['age'], country=request.GET['country'])
             author.save()
             html = t.render(Context({'text':'操作成功'}))
         except:
             html = t.render(Context({'text':'操作失败'}))
     return HttpResponse(html)
 
def book_editor(request):
    t = get_template('book_editor.html')
    path = request.path
    book_id = path.split('/')[2]
    book = Book.objects.get(ISBN=book_id)
    book_author_name = book.author_id.name
    authors = Author.objects.all()
    author_names = []
    for author in authors:
        author_names.append(author.name)
    html = t.render(Context({'book':book,'authors':author_names, 'book_author_name':book_author_name}))
    return HttpResponse(html)
