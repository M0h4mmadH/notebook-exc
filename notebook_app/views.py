from rest_framework import generics
from rest_framework.response import Response
from .models import Note, ChecklistItem
from .serializers import NoteSerializer, ChecklistItemSerializer


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteToggleComplete(generics.UpdateAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        note = self.get_object()
        note.is_completed = not note.is_completed
        note.save()
        serializer = self.get_serializer(note)
        return Response(serializer.data)


class ChecklistItemList(generics.ListCreateAPIView):
    serializer_class = ChecklistItemSerializer

    def get_queryset(self):
        return ChecklistItem.objects.filter(note__user=self.request.user)

    def perform_create(self, serializer):
        note_id = self.kwargs.get('note_id')
        note = Note.objects.get(id=note_id, user=self.request.user)
        serializer.save(note=note)


class ChecklistItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChecklistItemSerializer

    def get_queryset(self):
        return ChecklistItem.objects.filter(note__user=self.request.user)


class ChecklistItemToggleChecked(generics.UpdateAPIView):
    serializer_class = ChecklistItemSerializer

    def get_queryset(self):
        return ChecklistItem.objects.filter(note__user=self.request.user)

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        item.is_checked = not item.is_checked
        item.save()
        serializer = self.get_serializer(item)
        return Response(serializer.data)
