# i created this file - sssfasih@gmail.com

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('q',"Something")
    pc = request.POST.get('removepunc',"off")
    fullcaps = request.POST.get('fullcaps', "off")
    newline = request.POST.get('newline', "off")
    charcount = request.POST.get('charcount', "off")
    analyzed = str()
    purpose = str()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if pc == 'on':
        for chars in text:
            if chars not in punctuations:
                analyzed += chars
        purpose = "Remove Punctuations"

    if fullcaps == 'on':
        if analyzed != str():
            text=analyzed
            analyzed = str()
        for eachletter in text:
            analyzed += eachletter.capitalize()
        if purpose == str():
            purpose = "Capitalization"
        else:
            purpose += " + Capitalization"
    if newline == 'on':
        if analyzed != str():
            text=analyzed
            analyzed = str()
        for eachletter in text:
            if eachletter != '\n' and eachletter != '\r':
                analyzed += eachletter
        if purpose == str():
            purpose = "New Line Removing"
        else:
            purpose += " + New Line Removing"
    if charcount == 'on':
        if analyzed != str():
            text=analyzed
        counter = 0
        for eachletter in text:
            counter += 1
        count = len(text)

        analyzed += "\n\nTotal Characters (Manual counting)= "+str(counter)+" By len function: "+str(count)
        if purpose == str():
            purpose = "Characters Counting"
        else:
            purpose += " + Characters Counting"



    if purpose == str():
        purpose = "No Opeation Performed"
        analyzed = text

    params = {"purpose":purpose,"analyzed_text":analyzed}
    return render(request, 'analyze.html', params)


