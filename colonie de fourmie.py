import random

# Définition du graphe représentant la carte routière
graph = {
    'A': {'B': 2, 'C': 4, 'D': 7},
    'B': {'A': 2, 'C': 1, 'D': 5},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'A': 7, 'B': 5, 'C': 3}
}

# Définition des paramètres de l'algorithme génétique
population_size = 10
mutation_rate = 0.1
num_generations = 20

# Génération d'une population initiale aléatoire
def generate_individual():
    return random.sample(graph.keys(), len(graph))

population = [generate_individual() for _ in range(population_size)]

# Calcul de la distance totale d'un individu
def calculate_distance(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        current_node = individual[i]
        next_node = individual[i+1]
        total_distance += graph[current_node][next_node]
    return total_distance

# Sélection des individus les plus performants
def selection(population):
    sorted_population = sorted(population, key=lambda x: calculate_distance(x))
    return sorted_population[:population_size // 2]

# Croisement de deux individus pour créer un nouvel individu
def crossover(parent1, parent2):
    child = []
    gene1, gene2 = random.sample(range(len(parent1)), 2)
    start_gene = min(gene1, gene2)
    end_gene = max(gene1, gene2)
    child.extend(parent1[start_gene:end_gene])
    child.extend([gene for gene in parent2 if gene not in child])
    return child

# Mutation d'un individu en échangeant deux gènes
def mutate(individual):
    gene1, gene2 = random.sample(range(len(individual)), 2)
    individual[gene1], individual[gene2] = individual[gene2], individual[gene1]
    return individual

# Boucle principale de l'algorithme génétique
for generation in range(num_generations):
    # Sélection des individus les plus performants
    selected_population = selection(population)

    # Croisement pour créer une nouvelle population
    new_population = []
    while len(new_population) < population_size:
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        child = crossover(parent1, parent2)
        new_population.append(child)

    # Mutation de certains individus de la nouvelle population
    for i in range(len(new_population)):
        if random.random() < mutation_rate:
            new_population[i] = mutate(new_population[i])

    # Remplacement de l'ancienne population par la nouvelle
    population = new_population

# Sélection du meilleur individu de la population finale
best_individual = min(population, key=lambda x: calculate_distance(x))
best_distance = calculate_distance(best_individual)

# Affichage du résultat
print("Meilleur individu :", best_individual)
print("Distance minimale :", best_distance)
