class Films:
    def __init__(self, film_name, prod_name, profits, language):
        self.film_name = film_name
        self.prod_name = prod_name
        self.profits = profits
        self.language = language


class FilmCollections:
    def __init__(self, film_ls):
        self.film_ls = film_ls

    def Method1(self, profit_val):
        return ''.join([i.film_name for i in self.film_ls if i.language.lower() == 'english' and int(i.profits[1:-7]) > profit_val])


if __name__ == '__main__':
    film_ls = [Films(input(), input(), input(), input())
               for _ in range(int(input()))]
    profit_val = int(input())

    film_coll_obj = FilmCollections(film_ls)

    if film_coll_obj.Method1(profit_val):
        print(film_coll_obj.Method1(profit_val))
    else:
        print('No record found')
