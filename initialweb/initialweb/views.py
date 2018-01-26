from django.shortcuts import render

class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        
def index(request):
    article1 = Article(
                        title='Article1',
                        content='''article 1 content.
                        This is a multi-line peice of content
                        This is the last line'''
                        )

    article2 = Article(
                        title='Article2',
                        content='''article 2 content.
                        This is a multi-line peice of content
                        This is the last line'''
                        )

    article3 = Article(
                        title='Article3',
                        content='''article 3 content.
                        This is a multi-line peice of content
                        This is the last line'''
                        )
    
    content = {
        'article1':article1,
        'article2':article2,
        'article3':article3,    
    }
    
    return render(request, 'index.html', content)