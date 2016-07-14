from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from . import models


def team_list(request):
    teams = models.Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})


def team_detail(request, pk):
    team = get_object_or_404(models.Team, pk=pk)
    return render(request, 'teams/team_detail.html', {'team': team})


class TeamListView(ListView):
    context_object_name = 'teams'
    model = models.Team


class TeamDetailView(DetailView):
    model = models.Team


class TeamCreateView(CreateView):
    fields = ('name', 'practice_location', 'coach')
    model = models.Team


class TeamUpdateView(UpdateView):
    fields = ('name', 'practice_location', 'coach')
    model = models.Team


class TeamDeleteView(DeleteView):
    model = models.Team
