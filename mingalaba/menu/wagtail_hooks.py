from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from mingalaba.menu.models import Category, Food


class CategoryViewSet(SnippetViewSet):
    model = Category
    ordering = ("name",)
    search_fields = ("name",)


class FoodViewSet(SnippetViewSet):
    model = Food
    list_display = ("name", "category", "price")
    list_filter = [
        "category",
    ]
    list_export = ("name", "category", "note", "description", "price")


class FoodMenuGroup(SnippetViewSetGroup):
    menu_label = "Food Menu"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        CategoryViewSet,
        FoodViewSet,
    )

register_snippet(FoodMenuGroup)