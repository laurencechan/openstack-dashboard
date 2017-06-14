from horizon import tables

from openstack_dashboard.dashboards.statistics.resource_pool \
    import tables as project_tables


class MainIndexView(tables.DataTableView):
    from openstack_dashboard.dashboards.main.main.views import MainIndexView
    MainIndexView.get_data(request=None, context={}, hypervisor_stats_count={}, instance_stats_count={})
    table_class = project_tables.MainTable
    template_name = 'statistics/resource_pool/main.html'
    page_title = "main page"

    def get_data(self):
        data = []
        return data
