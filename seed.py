import asyncio
import random
from faker import Faker

from src.core.database import Database
from src.core.config import configs
from src.models.building import Building
from src.models.organization import Organization
from src.models.organization_phone import OrganizationPhone
from src.models.activity import Activity
from src.models.organization_activity import OrganizationActivity

fake = Faker()
db = Database(configs.DATABASE_ASYNC_URI)


async def clear_db(session):
    # Удаляем в порядке, не нарушающем FK
    for model in [
        OrganizationActivity,
        OrganizationPhone,
        Organization,
        Building,
        Activity
    ]:
        await session.exec(model.__table__.delete())
    await session.commit()


async def seed():
    session = db.get_session()

    # Очистка данных
    await clear_db(session)

    # Здания
    buildings = [
        Building(address=fake.address(), lat=fake.latitude(), lon=fake.longitude())
        for _ in range(10)
    ]
    session.add_all(buildings)
    await session.commit()
    await session.refresh(buildings[0])

    # Трёхуровневая структура активностей
    level1 = [
        Activity(name="Еда"),
        Activity(name="Автомобили")
    ]
    session.add_all(level1)
    await session.commit()

    level2 = [
        Activity(name="Молочная", parent_id=level1[0].id),
        Activity(name="Мясная", parent_id=level1[0].id),
        Activity(name="Грузовые", parent_id=level1[1].id),
        Activity(name="Легковые", parent_id=level1[1].id)
    ]
    session.add_all(level2)
    await session.commit()

    level3 = [
        Activity(name="Йогурты", parent_id=level2[0].id),
        Activity(name="Сыр", parent_id=level2[0].id),
        Activity(name="Колбасы", parent_id=level2[1].id),
        Activity(name="Стейки", parent_id=level2[1].id),
        Activity(name="Фуры", parent_id=level2[2].id),
        Activity(name="Пикапы", parent_id=level2[3].id),
    ]
    session.add_all(level3)
    await session.commit()

    all_activities = level1 + level2 + level3

    # Организации
    organizations = []
    for _ in range(15):
        org = Organization(
            name=fake.company(),
            building_id=random.choice(buildings).id
        )
        session.add(org)
        await session.flush()
        organizations.append(org)

        # телефоны
        phones = [OrganizationPhone(number=fake.phone_number(), organization_id=org.id) for _ in range(random.randint(1, 3))]
        session.add_all(phones)

        # связи с деятельностями
        acts = random.sample(all_activities, k=random.randint(1, 3))
        links = [OrganizationActivity(organization_id=org.id, activity_id=a.id) for a in acts]
        session.add_all(links)

    await session.commit()
    print("✔️ seed выполнен успешно")


if __name__ == "__main__":
    asyncio.run(seed())
