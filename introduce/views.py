from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def mbti(request):
    return render(request, 'mbti.html')

def likes(request):
    return render(request, 'likes.html')