# Парсер для инстаграма

Бот ставит лайки от вашего аккаунта. Будет лайкать все посты другого аккаунта, или все посты по хештегу

Скрипт можно запустить используя переменные окружения. 

Например: login=YOUR_LOGIN password=YOUR_PASSWORD request=YOUR_REQ python3 instabot.py

В файле instabot.py вызвана функция press_likes(). В параметры метода пихаем логин, пароль и запрос(аккаутнт или хештег)

Далее запускаем файл

В pages.py прописаны методы клацания кнопок в браузере и тд.

Иногда летит исключение связанные с непрогрузкой страницы, в этом случае просто перезапустите скрипт.
