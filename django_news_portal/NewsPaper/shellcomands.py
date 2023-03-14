python manage.py shell

from NewsPaper.models inport *

user1 = User.objects.create_user(username='Пушкин')
user2 = User.objects.create_user(username='Есенин')

Author.objects.create(author_user=user1)
Author.objects.create(author_user=user2)

Category.objects.create(category_name="Спорт")
Category.objects.create(category_name="Экономика")
Category.objects.create(category_name="Проишествия")
Category.objects.create(category_name="Достижения")

Post.objects.create(post_author='Пушкин',post_type='NW', post_header="Газмяс - Чемпион", post_text=(
    Никто не ожидал и вот опять победа))

Post.objects.create(post_author='Пушкин',post_type='AR', post_header="Как накормить мир", post_text=(
    "раздаем всем удочки")

Post.objects.create(post_author='Есенин',post_type='AR', post_header="Кошка спасла пожарного", post_text=(
    "мур мур мур мяу мяу мур")