from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.utils.translation import gettext_lazy as _
from pascal.club_and_cell.forms import ClubCellForm
from pascal.club_and_cell.models import ClubCell


class ClubCellListView(LoginRequiredMixin,ListView):
    model = ClubCell
    template_name = "club_and_cell/club_and_cell_list.html"
    context_object_name = "clubs_and_cells"
    queryset = ClubCell.objects.filter(is_active=True)


class ClubCellView(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = ClubCell
    form_class = ClubCellForm
    template_name = "club_and_cell/club_and_cell_create_form.html"
    success_message = _("Club or Cell added successfully.")
    success_url = "/club-cells/all-clubs-and-cells"
