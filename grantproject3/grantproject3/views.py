from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def formattext(request):
    #get the text
    djtext = request.POST.get('text','default')
    remove_punc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    if remove_punc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        formatted = ""
        for char in djtext:
            if char not in punctuations:
                formatted = formatted + char

        params = {'purpose':'Remove Punctuations' , 'formatted_text':formatted}
        #return render(request , 'formatted.html',params)
        djtext = formatted

    if fullcaps=="on":
        formatted = ""
        for char in djtext:
            formatted = formatted + char.upper()
        params = {'purpose':'Changed to Upper Case' , 'formatted_text':formatted}
        #return render(request , 'formatted.html',params)
        djtext = formatted

    if newlineremover=="on":
        formatted = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                formatted = formatted + char
        params = {'purpose':'Removed New lines' , 'formatted_text':formatted}
        #return render(request , 'formatted.html',params)
        djtext = formatted

    if extraspaceremover=="on":
        formatted = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                formatted = formatted + char
        params = {'purpose':'Removed Extra Spaces' , 'formatted_text':formatted}
        #return render(request , 'formatted.html',params)
        djtext = formatted

    #else:
        #return HttpResponse(djtext)

    return render(request,'formatted.html',params)