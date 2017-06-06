from django.core.urlresolvers import reverse_lazy
from menu import Menu
from apps.main.menus import ViewMenuItem

# --- Publicación --- #
publi_children = (
    ViewMenuItem(
        "Crear Publicación",
        reverse_lazy("create_post"),
        weight=30,
        icon="fa-bookmark"),
     ViewMenuItem(
        "Editar Publicación",
        reverse_lazy("view_private_post"),
        weight=20,
        icon="fa-terminal "),
    ViewMenuItem(
        "Vista de Usuarios",
        reverse_lazy("view_post"),
        weight=10,
        icon="fa-bookmark-o"),
    )

Menu.add_item(
    "user",
    ViewMenuItem(
        "Publicaciones",
        reverse_lazy('view_post'),
        weight=100,
        icon="fa-book",
        group="u_valle",
        children=publi_children))
