#this is file for testing
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     file=open("C:\\Users\HP\PycharmProjects\Project1\Project1\Project1\data.txt")
#     return HttpResponse(file.read())


# def about(request):
#     return HttpResponse("MIT is college")
#
# def contact(request):
#     return HttpResponse("MIT contact is 123456")


# def index(request):
#     return HttpResponse("<h1> This is the basic navigator app </h1> "
#                         "<button>Func1</button><br>"
#                         "<a href='https://www.facebook.com/'> Facebook </a> <br> "
#                         "<a href='https://www.instagram.com/'> Instagram </a><br> "
#                         "<a href='https://twitter.com/i/flow/login'> Twitter </a>")
#



#project 1
# def index(request):
#     return HttpResponse("Home <a href='/about'> About </a>")
#
# def about(request):
#     return HttpResponse("Welcome to about <a href='/'> Back To Home </a>")


#create pipeline
# def index(request):
#     return HttpResponse("Home ")
#
def removepunc(request):
    mytext= request.GET.get('text','default')
    return HttpResponse("Removed punctuations from text ")
#
# def uppercase(request):
#     return HttpResponse("Uppercase all the text  ")
#
# def lowercase(request):
#     return HttpResponse("lowercase all the text ")
#
# def charcount(request):
#     return HttpResponse("Count total number of characters ")




#templates
def index(request):
    param={'name':'Prithvi','place':'Pune'}
    return render(request,'index.html',param)

def analyze(request):

    mytext = request.GET.get('text', 'off')
    mycheckbox = request.GET.get('mycheckbox','default')
    countcheckbox = request.GET.get('countcheckbox','default')
    uppercheckbox = request.GET.get('uppercheckbox','default')
    lowercheckbox = request.GET.get('lowercheckbox','default')
    punctuations= '''(){}'\/&@#$%*!^[]-_<>'''
    analyzed = ""
    if mycheckbox == "on":
            for char in mytext:
                if char not in punctuations:
                    analyzed = analyzed+char
            params = {'purpose': "Remove Punctuation", 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
    elif uppercheckbox == "on":
        newtext= mytext.upper()
        params = {'purpose': "Uppercase", 'analyzed_text': newtext}
        return render(request, 'analyze.html', params)
    elif lowercheckbox == "on":
        newtext= mytext.lower()
        params = {'purpose': "Lowercase", 'analyzed_text': newtext}
        return render(request, 'analyze.html', params)
    elif countcheckbox == "on":
        count= len(mytext)
        params = {'purpose': "Count Character", 'analyzed_text': count}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error no checkbox selected")


