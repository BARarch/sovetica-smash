from django.shortcuts import render

class Article:
    def __init__(self, title, content, id):
        self.id = id
        self.title = title
        self.content = content
        
def index(request):
    article1 = Article(
                        id=1,
                        title='Article1',
                        content='''article 1 content.
                        This is a multi-line peice of content
                        This is the last line'''
                        )

    article2 = Article(
                        id=2,
                        title='Article2',
                        content='''article 2 content.
                        This is a multi-line peice of content
                        This is the last line'''
                        )

    article3 = Article(
                        id=3,
                        title='Article3',
                        content='''article 3 content.
                        This is a multi-line peice of content
                        This is the last line'''
                        )
    
    content = {
        'articles':[article1, article2, article3]  
    }
    
    return render(request, 'index.html', content)