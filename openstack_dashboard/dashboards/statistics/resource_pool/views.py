from horizon import tables

from openstack_dashboard.dashboards.statistics.resource_pool \
    import tables as project_tables


class MainIndexView(tables.DataTableView):
    table_class = project_tables.MainTable
    template_name = 'statistics/resource_pool/main.html'
    page_title = "main page"

    def get_data(self):
        data = []
        return data
