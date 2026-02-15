from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ManageRooms",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("roomname", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, max_length=200)),
                ("create_room", models.BooleanField(default=False)),
                ("book_room", models.BooleanField(default=False)),
            ],
        ),
    ]
