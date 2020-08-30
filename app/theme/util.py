from wagtail.contrib.modeladmin.helpers import AdminURLHelper


class CustomURLHelper(AdminURLHelper):
    # New functionality and exising method overrides added here

    def get_action_url(self, action):
        return "/admin/settings/theme/header/2/"
        # return header_istance.url_helper.get_action_url('edit', 2)
