from django.db import migrations

class Migration(migrations.Migration):
    """
    This is a proper migration class to fix the BadMigrationError.
    Initially we wanted to delete this file, but since it's still present,
    we're making it a valid empty migration instead.
    """
    # We need a proper dependency - if there are no migrations yet, 
    # make this the initial migration
    dependencies = [('ventas', '0001_initial')]

    operations = [
        # Empty operations - this is just a placeholder migration
        # that won't affect the database
    ]
