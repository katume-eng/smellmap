from django.shortcuts import render

def init(request):
    """
    Render the initial page of the mapping application.
    """
    return render(request, 'mapping/init.html')

