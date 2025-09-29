# 🛍️ Atividade – Lista de Compras no Supermercado

## 🎯 Objetivo
Praticar os conceitos de **listas, dicionários, laços (`for`) e condições (`if`)** em Python, em um contexto do dia a dia.

---

## 📝 Enunciado Original
Você vai criar um programa que organiza uma **lista de compras** do supermercado.  
Cada item deve conter:  
- Nome do produto  
- Quantidade  
- Preço unitário  

O sistema deve mostrar todos os itens comprados e gerar um **resumo da compra**.

---

## 🔹 O que você deve fazer
1. Criar uma lista chamada `compras`, onde cada item será um **dicionário** com as informações do produto.  
2. Adicionar pelo menos **5 itens diferentes** na lista.  
3. Usar um **for** para mostrar todos os itens no formato:  

   Produto: Arroz | Quantidade: 2 | Preço: R$ 20.00
 

4. Calcular o **total gasto** percorrendo a lista com um `for`.  
5. Usar `if` dentro de um laço `for` para descobrir:  
- O produto mais caro  
- O produto com maior quantidade  

---

## 💡 Dicas de uso de `for` e `if`
- Use o **for** para percorrer todos os itens da lista e exibir as informações.  
- Use o **for** também para calcular o **total gasto**.  
- Use o **if** para comparar valores e descobrir qual é o **produto mais caro** e qual tem a **maior quantidade**.  

---

## 📌 Exemplo de Saída Esperada

   Produto: Arroz | Quantidade: 2 | Preço: R$ 20.00
   Produto: Feijão | Quantidade: 1 | Preço: R$ 8.00
   Produto: Leite | Quantidade: 3 | Preço: R$ 5.00
   Produto: Pão | Quantidade: 10 | Preço: R$ 0.50
   Produto: Café | Quantidade: 1 | Preço: R$ 12.00

   Resumo da Compra:
   Total de itens diferentes: 5
   Total gasto: R$ 61.00
   Produto mais caro: Arroz (R$ 20.00)
   Produto com maior quantidade: Pão (10 unidades)

---

## 🎓 Conceitos Práticos
Esta atividade exercita:
- **Listas**: Estrutura para armazenar múltiplos itens
- **Dicionários**: Estrutura para organizar informações de cada produto
- **Laços `for`**: Para percorrer e processar todos os itens
- **Condições `if`**: Para fazer comparações e encontrar extremos
- **Formatação de strings**: Para exibir os resultados de forma organizada

---

## ✅ Critérios de Avaliação
- [x] Lista `compras` criada corretamente
- [x] Pelo menos 5 itens adicionados
- [x] Cada item é um dicionário com nome, quantidade e preço
- [x] Uso de `for` para exibir todos os itens
- [x] Cálculo do total gasto implementado
- [x] Identificação do produto mais caro
- [x] Identificação do produto com maior quantidade
- [x] Saída formatada conforme o exemplo

---

## 🚀 Como Executar

1. **Execute o programa**
   ```bash
   python "estrutura de dados.py"
   ```

2. **Verifique a saída**
   - Confirme se todos os itens são exibidos
   - Verifique se os cálculos estão corretos
   - Compare com o exemplo esperado

---

## 🎯 Melhorias e Escolhas de Design Implementadas

### **1. Programação Orientada a Objetos**
```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ProductList:
    def __init__(self):
        self.products = []
```

**Por que escolhi POO?**
- **Encapsulamento**: Organiza dados e comportamentos em classes
- **Reutilização**: Código pode ser usado em outros projetos
- **Manutenibilidade**: Mais fácil de modificar e estender
- **Escalabilidade**: Permite adicionar novos recursos facilmente

### **2. Nomenclatura em Inglês**
```python
class Product:  # Em vez de "Produto"
    def __init__(self, name, price, quantity):  # Em vez de "nome", "preco", "quantidade"
        self.name = name
        self.price = price
        self.quantity = quantity
```

**Por que inglês?**
- **Padrão internacional**: Código mais profissional e universal
- **Compatibilidade**: Facilita colaboração com desenvolvedores globais
- **Boas práticas**: Segue convenções da indústria
- **Manutenibilidade**: Código mais limpo e consistente

### **3. Métodos Especiais (Magic Methods)**
```python
def __str__(self):
    return f"Produto: {self.name}, Preço: {self.price}, Quantidade: {self.quantity}"

def __len__(self):
    return len(self.products)

def __getitem__(self, index):
    return self.products[index]
```

**Por que métodos especiais?**
- **Comportamento nativo**: Objetos se comportam como tipos do Python
- **Intuitividade**: Permite usar `len(lista)`, `lista[0]`, `print(lista)`
- **Profissionalismo**: Demonstra conhecimento avançado de Python
- **Usabilidade**: Código mais limpo e legível

### **4. Cálculos Avançados**
```python
def __total__(self):
    return sum(product.price * product.quantity for product in self.products)

def __media__(self):
    return self.__total__() / len(self.products)

def __maior_valor__(self):
    return max(self.products, key=lambda x: x.price)
```

**Por que cálculos avançados?**
- **Funcionalidade extra**: Vai além do que foi pedido
- **Demonstração de habilidades**: Mostra domínio de conceitos
- **Valor agregado**: Entrega mais do que foi solicitado
- **Aplicação prática**: Cálculos úteis para análise de dados

### **5. Documentação Profissional**
```python
class Product:
    """
    Classe que representa um produto com suas características básicas.
    
    Esta classe encapsula as informações de um produto, incluindo nome,
    preço e quantidade disponível.
    
    Attributes:
        name (str): Nome do produto
        price (float): Preço unitário do produto
        quantity (int): Quantidade disponível do produto
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
    # Criando a lista de produtos
    product_list = ProductList()
    product_list.add_product("Arroz", 10.0, 10)
    # ...
```

**Por que estrutura organizada?**
- **Modularidade**: Separa lógica da classe da execução
- **Testabilidade**: Código mais fácil de testar
- **Reutilização**: Classes podem ser importadas em outros projetos
- **Boas práticas**: Segue convenções de desenvolvimento

### **7. Interface de Usuário Melhorada**
```python
print("-" * 5 + "  Resumo da Compra  " + "-" * 5)
print(f"Total: {product_list.__total__():.2f}")
print(f"Média: {product_list.__media__():.2f}")
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
| **Estrutura** | Lista de dicionários | Classes POO |
| **Nomenclatura** | Português | Inglês (padrão) |
| **Funcionalidades** | Básicas | Avançadas + extras |
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
