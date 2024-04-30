"""
Реалізуйте скрипт для пошуку цитат за тегом, за ім'ям автора або набором тегів.
Скрипт виконується в нескінченному циклі і за допомогою звичайного оператора
input приймає команди у наступному форматі команда: значення.
Приклад:
name: Steve Martin — знайти та повернути список всіх цитат автора Steve Martin;

tag:life — знайти та повернути список цитат для тега life;
tags:life,live — знайти та повернути список цитат, де є теги life або live
(примітка: без пробілів між тегами life, live);
exit — завершити виконання скрипту.

Виведення результатів пошуку лише у форматі utf-8
"""
from models import Quote, Author


def search_quotes(criteria):
    if criteria.startswith("name:"):
        author_name = criteria.split(":")[1].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            return quotes
        else:
            return None
    elif criteria.startswith("tag:"):
        tag = criteria.split(":")[1].strip()
        quotes = Quote.objects(tags=tag)
        return quotes
    elif criteria.startswith("tags:"):
        tags = criteria.split(":")[1].strip().split(",")
        quotes = Quote.objects(tags__in=tags)
        return quotes
    elif criteria == "exit":
        exit()
    else:
        print("Invalid command. Please try again.")


if __name__ == "__main__":
    while True:
        command = input("Enter tag or name, for example 'tag:life' or 'name:Albert Einstein': ")
        quotes = search_quotes(command)
        if quotes:
            for quote in quotes:
                print(f'{quote.quote.encode("utf-8").decode()} - {quote.author.fullname.encode("utf-8").decode()}')
        else:
            print("No quotes found.")
