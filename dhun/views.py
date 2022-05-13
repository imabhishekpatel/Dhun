from pyexpat import model
from urllib import request
from django.contrib.auth.hashers import make_password
from django.forms import fields
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Album, Song, User
from .myforms import Signinform, Signupform 
from django.views import generic
from django.urls import reverse_lazy,reverse
from dhun import models
from django.contrib.auth.mixins import LoginRequiredMixin


class Signupview(generic.View):
    def get(self,request):
        return render(request,'dhun/signup.html',{'form':Signupform(None)})
    def post(self,request):
        f=Signupform(request.POST)
        if f.is_valid():
            tempform=f.save(commit=False)
            p=f.cleaned_data['password']
            tempform.password=make_password(p)
            tempform.save()
            return redirect('dhun:signin')
        return render(request,'dhun/signup.html',{'form':f})
        
class Signinview(generic.View):
    def get(self,request):
        return render(request,'dhun/login.html',{'form':Signinform(None)})
    def post(self,request):
        f=Signinform(request.POST)
        if f.is_valid():
            u=f.cleaned_data.get('username')
            obj=User.objects.get(username=u)
            self.request.session['user_log']={'username':obj.username}
            redirect_to =request.GET.get('next')
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('dhun:home')
        return render(request,'dhun/login.html',{'form':f})
    
class Home(generic.ListView):
    template_name='dhun/home.html'
    context_object_name='data'
    def get_queryset(self):
        alb=Album.objects.all()
        songs=Song.objects.all()
        return {'songs':songs[:5], 'alb':alb[:5]}

def signout(request):
    request.session.pop("user_log")
    return redirect("dhun:home")

class Addalbum(LoginRequiredMixin,generic.CreateView):
    login_url='dhun:signin'
    model=Album
    template_name='dhun/addalbum.html'
    success_url=reverse_lazy('dhun:addsong')
    fields=['album_name','artist_name','album_logo','album_genre']
    context_object_name='form'
    def form_valid(self,form):
        u=self.request.session.get('user_log')
        u1=User.objects.get(username=u.get('username'))
        form.instance.userid=u1
        return super().form_valid(form)

class Addsong(generic.CreateView):
    model=Song
    template_name='dhun/addsong.html'
    fields=['album_id','song_name','song_image','song']
    context_object_name='form'

    # def get_success_url(self,request):
    #     redirect_to =request.GET.get('next')
    #     if redirect_to:
    #         return reverse(redirect_to)
    #     else:
    #         return reverse("dhun:home")    

class Myalbum(generic.ListView):
    template_name='dhun/myalbum.html'
    context_object_name='data'
    # model=Album
    def get_queryset(self):
        u=self.request.session.get("user_log")
        if u:
            alb1=User.objects.get(username=u.get('username'))
            return {'alb':Album.objects.filter(userid=alb1)}
        else:
            return None

class Albumplaying(generic.ListView):
    template_name='dhun/playing.html'
    context_object_name='data'
    def get_queryset(self):
        albumid=self.kwargs.get('pk')
        album=Album.objects.get(id=albumid)
        return {'album':album, 'song':album.song_set.all()}

class Seeallalbum(generic.ListView):
    template_name='dhun/seeallalbum.html'
    context_object_name='data'
    def get_queryset(self):
        dt=Album.objects.all()
        name='Albums'
        return {'dt':dt, 'name':name}

class Seeallsong(generic.ListView):
    template_name='dhun/seeallsong.html'
    context_object_name='data'
    def get_queryset(self):
        dt=Song.objects.all()
        name='Songs'
        return {'dt':dt, 'name':name}

class Editsong(generic.UpdateView):
    model=Song
    template_name='dhun/addsong.html'
    fields=['album_id','song_name','song_image','song']
    context_object_name='form'

class EditAlbum(generic.UpdateView):
    model=Album
    template_name='dhun/addalbum.html'
    fields=['userid','album_name','artist_name','album_logo','album_genre']
    context_object_name='form'
    
    

# class Deletesong(generic.DeleteView):
#     template_name='dhun/delete.html'
#     model=Song
#     # context_object_name='prod'
#     success_url=reverse_lazy('dhun:play')
#     success_message='product deleted'

def deletesong(request,pk):
    song=Song.objects.get(id=pk)
    song.delete()
    return redirect('dhun:play')
print('hello')