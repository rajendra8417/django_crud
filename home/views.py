from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):
    people=[ 

{ "name":"abcd", "age":21},
{ "name":"mnop", "age":23},
{ "name":"efgh", "age":18},
{ "name":"jklm", "age":23},
{ "name":"abcd", "age":21}
]
    text= "iomwitnhiogvhviboihjtnoji"
    
    return render(request, "index.html", context={"peoples":people, "text":text})
    

def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")