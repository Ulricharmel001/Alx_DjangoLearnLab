# Permissions and Groups Setup

- Model `Book` has custom permissions: can_view, can_create, can_edit, can_delete.
- Three groups are created:
    - Editors: can_edit, can_create
    - Viewers: can_view
    - Admins: can_view, can_edit, can_delete
- Views are protected with @permission_required decorator to enforce permissions.
- Assign users to appropriate groups to control their access rights.
# Permissions and Groups Setup

- Model `Book` has custom permissions: can_view, can_create, can_edit, can_delete.
- Three groups are created:
    - Editors: can_edit, can_create
    - Viewers: can_view
    - Admins: can_view, can_edit, can_delete
- Views are protected with @permission_required decorator to enforce permissions.
- Assign users to appropriate groups to control their access rights.
