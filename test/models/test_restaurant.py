from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        self.number_served = 10
        self.open = True

        response_assert = "Esse restaurante se chama Mamma Mia and serve comida italiana.\nEsse restaturante está servindo 10 consumidores desde que está aberto."

        response = restaurant.describe_restaurant()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_open_restaurant_closed(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        self.open = False
        response_assert = 'Mamma Mia agora está aberto!'

        response = restaurant.open_restaurant()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_close_restaurant_open(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        self.open = True
        response_assert = 'Mamma Mia já está aberto!'

        response = restaurant.open_restaurant()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_set_number_served_open(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        self.open = True
        response_assert = 10

        response = restaurant.set_number_served(10)

        assert response_assert == response, 'Retorno do código difere do número de clientes atendidos esperado.'

    def test_set_number_served_closed(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        self.open = False
        response_assert = 'Mamma Mia está fechado!'

        response = restaurant.set_number_served(10)

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_increment_number_served_positive(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        self.number_served = 0
        response_assert = 1

        response = restaurant.increment_number_served(1)

        assert response_assert == response, 'Retorno do código difere do número de clientes atendidos esperado.'

    def test_increment_number_served_negative(self):
        restaurant = Restaurant('mamma mia', 'comida italiana')
        self.number_served = 0
        response_assert = 'Numero invalido'

        response = restaurant.increment_number_served(-1),

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'
