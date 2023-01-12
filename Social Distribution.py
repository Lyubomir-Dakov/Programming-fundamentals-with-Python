population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())

if sum(population) / len(population) < minimum_wealth:
    print("No equal distribution possible")
else:
    for num in range(len(population)):
        if population[num] < minimum_wealth:
            transfer = minimum_wealth - population[num]
            richest = population.index(max(population))
            population[richest] -= transfer
            population[num] += transfer
    print(population)



