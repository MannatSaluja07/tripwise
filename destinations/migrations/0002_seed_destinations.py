from django.db import migrations


SAMPLE_DESTINATIONS = [
    {
        "name": "Santorini",
        "country": "Greece",
        "description": "Whitewashed cliffside villages overlooking the Aegean Sea, famous for their sunsets.",
        "image_url": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=800",
        "price_per_night": 145.00,
        "rating": 4.8,
    },
    {
        "name": "Kyoto",
        "country": "Japan",
        "description": "Ancient temples, bamboo forests, and traditional tea houses in Japan's former capital.",
        "image_url": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800",
        "price_per_night": 98.00,
        "rating": 4.9,
    },
    {
        "name": "Banff",
        "country": "Canada",
        "description": "Turquoise glacial lakes surrounded by the peaks of the Canadian Rockies.",
        "image_url": "https://images.unsplash.com/photo-1609825488888-3a766db05542?w=800",
        "price_per_night": 120.00,
        "rating": 4.7,
    },
    {
        "name": "Lisbon",
        "country": "Portugal",
        "description": "Pastel-colored streets, historic trams, and river views along the Tagus.",
        "image_url": "https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=800",
        "price_per_night": 75.00,
        "rating": 4.6,
    },
]


def seed_destinations(apps, schema_editor):
    Destination = apps.get_model('destinations', 'Destination')
    for entry in SAMPLE_DESTINATIONS:
        Destination.objects.create(**entry)


def remove_seeded_destinations(apps, schema_editor):
    Destination = apps.get_model('destinations', 'Destination')
    names = [d["name"] for d in SAMPLE_DESTINATIONS]
    Destination.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_destinations, remove_seeded_destinations),
    ]
