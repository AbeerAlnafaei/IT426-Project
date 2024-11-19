import random
import matplotlib.pyplot as plt # type: ignore

# Define the full search space (all items included) 
categories = {
    "Top": [
        {"Item": "T-shirt", "Price": 0.0, "DressCode": "Casual", "Color": "Bright", "Comfort": 5},
        {"Item": "Formal Shirt", "Price": 120.0, "DressCode": "Business", "Color": "Dark", "Comfort": 3},
        {"Item": "Polo Shirt", "Price": 80.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 4},
        {"Item": "Evening Blouse", "Price": 150.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 3},
        {"Item": "Sweater", "Price": 0.0, "DressCode": "Casual", "Color": "Dark", "Comfort": 5},
        {"Item": "Hoodie", "Price": 60.0, "DressCode": "Casual", "Color": "Bright", "Comfort": 4},
        {"Item": "Tank Top", "Price": 0.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 4},
        {"Item": "Silk Blouse", "Price": 200.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 3},
    ],
    "Bottom": [
        {"Item": "Jeans", "Price": 0.0, "DressCode": "Casual", "Color": "Dark", "Comfort": 4},
        {"Item": "Formal Trousers", "Price": 150.0, "DressCode": "Business", "Color": "Dark", "Comfort": 3},
        {"Item": "Sports Shorts", "Price": 0.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 5},
        {"Item": "Skirt", "Price": 100.0, "DressCode": "Evening", "Color": "Bright", "Comfort": 3},
        {"Item": "Chinos", "Price": 90.0, "DressCode": "Business", "Color": "Dark", "Comfort": 4},
        {"Item": "Leggings", "Price": 60.0, "DressCode": "Casual", "Color": "Dark", "Comfort": 5},
        {"Item": "Athletic Pants", "Price": 80.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 5},
        {"Item": "Evening Gown Bottom", "Price": 250.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 1},
    ],
    "Shoes": [
        {"Item": "Sneakers", "Price": 0.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 5},
        {"Item": "Leather Shoes", "Price": 180.0, "DressCode": "Business", "Color": "Dark", "Comfort": 2},
        {"Item": "Running Shoes", "Price": 120.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 5},
        {"Item": "Ballet Flats", "Price": 90.0, "DressCode": "Casual", "Color": "Dark", "Comfort": 4},
        {"Item": "High Heels", "Price": 250.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 2},
        {"Item": "Sandals", "Price": 0.0, "DressCode": "Casual", "Color": "Bright", "Comfort": 5},
        {"Item": "Loafers", "Price": 150.0, "DressCode": "Business", "Color": "Dark", "Comfort": 3},
        {"Item": "Evening Pumps", "Price": 220.0, "DressCode": "Evening", "Color": "Bright", "Comfort": 2},
    ],
    "Neck": [
        {"Item": "Silk Scarf", "Price": 70.0, "DressCode": "Business", "Color": "Dark", "Comfort": 3},
        {"Item": "Sports Scarf", "Price": 0.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 4},
        {"Item": "Necklace", "Price": 220.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 3},
        {"Item": "Casual Scarf", "Price": 0.0, "DressCode": "Casual", "Color": "Bright", "Comfort": 5},
        {"Item": "Bow Tie", "Price": 80.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 3},
        {"Item": "Athletic Headband", "Price": 50.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 5},
        {"Item": "Diamond Necklace", "Price": 750.0, "DressCode": "Evening", "Color": "Bright", "Comfort": 3},
        {"Item": "Choker", "Price": 0.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 4},
    ],
    "Purse": [
        {"Item": "Clutch Bag", "Price": 100.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 3},
        {"Item": "Canvas Bag", "Price": 0.0, "DressCode": "Casual", "Color": "Bright", "Comfort": 5},
        {"Item": "Leather Briefcase", "Price": 180.0, "DressCode": "Business", "Color": "Dark", "Comfort": 1},
        {"Item": "Sports Backpack", "Price": 80.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 5},
        {"Item": "Tote Bag", "Price": 0.0, "DressCode": "Casual", "Color": "Bright", "Comfort": 4},
        {"Item": "Wristlet", "Price": 150.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 3},
        {"Item": "Fanny Pack", "Price": 50.0, "DressCode": "Sportswear", "Color": "Bright", "Comfort": 4},
        {"Item": "Elegant Handbag", "Price": 250.0, "DressCode": "Evening", "Color": "Dark", "Comfort": 3},
    ]
}

# Fitness weights
dress_code_weight = 0.4
budget_weight = 0.4
color_palette_weight = 0.1
comfort_weight = 0.1


def create_initial_population(pop_size=10, budget=0):
    population = []
    found_outfits = 0  # Counter for successfully found outfits

    while found_outfits < pop_size:
        # Generate a random outfit
        outfit = {category: random.choice(items) for category, items in categories.items()}

        # Calculate total price of the outfit
        total_price = sum([outfit[cat]["Price"] for cat in outfit])

        # If the outfit is within the budget, add it to the population
        if total_price <= budget:
            population.append(outfit)
            found_outfits += 1  

    return population


def fitness(outfit, dress_code, color_palette, budget, comfort_level):
    total_price = sum([outfit[cat]["Price"] for cat in outfit])

    # Check if comfort of each item is equal to or greater than comfort_level
    comfort_match = sum([1 if outfit[cat]["Comfort"] >= comfort_level else 0 for cat in outfit])
    avg_comfort = comfort_match / len(outfit)  

    dress_code_match = sum([outfit[cat]["DressCode"] == dress_code for cat in outfit]) / len(outfit)
    color_match = sum([outfit[cat]["Color"] == color_palette for cat in outfit]) / len(outfit)

    # Handle budget to avoid division by zero
    if budget > 0:
        budget_component = max(0, (budget - total_price) / budget)
    else:
        # if budget 0
        budget_component = 0

    # Calculate fitness score using weighted criteria
    fitness_value = (
        dress_code_weight * dress_code_match + 
        color_palette_weight * color_match + 
        budget_weight * budget_component + 
        comfort_weight * avg_comfort
    )
    
    return fitness_value

# Binary tournament selection
def binary_tournament_selection(population, fitness_scores):
    def tournament():
        a, b = random.sample(list(fitness_scores.keys()), 2)
        return a if fitness_scores[a] > fitness_scores[b] else b
    
    return tournament(), tournament()

# Function to check if outfit is valid within the budget
def valid_outfit(outfit, budget):
    total_price = sum([outfit[cat]["Price"] for cat in outfit])
    return total_price <= budget

#phase 1

# Crossover (combine two outfits) with budget check
 
#def crossover(parent1, parent2, budget):
   # child = {}
   # for category in categories:
     #   child[category] = random.choice([parent1[category], parent2[category]])
    
    # Ensure the child outfit is within the budget
  #  while not valid_outfit(child, budget):
  #      child = {category: random.choice([parent1[category], parent2[category]]) for category in categories}
    
  #  return child


#phase 2
# 2-Point Crossover (combine two outfits)
def two_point_crossover(parent1, parent2, budget):
    # Get the list of categories
    categories_list = list(categories.keys())
    
    # Select two random points for crossover
    point1, point2 = sorted(random.sample(range(len(categories_list)), 2))
    
    # Create child by combining segments from both parents
    child = {}
    for i, category in enumerate(categories_list):
        if point1 <= i <= point2:
            child[category] = parent2[category]
        else:
            child[category] = parent1[category]
    
    # Ensure the child outfit is within the budget
    while not valid_outfit(child, budget):
        point1, point2 = sorted(random.sample(range(len(categories_list)), 2))
        for i, category in enumerate(categories_list):
            if point1 <= i <= point2:
                child[category] = parent2[category]
            else:
                child[category] = parent1[category]

    return child


        # Mutation (randomly change one item) with budget check
def mutate(outfit, budget):
    # Select a random category
    category = random.choice(list(categories.keys()))
    # Randomly select a new item from that category
    new_item = random.choice(categories[category])
    
    # Replace the item in the outfit
    outfit[category] = new_item
    
    # Ensure the mutated outfit is within the budget
    while not valid_outfit(outfit, budget):
        category = random.choice(list(categories.keys()))
        new_item = random.choice(categories[category])
        outfit[category] = new_item


def replacement(old_population, new_population, dress_code, color_palette, budget, comfort_level):

    # Combine old and new populations
    combined_population = old_population + new_population
    
    # Evaluate fitness for all individuals
    combined_fitness = {i: fitness(individual, dress_code, color_palette, budget, comfort_level)
                        for i, individual in enumerate(combined_population)}
    
    # Sort by fitness in descending order
    sorted_indices = sorted(combined_fitness, key=combined_fitness.get, reverse=True)
    
    # Select the top individuals to form the next generation
    next_generation = [combined_population[i] for i in sorted_indices[:len(old_population)]]
    
    return next_generation


# Genetic Algorithm with 2-point crossover and mutation
def genetic_algorithm(dress_code, color_palette, budget, comfort_level, pop_size=10):
    generations = 20
    
    # Step 0: Initialize the population
    population = create_initial_population(pop_size, budget)
    
    for generation in range(generations):
        # Step 1: Calculate fitness for each individual in the population
        fitness_scores = {i: fitness(population[i], dress_code, color_palette, budget, comfort_level) 
                          for i in range(len(population))}
        
        # Step 2: Selection and crossover to generate new offspring
        new_population = []
        while len(new_population) < pop_size:
            # Select parents using binary tournament selection
            parent1_idx, parent2_idx = binary_tournament_selection(population, fitness_scores)
            parent1 = population[parent1_idx]
            parent2 = population[parent2_idx]
            
            # Perform 2-point crossover to create a child
            child = two_point_crossover(parent1, parent2, budget)
            
            # Apply mutation with a probability of 10%
            if random.random() < 0.1:  # 10% mutation rate
                mutate(child, budget)
            
            # Add the child to the new population
            new_population.append(child)
        
        # Step 3: Replace the old population with the new one using the replacement strategy
        population = replacement(population, new_population, dress_code, color_palette, budget, comfort_level)
    
    # Step 4: After all generations, calculate the final fitness of the population
    fitness_scores = {i: fitness(population[i], dress_code, color_palette, budget, comfort_level) 
                      for i in range(len(population))}
    
    # Step 5: Return the best outfit and its fitness score
    best_outfit_idx = max(fitness_scores, key=fitness_scores.get)
    return population[best_outfit_idx], fitness_scores[best_outfit_idx]





def main():

    userName = input("Welcome to PerfectFit! What is your name?\n")
    print(f"\nHi {userName}, please provide your preferences:")
    

    dress_code = input("\nPlease enter your dress code preference (Casual, Sportswear, Business, Evening):\n")
    color_palette = input("\nPlease enter your color palette preference (Dark, Bright):\n")
    comfort_level = int(input("\nPlease enter your comfort level (1 (least comfortable) to 5 (most comfortable)):\n"))
    budget = float(input("\nPlease enter your budget (in SAR):\n"))
    

    best_outfit, score = genetic_algorithm(dress_code, color_palette, budget, comfort_level, pop_size=10)
    

    print("\nWe are working on preparing your optimal outfit...\n")
    print("\nYour outfit selection is ready! Here's your personalized outfit plan:\n")
    

    categories_in_order = ["Top", "Bottom", "Shoes", "Neck", "Purse"]
    for i, category in enumerate(categories_in_order, 1):
        if category in best_outfit:  
            item = best_outfit[category]
            print(f" {category}: {item['Item']}")

    
    print("\nHope you feel fabulous in your outfit!")
    # Number of generations and population size
    generations = 20
    population_size = 10

    # Initialize variables for tracking performance
    avg_fitness_per_generation = []

    # Run the genetic algorithm
    population = create_initial_population(population_size, budget)
    best_fitness_overall = 0
    best_outfit_overall = None

    for generation in range(generations):
        fitness_scores = {i: fitness(population[i], dress_code, color_palette, budget, comfort_level) 
                          for i in range(len(population))}

        # Store average fitness for the current generation
        avg_fitness = sum(fitness_scores.values()) / len(fitness_scores)
        avg_fitness_per_generation.append(avg_fitness)

        # Check for the best individual in the generation
        best_fitness_in_generation = max(fitness_scores.values())
        if best_fitness_in_generation > best_fitness_overall:
            best_fitness_overall = best_fitness_in_generation
            best_outfit_overall = population[max(fitness_scores, key=fitness_scores.get)]

        # Termination condition: If no significant improvement
        if generation > 0 and abs(avg_fitness_per_generation[-1] - avg_fitness_per_generation[-2]) < 0.001:
            print("\nConvergence detected. Terminating early.")
            break

        # Selection, crossover, mutation, and replacement
        new_population = []
        while len(new_population) < population_size:
            parent1_idx, parent2_idx = binary_tournament_selection(population, fitness_scores)
            parent1 = population[parent1_idx]
            parent2 = population[parent2_idx]
            child = two_point_crossover(parent1, parent2, budget)
            if random.random() < 0.1:  # Mutation probability
                mutate(child, budget)
            new_population.append(child)

        population = replacement(population, new_population, dress_code, color_palette, budget, comfort_level)

    # Display the best outfit and its fitness score
    print(f"\nBest outfit: {best_outfit_overall}")
    print(f"Best fitness score: {best_fitness_overall}")

    # Plot the graph of fitness over generations
    plt.plot(avg_fitness_per_generation, label="Average Fitness")
    plt.title("GA Performance: Generation vs Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    main()



