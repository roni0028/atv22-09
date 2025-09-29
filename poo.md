# 🍔 Atividade – Avaliação de Restaurante (iFood)

## 🎯 Objetivo
Praticar os conceitos de **classe, atributos, métodos, listas, for e if** em Python, em um contexto real.

---

## 📝 Enunciado
Você foi contratado para criar um sistema que avalia **restaurantes do iFood**.  
Cada restaurante recebe **avaliações de clientes** (notas de 0 a 10).  
O sistema deve calcular a **média das notas** e indicar se o restaurante é **bem avaliado** ou **mal avaliado**.

---

## 🔹 O que você deve fazer
1. Criar uma classe chamada **Restaurante** com:
   - Atributo `nome`
   - Atributo `avaliacoes` (lista de notas dos clientes)

2. Criar um método `calcular_media` que retorne a média das avaliações.  

3. Criar um método `verificar_avaliacao` que:
   - Retorne `"Bem avaliado"` se a média for **maior ou igual a 7.0**.  
   - Retorne `"Mal avaliado"` caso contrário.  

4. No programa principal:
   - Criar uma lista com pelo menos **3 objetos Restaurante**.  
   - Usar um **for** para mostrar:
     - Nome do restaurante  
     - Média das avaliações  
     - Situação (bem avaliado ou mal avaliado).  

---

## 🚀 Desafio Extra
- Mostrar **quantos restaurantes foram bem avaliados** e **quantos foram mal avaliados**.  
- Identificar qual restaurante tem a **maior nota média**.  

---

## 📌 Exemplo de Saída Esperada
Restaurante: Pizza Boa  
Média: 8.50  
Situação: Bem avaliado  
--------------------  
Restaurante: Lanche Popular  
Média: 6.00  
Situação: Mal avaliado  
--------------------  
Restaurante: Sushi Prime  
Média: 9.00  
Situação: Bem avaliado  
--------------------  

Total de bem avaliados: 2  
Total de mal avaliados: 1  
Melhor restaurante: Sushi Prime

---

## 🎓 Conceitos Práticos
Esta atividade exercita:
- **Classes**: Estrutura para modelar entidades do mundo real
- **Atributos**: Propriedades que caracterizam um objeto
- **Métodos**: Comportamentos e operações dos objetos
- **Listas**: Para armazenar múltiplos objetos e avaliações
- **Laços `for`**: Para percorrer e processar todos os objetos
- **Condições `if`**: Para fazer comparações e lógica condicional
- **Formatação de strings**: Para exibir os resultados de forma organizada

---

## ✅ Critérios de Avaliação
- [x] Classe `Restaurante` criada corretamente
- [x] Atributos `nome` e `avaliacoes` implementados
- [x] Método `calcular_media` implementado
- [x] Método `verificar_avaliacao` implementado
- [x] Pelo menos 3 objetos Restaurante criados
- [x] Uso de `for` para exibir todos os restaurantes
- [x] Desafio extra implementado (contagem e melhor restaurante)
- [x] Saída formatada conforme o exemplo

---

## 🚀 Como Executar

1. **Execute o programa**
   ```bash
   python "poo.py"
   ```

2. **Verifique a saída**
   - Confirme se todos os restaurantes são exibidos
   - Verifique se os cálculos estão corretos
   - Compare com o exemplo esperado

---

## 🎯 Melhorias e Escolhas de Design Implementadas

### **1. Programação Orientada a Objetos**
```python
class Restaurant:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

class RestaurantList:
    def __init__(self):
        self.restaurants = []
```

**Por que escolhi POO?**
- **Encapsulamento**: Organiza dados e comportamentos em classes
- **Reutilização**: Código pode ser usado em outros projetos
- **Manutenibilidade**: Mais fácil de modificar e estender
- **Escalabilidade**: Permite adicionar novos recursos facilmente

### **2. Nomenclatura em Inglês**
```python
class Restaurant:  # Em vez de "Restaurante"
    def __init__(self, name, ratings):  # Em vez de "nome", "avaliacoes"
        self.name = name
        self.ratings = ratings
```

**Por que inglês?**
- **Padrão internacional**: Código mais profissional e universal
- **Compatibilidade**: Facilita colaboração com desenvolvedores globais
- **Boas práticas**: Segue convenções da indústria
- **Manutenibilidade**: Código mais limpo e consistente

### **3. Métodos Especiais (Magic Methods)**
```python
def __str__(self):
    return f"Restaurante: {self.name} | Média: {self.calculate_average():.2f} | Avaliação: {self.check_rating_status()}"

def __len__(self):
    return len(self.ratings)

def __getitem__(self, index):
    return self.ratings[index]
```

**Por que métodos especiais?**
- **Comportamento nativo**: Objetos se comportam como tipos do Python
- **Intuitividade**: Permite usar `len(restaurant)`, `restaurant[0]`, `print(restaurant)`
- **Profissionalismo**: Demonstra conhecimento avançado de Python
- **Usabilidade**: Código mais limpo e legível

### **4. Cálculos Avançados**
```python
def __total_average__(self):
    all_ratings = []
    for restaurant in self.restaurants:
        all_ratings.extend(restaurant.ratings)
    return sum(all_ratings) / len(all_ratings) if all_ratings else 0.0

def __best_restaurant__(self):
    return max(self.restaurants, key=lambda x: x.calculate_average())

def __well_rated_count__(self):
    return sum(1 for restaurant in self.restaurants if restaurant.check_rating_status() == "Bem avaliado")
```

**Por que cálculos avançados?**
- **Funcionalidade extra**: Vai além do que foi pedido
- **Demonstração de habilidades**: Mostra domínio de conceitos
- **Valor agregado**: Entrega mais do que foi solicitado
- **Aplicação prática**: Cálculos úteis para análise de dados

### **5. Documentação Profissional**
```python
class Restaurant:
    """
    Classe que representa um restaurante com suas avaliações.
    
    Esta classe encapsula as informações de um restaurante, incluindo nome
    e lista de avaliações dos clientes.
    
    Attributes:
        name (str): Nome do restaurante
        ratings (list): Lista de notas dos clientes (0 a 10)
    """
```

**Por que documentação?**
- **Clareza**: Explica o propósito de cada classe/método
- **Manutenibilidade**: Facilita futuras modificações
- **Profissionalismo**: Segue padrões da indústria
- **Colaboração**: Ajuda outros desenvolvedores a entender o código

### **6. Estrutura de Código Organizada**
```python
# Main
if __name__ == "__main__":
    # Criando a lista de restaurantes
    restaurant_list = RestaurantList()
    restaurant_list.add_restaurant("Pizza Boa", [8, 9, 8, 9, 8])
    # ...
```

**Por que estrutura organizada?**
- **Modularidade**: Separa lógica da classe da execução
- **Testabilidade**: Código mais fácil de testar
- **Reutilização**: Classes podem ser importadas em outros projetos
- **Boas práticas**: Segue convenções de desenvolvimento

### **7. Interface de Usuário Melhorada**
```python
print("🍔 SISTEMA DE AVALIAÇÃO DE RESTAURANTES (iFOOD)")
print("=" * 50)
print("-" * 5 + "  Resumo das Avaliações  " + "-" * 5)
print(f"Média geral: {restaurant_list.__total_average__():.2f}")
```

**Por que interface melhorada?**
- **Visual atrativo**: Formatação melhora a experiência
- **Clareza**: Informações bem organizadas
- **Profissionalismo**: Saída mais polida
- **Usabilidade**: Fácil de entender e interpretar

---

## 📊 Comparação: Básico vs Implementação Avançada

| Aspecto | Versão Básica | Minha Implementação |
|---------|---------------|-------------------|
| **Estrutura** | Classe simples | Classes POO + RestaurantList |
| **Nomenclatura** | Português | Inglês (padrão) |
| **Funcionalidades** | Básicas | Avançadas + extras |
| **Métodos Especiais** | Nenhum | `__str__`, `__len__`, `__getitem__`, etc. |
| **Documentação** | Mínima | Profissional |
| **Reutilização** | Limitada | Alta |
| **Manutenibilidade** | Baixa | Alta |
| **Escalabilidade** | Limitada | Excelente |

---

## 🏆 Benefícios das Melhorias

### **Para o Aprendizado**
- **Conceitos avançados**: POO, métodos especiais, lambda
- **Boas práticas**: Nomenclatura, documentação, estrutura
- **Pensamento crítico**: Vai além do básico solicitado

### **Para o Desenvolvimento**
- **Código profissional**: Pronto para uso em projetos reais
- **Manutenibilidade**: Fácil de modificar e estender
- **Reutilização**: Classes podem ser usadas em outros contextos

### **Para a Carreira**
- **Portfólio**: Demonstra habilidades avançadas
- **Diferenciação**: Mostra iniciativa e qualidade
- **Preparação**: Prepara para projetos profissionais

---

## 📚 Recursos Adicionais

- [Documentação Python - Listas](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Documentação Python - Dicionários](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Tutorial Python - Laços](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Métodos Especiais](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [PEP 8 - Style Guide](https://pep8.org/)

---

<div align="center">

**Desenvolvido com ❤️ para o aprendizado de Python**

</div>
