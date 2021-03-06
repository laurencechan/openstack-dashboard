from horizon import tables

from openstack_dashboard.dashboards.security.vm_loophole \
    import tables as project_tables

class MainIndexView(tables.DataTableView):
    table_class = project_tables.MainTable
    template_name = 'security/vm_loophole/main.html'
    page_title = "main page"

    def get_data(self):
        data = []
        return data