from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from . import models


@login_required
def team_list(request):
    teams = models.Team.objects.filter(coach=request.user)
    return render(request, 'teams/team_list.html', {'teams': teams})
