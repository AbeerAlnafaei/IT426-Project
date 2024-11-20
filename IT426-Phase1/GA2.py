import random

import matplotlib.pyplot as plt  # type: ignore

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

def create_initial_population(pop_size, budget):
    population = []
    for _ in range(pop_size):
        while True:  # Keep generating outfits until the total price is within the budget
            outfit = {category: random.choice(items) for category, items in categories.items()}
            total_price = sum(outfit[cat]["Price"] for cat in outfit)
            if total_price <= budget:
                population.append(outfit)
                break
    return population


def fitness(outfit, dress_code, color_palette, budget, comfort_level):
    # Normalize total price to a scale of [0, 1] relative to the budget
    total_price = sum(outfit[cat]["Price"] for cat in outfit)
    if budget >= total_price:
        budget_component = 1
    else:
        
        budget_component = 0
    # Components
    comfort_component = sum(1 if outfit[cat]["Comfort"] >= comfort_level else 0 for cat in outfit) / len(outfit)
    dress_code_match = sum(1 if outfit[cat]["DressCode"] == dress_code else 0 for cat in outfit) / len(outfit)
    color_match = sum(1 if outfit[cat]["Color"] == color_palette else 0 for cat in outfit) / len(outfit)
    
    # Weighted fitness
    fitness_value = (
        dress_code_weight * dress_code_match +
        color_palette_weight * color_match +
        budget_weight * budget_component +
        comfort_weight * comfort_component
    )

    return fitness_value

# Binary tournament selection
def binary_tournament_selection(population, fitness_scores):
    def tournament():
        a, b = random.sample(list(fitness_scores.keys()), 2)
        return a if fitness_scores[a] > fitness_scores[b] else b
    
    return tournament(), tournament()


#phase 2
# 2-Point Crossover (combine two outfits)

def two_point_crossover(parent1, parent2, budget):
    categories_list = list(categories.keys())
    
    while True:  # Repeat until a valid child is produced
        # Select two random points for crossover
        point1, point2 = sorted(random.sample(range(len(categories_list)), 2))
        
        # Create child by combining segments from both parents
        child = {}
        for i, category in enumerate(categories_list):
            if point1 <= i <= point2:
                child[category] = parent2[category]
            else:
                child[category] = parent1[category]
        
        # Check if the child's total price is within the budget
        total_price = sum(child[cat]["Price"] for cat in child)
        if total_price <= budget:
            return child


        # Mutation (randomly change one item) with budget check
def mutate(outfit, budget):
    while True:  # Keep mutating until the resulting outfit respects the budget
        category = random.choice(list(categories.keys()))
        new_item = random.choice(categories[category])
        outfit[category] = new_item
        total_price = sum(outfit[cat]["Price"] for cat in outfit)
        if total_price <= budget:
            break


def replacement(old_population, new_population, dress_code, color_palette, budget, comfort_level):
    # Combine old and new populations
    combined_population = old_population + new_population

    # Evaluate fitness for all individuals
    combined_fitness = {
        i: fitness(individual, dress_code, color_palette, budget, comfort_level)
        for i, individual in enumerate(combined_population)
    }

    # Sort by fitness in descending order
    sorted_indices = sorted(combined_fitness, key=combined_fitness.get, reverse=True)

    # Select the top individuals to form the next generation
    next_generation = []
    for idx in sorted_indices:
        individual = combined_population[idx]
        total_price = sum(individual[cat]["Price"] for cat in individual)

        # Only add individuals that satisfy the budget constraint
        if total_price <= budget:
            next_generation.append(individual)

        # Stop once the next generation is filled
        if len(next_generation) == len(old_population):
            break

    # If for any reason we don't fill the population, regenerate missing individuals
    while len(next_generation) < len(old_population):
        next_generation.append(
            {category: random.choice(items) for category, items in categories.items()}
        )

    return next_generation


# Genetic Algorithm with 2-point crossover and mutation
def genetic_algorithm(dress_code, color_palette, budget, comfort_level, pop_size=10, generations=20):
    optimal_solution = 1.0  # The ideal fitness is normalized to 1.0
    tolerance = 1e-8  # Error tolerance for termination
    avg_fitness_per_generation = []  # Track average fitness for each generation

    # Initialize the population with respect to the budget
    population = create_initial_population(pop_size, budget)

    for generation in range(generations):
        # Step 1: Calculate fitness for the population
        fitness_scores = {i: fitness(population[i], dress_code, color_palette, budget, comfort_level)
                          for i in range(len(population))}

        # Track average fitness for plotting
        avg_fitness = sum(fitness_scores.values()) / len(fitness_scores)
        avg_fitness_per_generation.append(avg_fitness)

        # Termination condition based on best fitness
        best_fitness_in_generation = max(fitness_scores.values())
        if abs(optimal_solution - best_fitness_in_generation) < tolerance:
            print(f"Termination condition met at generation {generation}. Best fitness: {best_fitness_in_generation}")
            break

        # Step 2: Selection and crossover to create a new population
        new_population = []
        while len(new_population) < pop_size:
            parent1_idx, parent2_idx = binary_tournament_selection(population, fitness_scores)
            parent1 = population[parent1_idx]
            parent2 = population[parent2_idx]
            child = two_point_crossover(parent1, parent2, budget)  # Pass budget constraint to crossover

            # Apply mutation
            if random.random() < 0.1:  # 10% mutation probability
                mutate(child, budget)

            # Add the child to the new population
            new_population.append(child)

        # Step 3: Replace the old population with the new population
        population = replacement(population, new_population, dress_code, color_palette, budget, comfort_level)

    # Final evaluation after evolution completes
    fitness_scores = {i: fitness(population[i], dress_code, color_palette, budget, comfort_level)
                      for i in range(len(population))}
    best_outfit_idx = max(fitness_scores, key=fitness_scores.get)
    return population[best_outfit_idx], fitness_scores[best_outfit_idx], avg_fitness_per_generation


def run_ga_20_times(dress_code, color_palette, budget, comfort_level, pop_size=10, generations=20):
    runs = 20
    avg_fitness_per_run = []  # Collect average fitness per generation for plotting
    best_fitness_per_run = []  # Store the best fitness of each run
    best_outfits_per_run = []  # Store the best outfit of each run

    for run in range(runs):
        print(f"Running GA for trial {run + 1}...")
        best_outfit, best_fitness, avg_fitness_per_generation = genetic_algorithm(
            dress_code, color_palette, budget, comfort_level, pop_size, generations
        )
        avg_fitness_per_run.append(avg_fitness_per_generation)
        best_fitness_per_run.append(best_fitness)
        best_outfits_per_run.append(best_outfit)

    return avg_fitness_per_run, best_fitness_per_run, best_outfits_per_run

def plot_fitness(avg_fitness_per_run):
    # Calculate the average fitness over generations across all runs
    avg_fitness_over_generations = [sum(gen) / len(gen) for gen in zip(*avg_fitness_per_run)]
    plt.plot(avg_fitness_over_generations, label="Average Fitness Over 20 Runs")
    plt.title("GA Performance: Generation vs Average Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to PerfectFit!")
    user_name = input("\nEnter your name: ")
    print(f"\nHi {user_name}, let's create the perfect outfit for you!")

    # Get user inputs
    dress_code = input("\nEnter your dress code preference (Casual, Sportswear, Business, Evening): ")
    color_palette = input("\nEnter your color palette preference (Dark, Bright): ")
    comfort_level = int(input("\nEnter your comfort level (1 (least comfortable) to 5 (most comfortable)): "))
    budget = float(input("\nEnter your budget (in SAR): "))

    print("\nRunning the Genetic Algorithm 20 times...\n")
    avg_fitness_per_run, best_fitness_per_run, best_outfits_per_run = run_ga_20_times(
        dress_code, color_palette, budget, comfort_level)

    # Analyze results
    print("\nResults of 20 Runs:")
    for i in range(20):
        print(f"Run {i + 1}:")
        print(f"  Best Fitness: {best_fitness_per_run[i]:.4f}")
        print(f"  Best Outfit:")
        for category, item in best_outfits_per_run[i].items():
            print(f"    {category}: {item['Item']} (Price: {item['Price']},DressCode: {item['DressCode']},Color: {item['Color']}, Comfort: {item['Comfort']})")
        print()

    # Plot the average fitness across generations
    print("\nPlotting the performance graph...\n")
    plot_fitness(avg_fitness_per_run)

    print("\nThank you for using PerfectFit!")
if __name__ == "__main__":
    main()
