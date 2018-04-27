from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=32)
    pub_date = models.DateField(auto_now_add=False)
    pub_company = models.ForeignKey("Publishers")
    main_content = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Writers(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField("Books")
    def __str__(self):
        return self.name

class Publishers(models.Model):
    name = models.CharField(max_length=32)
    #writers = models.ManyToManyField("Writers")

    def __str__(self):
        return self.name
