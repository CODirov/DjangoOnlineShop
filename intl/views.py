from django.shortcuts import render
from django.utils.translation import gettext as _


def intl(request):
    context = {
        "data": [_("Kitoblar"), _("Daftarlar"), _("Ruchkalar"), _("Qalamlar"), _("Belgilar")]
    }
    return render(request, "intl/index.html", context)