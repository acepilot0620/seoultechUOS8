from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from account.models import Accout
# Create your views here.

def post(request):

    if request.method == "POST":
        post = Post()
        try: #로그인 체크
            user = request.user
            profile = Account.objects.get(user=user)
            post.author = profile
            post.prof = request.POST['prof']
            post.term = request.POST['term']
            post.content = request.POST['prof']
            post.total_score = request.POST['prof']
            post.check_att = request.POST['attend']
            post.lev_of_diff = request.POST['Level']
            post.quantity = request.POST['Study']
            post.grade = request.POST['Grade']
            post.achievement = request.POST['Value']
            post.save()
        except: #유저 로그인 안 했을 경우
            return redirect('account:login')
        return redirect('accout:home')
    else:
        try: #로그인 체크
            user = request.user
            profile = Profile.objects.get(user=user)
        except: #유저 로그인 안했을 경우
            return redirect('account:login')
        return render(request, 'post/post.html')

def delete(requset, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('account:home')