import os
from django.db.models import Avg, Max, Min, Count
os.environ.setdefault("DJANGO_SETTINGS_MODULE","BMS.settings")
import django
django.setup()
from apone.models import Books
# res = Books.objects.exclude(id=3).order_by("-pub_date")
# res = Books.objects .values("main_content","name")
res=Books.objects.all().aggregate(Avg("price"), Max("price"), Min("price"))
print(res)
q1= Books.objects.all().annotate(nums=Count("writers"))
print(q1)
q2= Books.objects.annotate(nums=Count("writers"))
for i in q2:
    print(i.nums)
