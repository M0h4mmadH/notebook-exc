from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    path('notes/<int:pk>/toggle_complete/', views.NoteToggleComplete.as_view(), name='note-toggle-complete'),
    path('notes/<int:note_id>/checklist_items/', views.ChecklistItemList.as_view(), name='checklist-item-list'),
    path('checklist_items/', views.ChecklistItemList.as_view(), name='checklist-item-detail'),
    path('checklist_items/<int:pk>/', views.ChecklistItemDetail.as_view(), name='checklist-item-detail'),
    path('checklist_items/<int:pk>/toggle_checked/', views.ChecklistItemToggleChecked.as_view(), name='checklist-item-toggle-checked'),
]