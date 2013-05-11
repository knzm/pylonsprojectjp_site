def includeme(config):
    factory = 'pylonsprojectjp.apps.admin.resources.AdminRootContext'
    config.add_route('admin_dashboard', '/', factory=factory)
    config.add_route('admin_index', '/{model}/', factory=factory)
    config.add_route('admin_entry', '/{model}/{id:\d+}', factory=factory)
    config.add_route('admin_new', '/{model}/new', factory=factory)
    config.add_route('admin_edit', '/{model}/{id:\d+};edit', factory=factory)
