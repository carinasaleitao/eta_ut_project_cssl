from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available_existent_stock(self):
        icecreamstand = IceCreamStand('Mamma Mia', 'comida italiana', ['limao', 'pistache', 'tiramisu'])
        response_assert = 'No momento temos os seguintes sabores de sorvete disponíveis:\t-limao,\tpistache,\t-tiramisu'

        response = icecreamstand.flavors_available()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_flavors_available_out_of_stock(self):
        icecreamstand = IceCreamStand('Mamma Mia', 'comida italiana', [])
        response_assert = 'Estamos sem estoque atualmente!'

        response = icecreamstand.flavors_available()

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_find_flavor_existent_flavor(self):
        icecreamstand = IceCreamStand('Mamma Mia', 'comida italiana', ['limao', 'pistache', 'tiramisu'])
        response_assert = 'Temos no momento limao!'

        response = icecreamstand.find_flavor('limao')

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_find_flavor_nonexistent_flavor(self):
        icecreamstand = IceCreamStand('Mamma Mia', 'comida italiana', ['limao', 'pistache', 'tiramisu'])
        response_assert = 'Não temos no momento baunilha!'

        response = icecreamstand.find_flavor('baunilha')

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_find_flavor_nonexistent_stock(self):
        icecreamstand = IceCreamStand('Mamma Mia', 'comida italiana', [])
        response_assert = 'Estamos sem estoque atualmente!'

        response = icecreamstand.find_flavor('limao')

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_add_flavor_existent_flavor(self):
        icecreamstand = IceCreamStand('Mamma Mia', 'comida italiana', ['limao', 'pistache', 'tiramisu'])
        response_assert = 'Sabor já disponivel!'

        response = icecreamstand.find_flavor('limao')

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_add_flavor_nonexistent_flavor(self):
        icecreamstand = IceCreamStand('Mamma Mia', 'comida italiana', ['limao', 'pistache', 'tiramisu'])
        response_assert = 'Baunilha adicionado ao estoque!'

        response = icecreamstand.find_flavor('baunilha')

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'

    def test_add_flavor_nonexistent_stock(self):
        icecreamstand = IceCreamStand('Mamma Mia', 'comida italiana', [])
        response_assert = 'Estamos sem estoque atualmente!'

        response = icecreamstand.find_flavor('limao')

        assert response_assert == response, 'Retorno do código difere da mensagem esperada.'
