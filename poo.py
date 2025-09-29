"""
Sistema de Avaliação de Restaurantes (iFood)

Este módulo implementa um sistema completo para gerenciar avaliações de restaurantes.
Contém duas classes principais:
- Restaurant: Representa um restaurante individual com nome e avaliações
- RestaurantList: Gerencia uma coleção de restaurantes com operações estatísticas

Autor: Ronicarlos Ferreira 37012676
Data: 27/09/2025
"""

class Restaurant:
    """
    Classe que representa um restaurante com suas avaliações.
    
    Esta classe encapsula as informações de um restaurante, incluindo nome
    e lista de avaliações dos clientes.
    
    Attributes:
        name (str): Nome do restaurante
        ratings (list): Lista de notas dos clientes (0 a 10)
    """
    
    def __init__(self, name, ratings):
        """
        Inicializa um restaurante com nome e lista de avaliações.
        
        Args:
            name (str): Nome do restaurante
            ratings (list): Lista de notas dos clientes (0 a 10)
        """
        self.name = name
        self.ratings = ratings
    
    def calculate_average(self):
        """
        Calcula a média das avaliações do restaurante.
        
        Returns:
            float: Média das avaliações
        """
        if not self.ratings:
            return 0.0
        return sum(self.ratings) / len(self.ratings)
    
    def check_rating_status(self):
        """
        Verifica se o restaurante é bem ou mal avaliado.
        
        Returns:
            str: "Bem avaliado" se média >= 7.0, "Mal avaliado" caso contrário
        """
        average = self.calculate_average()
        if average >= 7.0:
            return "Bem avaliado"
        else:
            return "Mal avaliado"
    
    def __str__(self):
        """
        Retorna uma representação em string do restaurante.
        
        Returns:
            str: String formatada com as informações do restaurante
        """
        return f"Restaurante: {self.name} | Média: {self.calculate_average():.2f} | Avaliação: {self.check_rating_status()}"
    
    def __len__(self):
        """
        Retorna o número de avaliações do restaurante.
        
        Returns:
            int: Quantidade de avaliações
        """
        return len(self.ratings)
    
    def __getitem__(self, index):
        """
        Permite acesso às avaliações por índice usando notação de lista.
        
        Args:
            index (int): Índice da avaliação desejada
            
        Returns:
            float: A avaliação no índice especificado
        """
        return self.ratings[index]
    
    def __setitem__(self, index, rating):
        """
        Permite modificar avaliações por índice usando notação de lista.
        
        Args:
            index (int): Índice da avaliação a ser modificada
            rating (float): Nova avaliação para substituir a existente
        """
        self.ratings[index] = rating
    
    def __delitem__(self, index):
        """
        Permite remover avaliações por índice usando notação de lista.
        
        Args:
            index (int): Índice da avaliação a ser removida
        """
        del self.ratings[index]

class RestaurantList:
    """
    Classe que gerencia uma coleção de restaurantes.
    
    Esta classe implementa uma lista personalizada de restaurantes com métodos
    especiais para operações estatísticas e manipulação da lista.
    
    Attributes:
        restaurants (list): Lista contendo objetos da classe Restaurant
    """
    
    def __init__(self):
        """
        Inicializa uma nova lista de restaurantes vazia.
        """
        self.restaurants = []
    
    def add_restaurant(self, name, ratings):
        """
        Adiciona um novo restaurante à lista.
        
        Args:
            name (str): Nome do restaurante
            ratings (list): Lista de notas dos clientes
        """
        self.restaurants.append(Restaurant(name, ratings))
    
    def __str__(self):
        """
        Retorna uma representação em string da lista de restaurantes.
        
        Returns:
            str: String com todos os restaurantes, um por linha
        """
        return "\n".join(str(restaurant) for restaurant in self.restaurants)
    
    def __len__(self):
        """
        Retorna o número de restaurantes na lista.
        
        Returns:
            int: Quantidade de restaurantes na lista
        """
        return len(self.restaurants)
    
    def __getitem__(self, index):
        """
        Permite acesso aos restaurantes por índice usando notação de lista.
        
        Args:
            index (int): Índice do restaurante desejado
            
        Returns:
            Restaurant: O restaurante no índice especificado
        """
        return self.restaurants[index]
    
    def __setitem__(self, index, restaurant):
        """
        Permite modificar restaurantes por índice usando notação de lista.
        
        Args:
            index (int): Índice do restaurante a ser modificado
            restaurant (Restaurant): Novo restaurante para substituir o existente
        """
        self.restaurants[index] = restaurant
    
    def __delitem__(self, index):
        """
        Permite remover restaurantes por índice usando notação de lista.
        
        Args:
            index (int): Índice do restaurante a ser removido
        """
        del self.restaurants[index]
    
    def __total_average__(self):
        """
        Calcula a média geral de todas as avaliações de todos os restaurantes.
        
        Returns:
            float: Média geral de todas as avaliações
        """
        all_ratings = []
        for restaurant in self.restaurants:
            all_ratings.extend(restaurant.ratings)
        return sum(all_ratings) / len(all_ratings) if all_ratings else 0.0
    
    def __best_restaurant__(self):
        """
        Encontra o restaurante com maior média de avaliações.
        
        Returns:
            Restaurant: O restaurante com maior média
        """
        return max(self.restaurants, key=lambda x: x.calculate_average())
    
    def __worst_restaurant__(self):
        """
        Encontra o restaurante com menor média de avaliações.
        
        Returns:
            Restaurant: O restaurante com menor média
        """
        return min(self.restaurants, key=lambda x: x.calculate_average())
    
    def __well_rated_count__(self):
        """
        Conta quantos restaurantes são bem avaliados (média >= 7.0).
        
        Returns:
            int: Número de restaurantes bem avaliados
        """
        return sum(1 for restaurant in self.restaurants if restaurant.check_rating_status() == "Bem avaliado")
    
    def __poorly_rated_count__(self):
        """
        Conta quantos restaurantes são mal avaliados (média < 7.0).
        
        Returns:
            int: Número de restaurantes mal avaliados
        """
        return sum(1 for restaurant in self.restaurants if restaurant.check_rating_status() == "Mal avaliado")

# Main
if __name__ == "__main__":
    # Criando a lista de restaurantes
    restaurant_list = RestaurantList()
    restaurant_list.add_restaurant("Pizza Boa", [8, 9, 8, 9, 8])
    restaurant_list.add_restaurant("Lanche Popular", [6, 5, 7, 6, 6])
    restaurant_list.add_restaurant("Sushi Prime", [9, 10, 9, 8, 9])
    restaurant_list.add_restaurant("Burger King", [7, 8, 7, 8, 7])
    restaurant_list.add_restaurant("McDonald's", [5, 6, 5, 4, 6])

    # Exibindo os restaurantes
    print("🍔 SISTEMA DE AVALIAÇÃO DE RESTAURANTES (iFOOD)")
    print("=" * 50)
    
    for restaurant in restaurant_list:
        print(f"Restaurante: {restaurant.name}")
        print(f"Média: {restaurant.calculate_average():.2f}")
        print(f"Avaliação: {restaurant.check_rating_status()}")
        print("-" * 20)
    
    # Exibindo o resumo das avaliações
    print("\n")
    print("-" * 5 + "  Resumo das Avaliações  " + "-" * 5)
    print(f"Média geral: {restaurant_list.__total_average__():.2f}")
    print(f"Total bem avaliados: {restaurant_list.__well_rated_count__()}")
    print(f"Total mal avaliados: {restaurant_list.__poorly_rated_count__()}")
    print(f"Melhor restaurante: {restaurant_list.__best_restaurant__().name} (Média: {restaurant_list.__best_restaurant__().calculate_average():.2f})")
    print(f"Pior restaurante: {restaurant_list.__worst_restaurant__().name} (Média: {restaurant_list.__worst_restaurant__().calculate_average():.2f})")
    print("-" * 30 + "\n")
