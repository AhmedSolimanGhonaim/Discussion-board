from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse , Http404
from .models import Board, Topic, Post

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


def new_topic(request, id): 
    board = get_object_or_404(Board, pk = id)
    if request.method == 'POST':
        topic_subject = request.POST['subject']
        topic = Topic.objects.create(subject=topic_subject, board=board, created_by=request.user)
        return redirect('board_topics', id=board.pk)
    return render(request, 'new_topic.html', {'board': board})