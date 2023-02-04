from django.shortcuts import render

# Create your views here.
def Blog(request):

    datas = {}

    return render(request, "blog.html", datas)