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

Post.objects.get(id=1).post_category.add(Category.objects.get(id=1, 4)
Post.objects.get(id=2).post_category.add(Category.objects.get(id=2, 3, 4)
Post.objects.get(id=2).post_category.add(Category.objects.get(id=3, 4)

Comment.objects.create(com_post=Post.objects.get(id=1), com_author=Author.objects.get(id=2), com_text="Ура, болел за Газмяс!")
Comment.objects.create(com_post=Post.objects.get(id=2), com_author=Author.objects.get(id=2), com_text="Готов на рыбалку хоть завтра")
Comment.objects.create(com_post=Post.objects.get(id=3), com_author=Author.objects.get(id=1), com_text="Обожаю котиков")
Comment.objects.create(com_post=Post.objects.get(id=2), com_author=Author.objects.get(id=1), com_text="Жду вас завтра у одинокой ивы")

Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).dislike()
Post.objects.get(id=3).dislike()
Post.objects.get(id=3).dislike()

Comment.objects.get(id=1).like()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=4).dislike()

a = Author.objects.get(id=1)
a.update_rating()

b = Author.objects.get(id=2)
b.update_rating()




