from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse , Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm , ReplyForm
from django.contrib.auth.decorators import login_required


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def about(request):
    return render(request, 'about.html')

def board_topics(request,id):
    
    #  try:
    #      board = Board.objects.get(pk = id)
    #  except Board.DoesNotExist:
    #         raise Http404
    board = get_object_or_404(Board, pk = id)
    return render(request, 'topics.html', {'board': board})

@login_required
def new_topic(request, id): 
    board = get_object_or_404(Board, pk = id)
    if request.method == 'POST':
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
    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})

def topic_page(request,board_id,topic_id):
     topic = get_object_or_404(Topic,board__pk=board_id ,pk=topic_id)
     topic.views += 1
     topic.save()
     return render(request, 'topic_page.html', {'topic': topic})

@login_required
def reply_topic(request,board_id,topic_id):
    topic = get_object_or_404(Topic,board__pk=board_id ,pk=topic_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic = topic
            reply.created_by = request.user
            reply.save()
            return redirect('topic_page', board_id=board_id, topic_id=topic_id)
    else:
        form = ReplyForm()
    return render(request, 'reply_topic.html', {'topic_reply': topic, 'form_reply': form})