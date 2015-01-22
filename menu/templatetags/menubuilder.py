from menu.models import Menu, MenuItem
from django import template
from django.core.cache import cache

register = template.Library()

def build_menu(parser, token):
    """
    {% menu menu_name %}
    """
    try:
        tag_name, menu_name = token.split_contents()
    except:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]
    return MenuObject(menu_name)

class MenuObject(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        current_path = context['request'].path
        user = context['request'].user
        context['menuitems'] = get_items(self.menu_name, current_path, user)
        return ''


def load_menu(current_path, i, menu, user):
    current = ( i.link_url != '/' and current_path.startswith(i.link_url)) or (
    i.link_url == '/' and current_path == '/' )
    if menu.base_url and i.link_url == menu.base_url and current_path != i.link_url:
        current = False
    show_anonymous = i.anonymous_only and user.is_anonymous()
    show_auth = i.login_required and user.is_authenticated()
    if (not (i.login_required or i.anonymous_only)) or (i.login_required and show_auth) or (i.anonymous_only and show_anonymous):
        menuitem = {'url': i.link_url, 'title': i.title, 'current': current, 'image': i.image, 'submenu': []}
        if i.submenu:
            for j in MenuItem.objects.filter(menu=i.submenu).order_by('order'):
                inner = load_menu(current_path, j, i.submenu, user)
                if inner:
                    menuitem['submenu'].append(inner)
        return menuitem
    else:
        return None





def get_items(menu_name, current_path, user):
    """
    If possible, use a cached list of items to avoid continually re-querying 
    the database.
    The key contains the menu name, whether the user is authenticated, and the current path.
    Disable caching by setting MENU_CACHE_TIME to -1.
    """
    from django.conf import settings
    cache_time = getattr(settings, 'MENU_CACHE_TIME', 1800)
    debug = getattr(settings, 'DEBUG', False)

    if cache_time >= 0 and not debug:
        cache_key = 'django-menu-items/%s/%s/%s'  % (menu_name, current_path, user.is_authenticated())
        menuitems = cache.get(cache_key, [])
        if menuitems:
            return menuitems
    else:
        menuitems = []
        
    try:
        menu = Menu.objects.get(slug=menu_name, enabled=True)
    except Menu.DoesNotExist:
        return []

    for i in MenuItem.objects.filter(menu=menu, enabled=True).order_by('order'):
        menuitem = load_menu(current_path, i, menu, user)
        if menuitem:
            menuitems.append(menuitem)

    if cache_time >= 0 and not debug:
        cache.set(cache_key, menuitems, cache_time)
    return menuitems

register.tag('menu', build_menu)

