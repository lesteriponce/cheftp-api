from wagtail import hooks
from wagtail.admin.menu import MenuItem

@hooks.register('register_admin_menu_item')
def register_api_docs_menu_item():
    return MenuItem(
        'API Docs',
        '/api/docs/',
        icon_name='code',
        order=10000
    )
