class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante.

        Alteração: print -> return
        BugFix: Esse restaturante chama {self.cuisine_type} -> Esse restaurante se chama {self.restaurant_name}
        """
        return f"Esse restaurante se chama {self.restaurant_name} and serve {self.cuisine_type}.\nEsse restaturante está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios.

        Alteração: print -> return
        BugFix: self.open = False -> self.open = True
        BugFix: self.number_served = -2 -> self.number_served = 0
        """
        if not self.open:
            self.open = True
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"

        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios.

        Alteração: print -> return
        """
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento.

        Alteração: print -> return
        """
        if self.open:
            self.number_served = total_customers
            return self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante.

        Alteração: print -> return
        Refactor: inclusão de validação para números negativos
        """
        if more_customers < 0:
            return 'Numero invalido'

        if self.open:
            self.number_served = more_customers
            return self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"
