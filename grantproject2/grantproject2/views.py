from django.http import HttpResponse

def index(request):
    return HttpResponse("Django Code for Website")

def about(request):
    return HttpResponse("About Django Coding!!!!")

def w_links(request):
    s = ''' <h1> Navigation Bar <br> </h1>
    <a href = "https://www.facebook.com/"> Facebook </a><br>
    <a href = "https://www.flipkart.com/">Flipkart </a><br>
    <a href = "https://www.bing.com/">News </a><br>
    <a href = "https://www.google.com/">Google </a><br>'''
    return HttpResponse(s)