from django.shortcuts import render, HttpResponse
# from django.contrib import admin

# def index(request):
#     return render(request, 'index.html')

def index(request):
    # 여기에서는 간단한 예시로 두 개의 게임 값을 컨텍스트에 추가하여 템플릿에 전달합니다.
    game_value_1 = 1
    game_value_2 = 2

    # 사용자의 GET 요청을 확인하여 선택된 게임 값이 있는지 확인합니다.
    selected_game = request.GET.get('game_select')                                                                                                

    # 선택된 게임 값이 있다면 어떤 처리를 수행하거나 결과를 가져올 수 있습니다.
    # 이 예시에서는 그냥 출력하도록 하겠습니다.
    if selected_game:
        print(f"Selected game: {selected_game}")

    # 컨텍스트에 변수들을 추가하여 템플릿에 전달합니다.
    context = {
        'game_value_1': game_value_1,
        'game_value_2': game_value_2,
    }

    # render 함수를 사용하여 템플릿을 렌더링하고 응답을 생성합니다.
    return render(request, 'index.html', context)





"""
topics =[
    {'link':'Bluearchive', 'title':'Bule Archive', "body":'conntinue blue archive test'},
    {'link':'Maplestroy', 'title':'Maple Story', "body":'conntinue maple story test'},
    {'link':'Main', 'title':'Sub Site', "body":'conntinue main test'}
]

def HTMLtemp(tag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href ="/{topic["link"]}"> {topic["title"]}</a></li>'   
    return f'''
    <html>
    <body>
        <h1><a href = '/'> Home</h1>
        <ol>
            {ol}
        </ol>
        {tag}
    </body>
    </html>
    '''

# Create your views here.
def index(request):
    h2 ='''
    <h2>Hello, World!</h2>
    pratice web site
    '''
    return HttpResponse(HTMLtemp(h2))

def BA(request):
    global topics
    article = ''
    for topic in topics:
        if topic['link'] == 'Bluearchive':
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLtemp(article))

def MS(request):
    global topics
    article = ''
    for topic in topics:
        if topic['link'] == 'Maplestroy':
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLtemp(article))

def main(request):
    global topics
    article = ''
    for topic in topics:
        if topic['link'] == 'Main':
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLtemp(article))
"""