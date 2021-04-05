from django import forms
#form은 모델에서 노출시킬지 여부 결정해주기도 하고, 
#처리하고 싶은 부분을 정의해주는 친구라고 생각하면 된다
from .models import Content

class ContentForm(forms.ModelForm):
	class Meta: #폼을 만들기 위해서 어떤 필드를 쓸것인지 알려주는 역할
        #나중에 필드 많아지면 구별하는 것 어려워서 얘를 사용한다
		model = Content
		fields = ['title', 'body',]#'achivement',]
        #pub_date는 디폴트로 가져와서 입력받을 필요없어