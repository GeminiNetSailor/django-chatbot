# chat/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RoomForm
from .models import Room, Message


@login_required(login_url='/login/')
def index(request):
    template = 'chat/index.html'
    data = {
        'rooms': Room.objects.all(),
        'form': RoomForm()
    }

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room_instace = form.save(commit=False)
            room_instace.owner = request.user
            room_instace.save()
            return render(request, template, data)

    return render(request, template, data)


@login_required(login_url='/login/')
def room(request, room_name):
    room_instace = get_object_or_404(Room, name=room_name)
    messages = reversed(Message.objects.filter(room=room_instace).order_by('-timestamp')[:50])

    return render(request, 'chat/room.html', {
        'messages': messages,
        'room': room_instace
    })


@login_required(login_url='/login/')
def delete_room(request, id):
    room_instace = get_object_or_404(Room, pk=id)
    if request.user != room_instace.owner:
        return redirect('index')
    room_instace.delete()
    return redirect('index')
