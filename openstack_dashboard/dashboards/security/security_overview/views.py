from horizon import tables

from openstack_dashboard.dashboards.security.security_overview \
    import tables as project_tables

class MainIndexView(tables.DataTableView):
    table_class = project_tables.MainTable
    template_name = 'security/security_overview/main.html'
    page_title = "main page"

    def get_data(self):
        data = []
        return data