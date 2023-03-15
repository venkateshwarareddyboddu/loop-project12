from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'m':2090,'n':2099,'p':1099}
    return render(request,'conditional.html',context=d)


def loop(request):
    d={'name':'REYYA'}
    return render(request,'loop.html',d)