import random

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

# Create initial population
def create_initial_population(pop_size=10):
    population = []
    for _ in range(pop_size):
        outfit = {category: random.choice(items) for category, items in categories.items()}
        population.append(outfit)
    return population

# Fitness function
def fitness(outfit, dress_code, color_palette, budget, comfort_level):
    total_price = sum([outfit[cat]["Price"] for cat in outfit])
    avg_comfort = sum([outfit[cat]["Comfort"] for cat in outfit]) / len(outfit)
    
    # Check if the dress code and color palette match
    dress_code_match = sum([outfit[cat]["DressCode"] == dress_code for cat in outfit]) / len(outfit)
    color_match = sum([outfit[cat]["Color"] == color_palette for cat in outfit]) / len(outfit)

    # Calculate fitness score
    fitness_value = (dress_code_weight * dress_code_match + 
                     color_palette_weight * color_match + 
                     budget_weight * max(0, (budget - total_price) / budget) + 
                     comfort_weight * avg_comfort / 5)
    
    return fitness_value

# Binary tournament selection
def binary_tournament_selection(population, fitness_scores):
    def tournament():
        a, b = random.sample(list(fitness_scores.keys()), 2)
        return a if fitness_scores[a] > fitness_scores[b] else b
    
    return tournament(), tournament()

# Crossover (combine two outfits)
def crossover(parent1, parent2):
    child = {}
    for category in categories:
        child[category] = random.choice([parent1[category], parent2[category]])
    return child

# Mutation (randomly change one item)
def mutate(outfit):
    category = random.choice(list(categories.keys()))
    outfit[category] = random.choice(categories[category])

# Genetic Algorithm
def genetic_algorithm(dress_code, color_palette, budget, comfort_level, generations=100, pop_size=10):
    population = create_initial_population(pop_size)
    
    for generation in range(generations):
        fitness_scores = {i: fitness(population[i], dress_code, color_palette, budget, comfort_level) for i in range(len(population))}
        
        # Selection and reproduction
        new_population = []
        while len(new_population) < pop_size:
            parent1_idx, parent2_idx = binary_tournament_selection(population, fitness_scores)
            parent1 = population[parent1_idx]
            parent2 = population[parent2_idx]
            
            child = crossover(parent1, parent2)
            
            # Mutate occasionally
            if random.random() < 0.1:  # 10% mutation rate
                mutate(child)
            
            new_population.append(child)
        
        population = new_population

    # Calculate final fitness scores again using indices
    fitness_scores = {i: fitness(population[i], dress_code, color_palette, budget, comfort_level) for i in range(len(population))}
    best_outfit_idx = max(fitness_scores, key=fitness_scores.get)
    
    return population[best_outfit_idx], fitness_scores[best_outfit_idx]

# User interaction
def main():
    # Get user inputs
    dress_code = input("Enter the desired dress code (Casual, Sportswear, Business, Evening): ")
    color_palette = input("Enter the desired color palette (Dark, Bright): ")
    budget = float(input("Enter your budget (SAR): "))
    comfort_level = int(input("Enter the desired comfort level (1 to 5): "))

    # Run genetic algorithm
    best_outfit, score = genetic_algorithm(dress_code, color_palette, budget, comfort_level, generations=50, pop_size=20)
    
    # Output best outfit
    print("\nBest Outfit Recommendation:")
    for category, item in best_outfit.items():
        print(f"{category}: {item['Item']} (Price: {item['Price']} SAR, Dress Code: {item['DressCode']}, Color: {item['Color']}, Comfort: {item['Comfort']})")
    print(f"\nFitness Score: {score:.2f}")

if __name__ == "__main__":
    main()
