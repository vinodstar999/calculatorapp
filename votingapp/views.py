from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

arr = ['Java','Python','Javascript','Sql','CSS','HTML']
global_count = dict()
# Create your views here.
def index(request):
  mydictionary= {
    "arr" : arr
  }
  return render(request,'index.html',context=mydictionary)

def getquery(request):
  q = request.GET['languages']
  if q in global_count:
    # if already exists increment the value
    global_count[q]+=1 
    # first occurrence
  else:
    global_count[q]=1
  mydictionary={
    "arr" : arr,
    "global_count" :global_count
  }
  return render(request,'index.html',context=mydictionary)


def sortdata(request):
  global global_count 
  global_count=dict(sorted(global_count.items(),key=lambda x:x[1],reverse=True))
  mydictionary = {
    "arr" : arr,
    "global_count" : global_count
  }
  return render(request,'index.html',context=mydictionary)
