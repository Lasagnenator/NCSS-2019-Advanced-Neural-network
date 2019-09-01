import multiprocessing as mp
import genetic
import sys
import os
import glob
import game_host
import random
import program

population_size = 1000
survivors_per_generation = 80 #top performing
wildcard_survivors = 20
random_per_generation = 100

max_games_per_thread = 20 #remember 4 players per game

survivors_total = survivors_per_generation+wildcard_survivors

def main():
    if os.path.exists("saveState.dat"):
        print("Found previous population data")
        population = loadState("saveState.dat")
        print("Loaded population from file")
    else:
        print("Did not find previous population, starting from nothing")
        population = create_population()
        
    f_arr = mp.Array("i", [0]*population_size)
    
    p = []
    p_id = 0
    print("Starting games")
    for i in range(0,population_size, max_games_per_thread*4):
        subset = population[i:i+(max_games_per_thread*4)]
        p.append(mp.Process(target = run_games, args=[subset, p_id, f_arr]))
        p[-1].start()
        p_id += 1
    print(p_id+1, "processes running")
    for proc in p:
        proc.join()
        
    temp = []
    for i, value in enumerate(f_arr):
        population[i].fitness = value
        temp.append(value)
        
    #print(temp)
    
    print("All bots have played a game")
    print("Saving for contingency")
    saveState(population, "saveState.dat")
    print("Saved")
    print("---------------")
    print("Begin evolution")
    population = genetic.order(population)
    print("Highest score in this generation:", population[0].fitness)
    new_population = []
    #pool to produce offspring
    pool = population[:survivors_per_generation]
    pool.extend(random.choices(population, k=wildcard_survivors))
    #how many children to produce
    required_children = population_size-random_per_generation-survivors_per_generation-wildcard_survivors
    created_children = 0
    print("Number in pool:", len(pool))
    while created_children<required_children:
        #print("created",created_children)
        childs_net = genetic.children(pool[created_children%survivors_total].net,
                                      pool[(created_children+1)%survivors_total].net)
        c1, c2 = new_player(), new_player()
        c1.net = childs_net[0]
        c2.net = childs_net[1]
        childs = [c1,c2]
        created_children += 2
        new_population.extend(childs)
    for i in range(random_per_generation):
        new_population.append(new_player())
    for player in pool:
        new_population.append(player)
    print("New population generated with length:", len(new_population))
    print("---------------")
    saveState(new_population, "saveState.dat")
    print("Saved new population")

def run_games(subset, thread_number, fitnesses):
    for i in range(0,len(subset),4):
        p1, p2, p3, p4 = subset[i:i+4]
        fname = "threads/thread{}-{}.txt".format(thread_number, i)
        f = open(fname, "w+")
        scores= game_host.start_game(p1.play, p2.play, p3.play, p4.play, f)
        fitnesses[thread_number*len(subset)+i]=scores[0]
        fitnesses[thread_number*len(subset)+i+1]=scores[1]
        fitnesses[thread_number*len(subset)+i+2]=scores[2]
        fitnesses[thread_number*len(subset)+i+3]=scores[3]
        f.close()

def new_player():
    return program.Player()

def create_population():
    pop = []
    for i in range(population_size):
        pop.append(new_player())
    return pop

def saveState(population:list, fname:str):
    import pickle
    with open(fname, "wb") as f:
        pickle.dump(population, f)

def loadState(fname:str):
    import pickle
    with open(fname, "rb") as f:
        population = pickle.load(f)
    #now we return the networks after leaving the with block
    return population

def TRAIN():
    try:
        generation = 0
        while True:
            print("-----------------------")
            print("Generation", generation)
            files = glob.glob("./threads/*")
            for file in files:
                os.remove(file)
            print("Cleared threads folder\n")
            main()
            generation += 1
            print()
    except KeyboardInterrupt:
        input("\nPress enter to exit.\n")

if __name__=="__main__":
    TRAIN()
