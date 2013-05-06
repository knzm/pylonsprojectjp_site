def includeme(config):
    config.add_route('admin_dashboard', '/')
    config.add_route('admin_index', '/{model}/')
    config.add_route('admin_entry', '/{model}/{id:\d+}')
    config.add_route('admin_new', '/{model}/{id:\d+};new')
    config.add_route('admin_edit', '/{model}/{id:\d+};edit')
