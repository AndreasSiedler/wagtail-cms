from wagtail.contrib.modeladmin.helpers import AdminURLHelper
from django.urls import reverse
from django.shortcuts import redirect

class CustomURLHelper(AdminURLHelper):
    # New functionality and exising method overrides added here

    def get_action_url(self, action):
        return redirect("/admin/theme/appearance/edit/1/")
        # return header_istance.url_helper.get_action_url('edit', 2)
