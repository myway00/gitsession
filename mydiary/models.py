from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django import forms
# Create your models here.
class Content(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)
	body = models.TextField(default='')
	#achivement=models.CharField(max_length=4,choices=CHOICES,default='100%',)
#모델이 콘텐트라는 상태를 가지게 되는 것이다
#마이그레이션은 디비 올리기전에 우리 이런거 했다라고 말해주는 거고
#마이그레이트는 실제로 db에 올려주는 것, 
#그래서 생성만 해놓고 마이그레이트 안해주면 에러가 나게 되어 있다