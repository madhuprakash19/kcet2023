from django.shortcuts import render
from cutoff.models import EngGenRound1

# Create your views here.
def round1(request):
    if request.method == 'POST':
        rank = request.POST['rank']
        result = list(EngGenRound1.objects.filter(gm__gt=int(rank),branch="IE").order_by("gm"))
        return render(request,'test1.html',{'result':result})
    return render(request,'test1.html')
