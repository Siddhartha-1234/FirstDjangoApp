# i made this file sid-bro
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    CharCount = request.POST.get('CharCount','off')


    if removepunc == "on":
        analysed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analysed += char
        params = {'purpose':'Removed Punctuations','analysed_text':analysed}
        djtext = analysed


    if fullcaps=="on":
        analysed=""
        for char in djtext:
            analysed += char.upper()
        params = {'purpose':'Changed to upper case','analysed_text':analysed}
        djtext = analysed


    if extraspaceremover=="on":
        analysed=""
        for index,char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1] == " ":
                pass
            else:
                analysed += char
        params = {'purpose':'Extra Space Remover','analysed_text':analysed}
        djtext = analysed



    if newlineremover=="on":
        analysed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed += char
        params = {'purpose':'Removed New Lines','analysed_text':analysed}
        djtext = analysed

        
    if CharCount=="on":
        analysed=""
        counter = 0;
        for index in djtext:
            counter += 1
        analysed = counter
        params = {'purpose':'Removed New Lines','analysed_text':analysed}
    if CharCount=="off" and newlineremover=="off" and extraspaceremover=="off" and fullcaps=="off" and removepunc == "off":
        return HttpResponse("Error")

    return render(request, 'analyse.html', params)