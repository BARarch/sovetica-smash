from django.shortcuts import render
from datetime import datetime
from .models import Article


        
def get_articles():
    
    result = Article.objects.all()
    
    
    return result
        
def index(request):
    
    content = {
        
        'current_date': datetime.now(),
        'title': "Home"
    }
    
    return render(request, 'index.html', content)

def about(request):
    content = {
        'current_date': datetime.now(),
        'title':'About'
    }   
    return render(request, 'about.html', content)
    
def news(request):
    
    populate_db()
    
    articles = get_articles()
    
    content = {
        'articles': articles,
        'current_date': datetime.now(),
        'title':'News'
    }  
    return render(request, 'news.html', content)

def populate_db():
    if Article.objects.count() == 0:
        Article(title = 'first item', content='this is the first db item').save()
        Article(title = 'second item', content='this is the second item').save()
        Article(title = 'third item', content='this is the last item for now').save()
        