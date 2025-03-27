# DELETE THIS FILE

# This file is causing issues because the ventas app doesn't have any migrations yet.
# You cannot create a migration that depends on 'XXXX_initial' when there are no
# existing migrations in the app.

# Instead, you should:
# 1. Delete this file
# 2. Create initial migrations for the ventas app with:
#    python manage.py makemigrations ventas

# After that, if the Usuario model was in your models.py but has now been removed,
# Django will automatically create a proper migration to remove it.
