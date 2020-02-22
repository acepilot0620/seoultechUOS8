from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
<<<<<<< HEAD
from account.models import Accout
=======
from account.models import Account

>>>>>>> a39c3ef64714e205898f61743f9a0f6a76440362
# Create your views here.

def post(request):

    if request.method == "POST":
        post = Post()
        if request.user.is_anonymous:
            return redirect('account:login')
        else:
            user = request.user
            profile = Account.objects.get(user=user)
            post.author = profile
            post.prof = request.POST['prof']
            post.term = request.POST['term']
            post.check_att = request.POST['attend']
            post.lev_of_diff = request.POST['Level']
            post.quantity = request.POST['Study']
            post.grade = request.POST['Grade']
            post.achievement = request.POST['Value']
<<<<<<< HEAD
            post.save()
        except: #유저 로그인 안 했을 경우
            return redirect('account:login')
        return redirect('accout:home')
=======
            post.content = request.POST.get('content')
            post.total_score = (int(post.check_att) + int(post.lev_of_diff) + int(post.quantity) + int(post.grade) + int(post.achievement))//5
            post.save() 
            return redirect('account:home')
>>>>>>> a39c3ef64714e205898f61743f9a0f6a76440362
    else:
        try: #로그인 체크
            user = request.user
            profile = Account.objects.get(user=user)
        except: #유저 로그인 안했을 경우
            return redirect('account:login')
        return render(request, 'post/post.html')

def delete(requset, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('account:home')