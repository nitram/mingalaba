from wagtail import hooks
from wagtail.admin.userbar import AccessibilityItem

from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from mingalaba.base.models import *


class CustomAccessibilityItem(AccessibilityItem):
    axe_run_only = None


@hooks.register("construct_wagtail_userbar")
def replace_userbar_accessibility_item(request, items):
    items[:] = [
        CustomAccessibilityItem() if isinstance(item, AccessibilityItem) else item
        for item in items
    ]


class LogoViewSet(SnippetViewSet):
    model = Logo


class PhoneViewSet(SnippetViewSet):
    model = Phone


class AddressViewSet(SnippetViewSet):
    model = Address

    
class HoursViewSet(SnippetViewSet):
    model = Hours


class SocialsViewSet(SnippetViewSet):
    model = Socials


class BrandViewSetGroup(SnippetViewSetGroup):
    menu_label = "Brand Info"
    menu_order = 300
    items = (
        LogoViewSet,
        PhoneViewSet,
        AddressViewSet,
        HoursViewSet,
        SocialsViewSet
    )


register_snippet(BrandViewSetGroup)