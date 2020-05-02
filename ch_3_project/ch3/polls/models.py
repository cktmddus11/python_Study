from django.db import models

# Create your models here.

# 테이블 설계
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    objects = models.Manager()
    # 장고에서 기본키는 자동 생성
    def __str__(self):
        return self.question_text # 리턴값이 admin 테이블에서 내용으로 보여짐

class Choice(models.Model):
    # 외래키 기본키 클래스 명만 지정
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self): # 객체를 문자열로 표현할 떄 사용하는 함수
        return self.choice_text       # 이거 해야지 사이트에서 제대로 표시됨
        