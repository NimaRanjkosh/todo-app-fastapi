from core.database import SessionLocal
from users.models import UserModel
from tasks.models import TaskModel
from faker import Faker
from random import randint

fake = Faker()


def seed_users(db):
    user = UserModel(username=fake.user_name())
    user.set_password(fake.password())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def seed_tasks(db, user_info, count=10):
    tasks_list = []
    for _ in range(count):
        tasks_list.append(
            TaskModel(
                title=fake.sentence(nb_words=10),
                description=fake.text(),
                status_id=randint(1, 2),
                is_completed=fake.boolean(),
                user_id=user_info.id,
            )
        )
    db.add_all(tasks_list)
    db.commit()
    print(f"Added {count} tasks for user_id: {user_info.id}")


def main():
    db = SessionLocal()
    try:
        user = seed_users(db=db)
        seed_tasks(db, user_info=user)
    finally:
        db.close()


if __name__ == "__main__":
    main()
