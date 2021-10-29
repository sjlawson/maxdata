from faker import Faker
from faker_music import MusicProvider
from faker.providers import person, internet

faker = Faker(locale="en_US")
faker.add_provider(person)
faker.add_provider(internet)
faker.add_provider(MusicProvider)
