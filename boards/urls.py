# /discussion_board/boards/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boards/<int:id>', views.board_topics, name='board_topics'),
    path('boards/<int:id>/new', views.NewTopicView.as_view(), name='new_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>', views.TopicPageView.as_view(), name='topic_page'),
    path('boards/<int:board_id>/topics/<int:topic_id>/reply', views.ReplyTopicView.as_view(), name='reply_topic'),
    path('boards/<int:board_id>/topics/<int:topic/id>/edit/posts/<int:post_id>', views.EditPostView.as_view(), name='edit_post'),
]
