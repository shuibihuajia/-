from django.shortcuts import render, redirect
from apone import models
from apone.models import Writers
from django.urls import reverse


def index(request):
    return render(request, "index.html")


# writers
def writers(request):
    obj = models.Writers.objects.all()
    # obj1 = models.Writers.objects.get(id=1)
    # writer_books = obj1.books_set.get()
    # 这里想要实现作者有哪些书，没能成功对应
    return render(request, "writers.html", {"writers": obj})


def add_writer(request):
    if request.method != "POST":
        return render(request, "add_writer.html")
    else:
        name = request.POST.get("writer_name")
        new_name = models.Writers.objects.create(name=name)
        new_name.save()
        return redirect("apone:writers")


def remove_writer(request):
    dele_obj = request.GET.get("id")
    obj = models.Writers.objects.get(id=dele_obj)
    obj.delete()
    return redirect("apone:writers")


def edite_writer(request):
    if request.method == "POST":
        new_writer_id = request.POST.get("writer_id")
        new_writer_name = request.POST.get("writer_name")
        obj = Writers.objects.get(id=new_writer_id)
        obj.name = new_writer_name
        obj.save()
        return redirect("/writers/")
    edite_id = request.GET.get("id")
    edite_obj = Writers.objects.get(id=edite_id)
    return render(request, "edite_writer.html", {"edite_writer": edite_obj})


# books
def books(request):
    obj = models.Books.objects.all()
    return render(request, "books.html", {"books": obj})


def add_book(request):
    writers_obj = models.Writers.objects.all()
    publisher_list = models.Publishers.objects.all()
    context = {"writers_list": writers_obj, "publisher_list": publisher_list}

    if request.method != "POST":
        return render(request, "add_book.html", context)
    name = request.POST.get("book_name")
    writer = request.POST.getlist("writer_name")
    publisher = request.POST.get("publisher_id")
    new_pub_date = request.POST.get("pub_date")
    main_content = request.POST.get("main_content")

    new_writers = models.Books.objects.create(name=name, pub_date=new_pub_date, main_content=main_content,
                                              pub_company_id=publisher)
    # 一本书对应多个作者
    new_writers.writer.set(writer)
    new_writers.save()
    return redirect("/books/")


def remove_book(request, arg):
    # print(arg)
    # remove_id = request.GET.get("id")
    remove_obj = models.Books.objects.get(id=arg)
    remove_obj.delete()
    return redirect("apone:books")


def edite_book(request, arg):
    if request.method != "POST":
        # 之前是通过url连接传递id值，所以需要get（）一下
        # edite_id = request.GET.get("id")
        edite_obj = models.Books.objects.get(id=arg)
        writers_obj = models.Writers.objects.all()
        publisher_list = models.Publishers.objects.all()
        context = {"books_list": edite_obj, "writers_list": writers_obj, "publisher_list": publisher_list}
        return render(request, "edite_book.html", context)
    book_id = request.POST.get("book_id")
    book_name = request.POST.get("book_name")
    writer = request.POST.getlist("writer_id")
    publisher = request.POST.get("publisher_id")
    new_pub_date = request.POST.get("pub_date")
    main_content = request.POST.get("main_content")
    # 获取要修改的对象
    new_edite_obj = models.Books.objects.get(id=book_id)
    new_edite_obj.name = book_name
    # 修改多对多字段时要用<多对多字段> .set(<新值>)
    new_edite_obj.writer.set(writer)
    new_edite_obj.pub_company.name = publisher
    new_edite_obj.pub_date = new_pub_date
    new_edite_obj.main_content = main_content
    new_edite_obj.save()
    # 这两种方式都可以取到
    # return redirect("apone:books")
    url = reverse("apone:books")
    return redirect(url)


def publishers(request):
    obj = models.Publishers.objects.all()
    return render(request, "publishers.html", {"publishers": obj})


def add_publisher(request):
    if request.method != "POST":
        return render(request, "add_publisher.html")
    else:
        name = request.POST.get("publisher_name")
        new_name = models.Publishers.objects.create(name=name)
        new_name.save()
        return redirect("apone:publishers")


def remove_publisher(request):
    dele_obj = request.GET.get("id")
    obj = models.Publishers.objects.get(id=dele_obj)
    obj.delete()
    return redirect("apone:publishers")


def edite_publisher(request):
    if request.method == "POST":
        publisher_id = request.POST.get("publisher_id")
        new_publisher_name = request.POST.get("publisher_name")
        obj = models.Publishers.objects.get(id=publisher_id)
        obj.name = new_publisher_name
        obj.save()
        return redirect("/publishers/")
    else:
        edite_id = request.GET.get("id")
        edite_obj = models.Publishers.objects.get(id=edite_id)

    return render(request, "edite_publisher.html", {"edite_publisher": edite_obj})
