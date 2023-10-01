from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        response_assert = f"Esse restaurante se chama Mamma Mia and serve comida italiana.\nEsse restaturante está servindo 0 consumidores desde que está aberto."

        response = restaurant.describe_restaurant()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_open_restaurant_closed(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        restaurant.open = False
        response_assert = 'Mamma Mia agora está aberto!'

        response = restaurant.open_restaurant()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_open_restaurant_open(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        restaurant.open = True
        response_assert = 'Mamma Mia já está aberto!'

        response = restaurant.open_restaurant()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_close_restaurant_open(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        restaurant.open = True
        response_assert = 'Mamma Mia agora está fechado!'

        response = restaurant.close_restaurant()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_close_restaurant_closed(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        restaurant.open = False
        response_assert = 'Mamma Mia já está fechado!'

        response = restaurant.close_restaurant()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_set_number_served_open(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        restaurant.open = True
        response_assert = 10

        response = restaurant.set_number_served(10)

        assert response_assert == response, 'Retorno do código difere do número de clientes atendidos esperado.'

    def test_set_number_served_closed(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        restaurant.open = False
        response_assert = 'Mamma Mia está fechado!'

        response = restaurant.set_number_served(10)

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_increment_number_served_positive(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        restaurant.open = True
        response_assert = 1

        response = restaurant.increment_number_served(1)

        assert response_assert == response, 'Retorno do código difere do número de clientes atendidos esperado.'

    def test_increment_number_served_negative(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        restaurant.open = True
        response_assert = 'Numero invalido'

        response = restaurant.increment_number_served(-1)

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_increment_number_served_closed(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        restaurant.open = False
        response_assert = 'Mamma Mia está fechado!'

        response = restaurant.increment_number_served(1)

        assert response_assert == response, 'Retorno do código difere do número de clientes atendidos esperado.'
