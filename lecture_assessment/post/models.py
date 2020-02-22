from django.db import models
from django.utils import timezone
from account.models import Profile

# Create your models here.

class Post(models.Model):

    class_name = models.CharField(max_length=50)                             #과목명
    prof = models.CharField(max_length=50)                                   #담당 교수(교수별로도 볼 수 있게 되려면 작성자의 경우와 같은 모델 사용)
    term = models.CharField(max_length=50)                                   #수강학기
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)            #작성자
    pub_date = models.DateTimeField(auto_now_add=True)                       #등록일
    content = models.TextField()                                             #강의평 내용
    total_score = models.PositiveIntegerField(default=0)                     #총점
    check_att = models.PositiveIntegerField(default=0)                       #출첵
    lev_of_diff = models.PositiveIntegerField(default=0)                     #난이도
    quantity = models.PositiveIntegerField(default=0)                        #학습량
    grade = models.PositiveIntegerField(default=0)                           #학점
    achievement = models.PositiveIntegerField(default=0)                     #성취

    def __str__(self):
        return self.total_score

    def summary(self):
        return self.content[:100]

    class Meta:
        ordering = ['-total_score'] 