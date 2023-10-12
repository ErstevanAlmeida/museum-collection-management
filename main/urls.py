from django.urls import path
from main.views import show_main, create_collection, show_xml, show_json, show_xml_by_id
from main.views import show_json_by_id, register, login_user, logout_user, edit_collection
from main.views import delete_collection, get_collection_json, add_collection_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-new-collection', create_collection, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('edit-collection/<int:id>', edit_collection, name="edit_collection"),
    path('delete-collection/<int:id>', delete_collection, name='delete_collection'),
    path('get-collection/', get_collection_json, name='get_collection_json'),
    path('create-new-collection-ajax/', add_collection_ajax, name='add_collection_ajax'),
]