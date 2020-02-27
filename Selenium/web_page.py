class WebPage():
    def __init__(self):
        self.url = None
        self.title = None
        self.author = 'Лев Толстой'
        self.language = 'ru'

    def print_WebPage(self):
        param_list = []
        param_list.append(str(self.url))
        param_list.append(str(self.title))
        param_list.append(str(self.author))
        param_list.append(str(self.language))
        return (', '.join(param_list))

def print_webpage():
    print(main_page.print_WebPage())
    print(posts_page.print_WebPage())
    print(search_page.print_WebPage())
    print(music_page.print_WebPage())
    print(friends_page.print_WebPage())

main_page = WebPage()
main_page.url = 'http://127.0.0.1:8000/'
main_page.title = 'Главная'

posts_page = WebPage()
posts_page.url = 'http://127.0.0.1:8000/posts/'
posts_page.title = 'Мои посты'

search_page = WebPage()
search_page.url = 'http://127.0.0.1:8000/search/'
search_page.title = 'Страница поиска'

music_page = WebPage()
music_page.url = 'http://127.0.0.1:8000/music/'
music_page.title = 'Моя музыка'

friends_page = WebPage()
friends_page.url = 'http://127.0.0.1:8000/friends/'
friends_page.title = 'Мои друзья'

print_webpage()

