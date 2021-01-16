#This website is created by Abhi
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse('''<h1>Hello World</h1><br>
    # <a href="removepun">removepun</a>
    # <a href="capitalizefirst">capitalizefirst</a>
    # <a href="newlineremover">newlineremover</a>
    # <a href="spaceremover">spaceremover</a>
    # <a href="charcount">charcount</a>
    # ''')
    return render(request,"index.html")

def analyze(req):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    data = req.POST
    text=data.get('text',"default")
    dict = {}
    removepun = data.get("removepun","off")
    capitalize = data.get("capitalize","off")
    caplock = data.get("caplock","off")
    newlineremover = data.get("newlineremover","off")
    charcount = data.get("charcount","on")
    if text == "":
        return HttpResponse("<h1>No Data Passed</h1>")
    if removepun == "on":
        analyzed = ''
        for char in text:
            if char not in punc:
                # analyzed = analyzed+char
                analyzed = analyzed+char
        text = analyzed
    if capitalize == "on":
        analyzed =''
        analyzed = text.capitalize()
        text = analyzed
    if caplock == "on":
        analyzed = ''
        for char in text:
             analyzed = analyzed+char.upper()
        text = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in text:
            print(char)
            if char == "\n" or char == "\r":
                pass
            else:
                analyzed = analyzed+char
        text = analyzed
    if charcount == "on":
        for i in text:
            if i != " ":
                if i not in dict:
                    dict[i] = 1
                else:
                    dict[i] = dict[i] + 1
        params = {"charcount":dict}
    params = {"analyzed_text":text,"charcount":dict}
    return render(req,"analyse.html",params)

# def removepun(req):
#     text = req.GET.get('text','default')
#     print(text)
#     return HttpResponse("<h1>removepun</h1><br><a href='/'>Back</a>");
# def capitalizefirst(req):
#     return HttpResponse("<h1>capitalizefirst</h1><br><a href='/'>Back</a>");
# def newlineremover(req):
#     return HttpResponse("<h1>newlineremover</h1><br><a href='/'>Back</a>");
# def spaceremover(req):
#     return HttpResponse("<h1>spaceremover</h1><br><a href='/'>Back</a>");
# def charcount(req):
#     return HttpResponse("<h1>charcount</h1><br><a href='/'>Back</a>");
