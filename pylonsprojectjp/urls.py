def includeme(config):
    settings = config.registry.settings
    static_assets = settings.get("pylonsprojectjp.static_assets", "pylonsprojectjp:static")

    # static urls
    config.add_static_view("static", static_assets, cache_max_age=3600)
    config.add_asset_views(static_assets, "robots.txt", http_cache=3600)
    config.add_asset_views(static_assets, "favicon.ico", http_cache=3600)

    # per-app urls
    config.include('.apps.page.urls')
    config.include('.apps.top.urls')
    config.include('.apps.auth.urls')
    config.include('.apps.admin.urls', route_prefix='/admin')
    config.include('.apps.blog.urls', route_prefix='/news')
