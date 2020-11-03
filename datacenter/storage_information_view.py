from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import datetime
from .view_helpers import format_duration


def get_duration(entered_at):
    delta = datetime.now() - entered_at.replace(tzinfo=None)
    return delta


def storage_information_view(request):
    non_closed_visits = []

    all_visits = Visit.objects.all()
    for visit in all_visits:
        if visit.leaved_at is not None:
            continue
        duration = get_duration(visit.entered_at)
        non_closed_visits.append(
            {
                "who_entered": visit.passcard,
                "entered_at": visit.entered_at,
                "duration": format_duration(duration)
            }
        )
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
