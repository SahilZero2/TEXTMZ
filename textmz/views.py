# i created this file
from os import error
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render( request , 'index.html')
    #return HttpResponse('hi, Sahil this side!')

def analyze(request):
    djtext = request.GET.get('text' , 'default')

    removepunc = request.GET.get('removepunc' , 'off')
    removespace = request.GET.get('removespace' , 'off')
    removelines = request.GET.get('removelines' , 'off')
    countchar = request.GET.get('countchar' , 'off')
    

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed =  analyzed + char
        print(analyzed)
        params = {'purpose' : 'remove punctuation' , 'Analyzed_text' : analyzed}

        return render(request, 'analyze2.html' , params)

    elif( removespace == 'on'):
        # printing original string 
        print("The original string is : " + djtext)
    
        # using split() + join()
        # remove additional space from string 
        res = " ".join(djtext.split())
        
        # printing result 
        print("The strings after extra space removal : " + str(res))

        params = {'purpose' : 'remove extra spaces' , 'Analyzed_text' : res}

        return render(request, 'analyze2.html' , params)

    elif(removelines=='on'):
        analyzed =''
        for char in djtext:
            if char != "/n":
                analyzed = analyzed + char
        params = {'purpose' : 'Remove extra lines' , 'Analyzed_text' : analyzed}

        return render(request, 'analyze2.html' , params)     

    elif(countchar=='on'):
        analyzed=''
        # for char in djtext:
        analyzed = len(djtext) - djtext.count(" ") - djtext.count('/n')
        params = {'purpose' : 'Count the charachters' , 'Analyzed_text' : analyzed}

        return render(request, 'analyze2.html' , params)     

    else:
        print('error')


# def removeline(request):
#     return HttpResponse('hi, Sahil this side el!')

# def countchar(request):
#     return HttpResponse('hi, Sahil this side cc!')