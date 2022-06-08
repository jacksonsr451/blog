from rolepermissions.roles import AbstractUserRole


class Usuario(AbstractUserRole):
    available_permissions = {
        'view_blog': True,
        'view_comments': True,
        'add_comments': True,
    }

class Editor(AbstractUserRole):
    available_permissions = {
        'view_blog': True,
        'edit_blog': True,
        'view_comments': True,
        'delete_comments': True,
        'add_comments': True,
    }

class Administrador(AbstractUserRole):
    available_permissions = {
        'view_blog': True,
        'edit_blog': True,
        'delete_blog': True,
        'add_blog': True,
        'view_users': True,
        'edit_users': True,
        'delete_users': True,
        'add_users': True,
        'add_editor': True,
        'edit_editor': True,
        'delete_editor': True,
        'view_roles': True,
        'edit_roles': True,
        'delete_roles': True,
        'add_roles': True,
        'view_permissions': True,
        'edit_permissions': True,
        'delete_permissions': True,
        'add_permissions': True,
        'view_comments': True,
        'delete_comments': True,
        'add_comments': True,
    }
    
class Invitado(AbstractUserRole):
    available_permissions = {
        'view_blog': True,
        'view_comments': False,
        'add_comments': False,
    }
    
class Banido(AbstractUserRole):
    available_permissions = {
        'view_blog': False,
        'view_comments': False,
        'add_comments': False,
    }
    
class Eliminado(AbstractUserRole):
    available_permissions = {
        'view_blog': True,
        'view_comments': False,
        'add_comments': False,
    }
