from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima.

        Alteração: print -> return
        """
        if self.flavors:
            message = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                message = message + f"\t-{flavor}"
            return message
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível.

        Alteração: print -> return
        Bugfix: Temos no momento {self.flavors}! -> Temos no momento {flavor}!
        Bugfix: Não temos no momento {self.flavors}! -> Não temos no momento {flavor}!
        """
        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento {flavor}!"
            else:
                return f"Não temos no momento {flavor}!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque.

        Alteração: print -> return
        Bugfix: "{flavor} adicionado ao estoque!" -> {flavor.title()} adicionado ao estoque!"
        """
        if self.flavors:
            if flavor in self.flavors:
                return f"\nSabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return f"{flavor.title()} adicionado ao estoque!"
        else:
            return "Estamos sem estoque atualmente!"
