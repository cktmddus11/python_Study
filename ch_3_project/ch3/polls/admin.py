from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2 # 추가로 입력할수 있는 빈 공간 


# ModelAdmin 클래스를 상속받아 새로운 QuestionAdmin 클래스를 
# 정의하고, 그 클래스를 admin.site.register() 함수의 두번쨰
# 인자로 등록해주면 됨
class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] # 필드 순서 변경
    fieldsets = [ # 각 필드 분리해서 보여주기
        ('Question Statement', {'fields':['question_text']}),
        # ('Date Information', {'fields':['pub_date']}),
        ('Date Imformation', {'fields':['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline] # Choice 모델 같이보기
    list_display = ('question_text', 'pub_date') # 레코드 리스트 컬럼 항목 지정
    list_filter = ['pub_date'] # 필터 사이드 바 추가
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin) # 두번째 인자로 정의
#admin.site.register(Question)
admin.site.register(Choice)