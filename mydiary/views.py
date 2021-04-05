from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import ContentForm
from .models import Content


# Create your views here.
def home(request):
	posts = Content.objects.all()
	return render(request, 'home.html', {'posts_list' : posts})
    #콘텐트가 클래스가 오브젝트가 객체
    #콘텐프에서 찍어낸 식빵 모두 담아놓아라

def new(request):
	if request.method == 'POST':
		form = ContentForm(request.POST, request.FILES)
        #
		if form.is_valid():
			post = form.save(commit=False)
            #flase 넣어주는 것은 당장 저장해주는 게 아니고 좀이따 넣어주는 것이라는 뜻
			post.author = request.user
            #user을 author에 대입해준다는것
			post.published_date = timezone.now()
            #타임존은 자동으로 생성되는 현재 시간의 값
			post.save()
			return redirect('home')
            #기본적으로 함수는 return 만나면 끝나버린다
	else : 
		form = ContentForm()
	return render(request, 'new.html', {'form':form})

def detail(request, index):
	post = get_object_or_404(Content, pk=index)
	return render(request, 'detail.html', {'post':post})

def edit(request, index):
	post = get_object_or_404(Content, pk=index)
	if request.method == "POST":
		form = ContentForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now
			post.save()
			return redirect('detail', index = post.pk)
	else:
		form = ContentForm(instance=post)
	return render(request, 'edit.html', {'form':form})

def delete(request, pk):
	post = get_object_or_404(Content, pk=pk)
	post.delete()
	return redirect('home')
	#삭제 잘되었으면 home

#pk를 어떤 변수에 넣어주엇냐 차이
#커밋을 false로 하는 것은 당장 저장하지 않겠다는 뜻 중복될수도 있으니깐
# redirect : 위의 함수를 다시호출, index라는 이름으로 pk받아와서
# 뒤에 헷갈리지 말라고 index=post.pk 붙여줘서 알려주는고양

#이 정보가 인덱스에 담겨져서 와서 인자를 인덱스로 받아주는 것이다
#post라는 이름으로 post를 받아서 줄게
#객체가 없다면 404 에러를 띄워라

#콘텐트에서 객체 가져올건데 인덱스를 가지고 있는데 pk가 인덱스인 애를 데리고 와~하는 것
    #렌더는 리턴값이 탬플릿이다, 
    #그래서 컨텍스트를 같이 줄 수 있다
    #redirect는 리턴값이 url이라 이런 컨텍스트값을 주지 못한다

    

