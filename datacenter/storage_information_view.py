from datacenter.models import Visit
from django.shortcuts import render
from .view_helpers import format_duration


def storage_information_view(request):
    non_closed_visits = []

    all_visits = Visit.objects.all()
    for visit in all_visits:
        if visit.leaved_at is not None:
            continue
        duration = visit.get_duration()
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
