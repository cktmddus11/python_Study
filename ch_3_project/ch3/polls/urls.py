from django.urls import path
from  . import views

app_name = 'polls'
urlpatterns = [
    # path(route : url, view : url스트링 매칭시 호출되는 뷰 함수.
    # HttpRequest 객체와 URL 스트링에서 추출된 항목이 뷰 함수 인자로 전달됨, 
    # name : url 패턴별로 이름 붙여줌. 이름은 템플릿 파일에서 사용)

    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
   
]
