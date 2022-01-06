from django.shortcuts import redirect,render
from .models import Post
import os
from django.conf import settings
from django.core.paginator import Paginator

def index(request):
    return render(request, 'board/index.html')

def list(request):
    page = request.GET.get('page','1')
    postlist = Post.objects.all().order_by('-id')

    paginator = Paginator(postlist,10)
    postlist = paginator.get_page(page)

    return render(request, 'board/list.html', {'postlist':postlist})

# 글쓰기 
def write(request):
    if request.method=='POST':
        # 페이징 처리를 위한 더미데이터 200개 입력시 사용
        #for i in range(200):
        try:
            Post.objects.create(
                user_id = request.POST['user_id'],
                titles = request.POST['titles'],
                #titles = request.POST['titles'] + "-" + str(i),
                passwd = request.POST['passwd'],
                contents = request.POST['contents'],
                # 파일첨부를 하지 않으면 여기서 예외발생됨.
                mainphoto = request.FILES['mainphoto'],
            )
        except:
            # 파일첨부를 하지 않은 경우이므로 제목과 내용만 입력함
            Post.objects.create(
                user_id = request.POST['user_id'],
                titles = request.POST['titles'],
                #titles = request.POST['titles'] + "-" + str(i),
                passwd = request.POST['passwd'],
                contents = request.POST['contents'],
            )
            # create()를 통해 insert 처리
        # 입력이 처리되었다면 리스트로 이동한다. 
        return redirect('../list')
    # 전송방식이 GET이라면 글쓰기 페이지로 진입한다. 
    return render(request, 'board/write.html')

# 글 상세보기
def view(request, pk):
    # 일련번호에 해당하는 게시물 하나를 select한다.
    post = Post.objects.get(pk=pk)
    return render(request, 'board/view.html', {'post':post})

# 글 수정하기
def edit(request, pk):
    # 일련번호를 통해 기존 게시물 가져오기 
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            post.user_id = request.POST['user_id']
            post.titles = request.POST['titles']
            post.passwd = request.POST['passwd']
            post.contents = request.POST['contents']
            post.mainphoto = request.FILES['mainphoto']
            
            print(os.path.join(settings.MEDIA_ROOT, request.POST['prevphoto']))
            os.remove(os.path.join(settings.MEDIA_ROOT, request.POST['prevphoto']))
        except:
            post.user_id = request.POST['user_id']
            post.titles = request.POST['titles']
            post.passwd = request.POST['passwd']
            post.contents = request.POST['contents']
        # 폼값 처리 후 save() 함수를 통해 update 처리함.
        post.save()
        # 수정처리가 완료되면 상세보기 페이지로 이동함
        return redirect('../view/'+str(pk))
    else:
        # 전송방식이 GET이라면 수정하기로 진입함
        return render(request, 'board/edit.html', {'post':post})   

# 글 삭제하기
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method=='GET':
        # 게시물 삭제 
        post.delete()
        return redirect('../list/')

