from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse , Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm , ReplyForm
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator 
from django.utils import timezone
from django.views.generic import View ,CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
def home(request):
    boards = Board.objects.all()
   
    return render(request, 'home.html', {'boards': boards})

def about(request):
    return render(request, 'about.html')

def board_topics(request,id):
    board = get_object_or_404(Board, pk = id)
    return render(request, 'topics.html', {'board': board})



@method_decorator(login_required, name='dispatch')
class NewTopicView(View):
    def get(self,request,id):
        board= get_object_or_404(Board, pk = id)
        form = NewTopicForm()
        return render(request, 'new_topic.html', {'board': board, 'form': form})
    def post(self,request,id):
        board= get_object_or_404(Board, pk = id)
        form = NewTopicForm(request.POST)
        if form.is_valid():  
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )

            return redirect('board_topics', id=board.pk)
        return render(request, 'new_topic.html', {'board': board, 'form': form})





class TopicPageView(View):
    def get(self, request, board_id, topic_id):
        topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
        session_key= 'view_topic{}'.format(topic.pk)
        if not request.session.get(session_key,False):
            topic.views += 1
            topic.save()
            request.session[session_key]= True

        
       
        return render(request, 'topic_page.html', {'topic': topic})
 



@method_decorator(login_required, name='dispatch')
class ReplyTopicView(View):
    def get(self, request, board_id, topic_id):
        topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
        form = ReplyForm()
        return self.render_reply_form(request, topic, form)

    def post(self, request, board_id, topic_id):
        topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic = topic
            reply.created_by = request.user
            reply.save()
            return redirect('topic_page', board_id=board_id, topic_id=topic_id)
        return self.render_reply_form(request, topic, form)

    def render_reply_form(self, request, topic, form):
        return render(request, 'reply_topic.html', {
            'topic_reply': topic,
            'form_reply': form
        })
@method_decorator (login_required, name='dispatch')
class EditPostView(UpdateView ):
     model= Post
     fields = ['message']
     template_name = 'edit_post.html'
     pk_url_kwarg = 'post_id'
     context_object_name = 'post'
     def form_valid(self,form):
         post = form.save(commit=False)
         post.updated_by = self.request.user
         post.updated_date = timezone.now()
         post.save()
         return redirect('topic_page', board_id=post.topic.board.pk, topic_id=post.topic.pk)

 