from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .view_helpers import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        duration = visit.get_duration()
        is_strange = visit.is_visit_long()
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": format_duration(duration),
                "is_strange": is_strange
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
