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

# Crossover (combine two outfits) with budget check
def crossover(parent1, parent2, budget):
    child = {}
    for category in categories:
        child[category] = random.choice([parent1[category], parent2[category]])
    
    # Ensure the child outfit is within the budget
    while not valid_outfit(child, budget):
        child = {category: random.choice([parent1[category], parent2[category]]) for category in categories}
    
    return child

# Mutation (randomly change one item) with budget check
def mutate(outfit, budget):
    category = random.choice(list(categories.keys()))
    new_item = random.choice(categories[category])
    outfit[category] = new_item
    
    # Ensure the mutated outfit is within the budget
    while not valid_outfit(outfit, budget):
        category = random.choice(list(categories.keys()))
        new_item = random.choice(categories[category])
        outfit[category] = new_item

# Genetic Algorithm
def genetic_algorithm(dress_code, color_palette, budget, comfort_level, generations=50, pop_size=10):
    population = create_initial_population(pop_size, budget)
    
    for generation in range(generations):
        fitness_scores = {i: fitness(population[i], dress_code, color_palette, budget, comfort_level) for i in range(len(population))}
        
        # Selection 
        new_population = []
        while len(new_population) < pop_size:
            parent1_idx, parent2_idx = binary_tournament_selection(population, fitness_scores)
            parent1 = population[parent1_idx]
            parent2 = population[parent2_idx]
            
            child = crossover(parent1, parent2, budget)
            
            # Mutate 
            if random.random() < 0.1:  # 10% mutation rate
                mutate(child , budget)
            
            new_population.append(child)
        
        population = new_population

    # Calculate final fitness scores again using indices
    fitness_scores = {i: fitness(population[i], dress_code, color_palette, budget, comfort_level) for i in range(len(population))}
    best_outfit_idx = max(fitness_scores, key=fitness_scores.get)
    
    return population[best_outfit_idx], fitness_scores[best_outfit_idx]


def main():

    userName = input("Welcome to PerfectFit! What is your name?\n")
    print(f"\nHi {userName}, please provide your preferences:")
    

    dress_code = input("\nPlease enter your dress code preference (Casual, Sportswear, Business, Evening):\n")
    color_palette = input("\nPlease enter your color palette preference (Dark, Bright):\n")
    comfort_level = int(input("\nPlease enter your comfort level (1 (least comfortable) to 5 (most comfortable)):\n"))
    budget = float(input("\nPlease enter your budget (in SAR):\n"))
    

    best_outfit, score = genetic_algorithm(dress_code, color_palette, budget, comfort_level, generations=50, pop_size=10)
    

    print("\nWe are working on preparing your optimal outfit...\n")
    print("\nYour outfit selection is ready! Here's your personalized outfit plan:\n")
    

    categories_in_order = ["Top", "Bottom", "Shoes", "Neck", "Purse"]
    for i, category in enumerate(categories_in_order, 1):
        if category in best_outfit:  
            item = best_outfit[category]
            print(f" {category}: {item['Item']}")

    
    print("\nHope you feel fabulous in your outfit!")



if __name__ == "__main__":
    main()



