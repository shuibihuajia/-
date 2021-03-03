from django.conf.urls import url
from . import views

app_name = "apone"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    # 作家url
    url(r'^writers', views.writers, name="writers"),
    url(r'^add_writer/', views.add_writer, name="add_writer"),
    url(r'^remove_writer', views.remove_writer, name="remove_writer"),
    url(r'^edite_writer', views.edite_writer, name="edite_writer"),

    url(r'books/', views.books, name="books"),
    url(r'add_book/', views.add_book, name="add_book"),
    url(r'remove_book/(\d+)', views.remove_book, name="remove_book"),
    url(r'edite_book/(\d+)', views.edite_book, name="edite_book"),

    url(r'publishers/', views.publishers, name="publishers"),
    url(r'^add_publisher/', views.add_publisher, name="add_publisher"),
    url(r'^remove_publisher', views.remove_publisher, name="remove_publisher"),
    url(r'^edite_publisher', views.edite_publisher, name="edite_publisher"),
]
