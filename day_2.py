def main():
    
    strategy_guide = "day_2.txt"
    with open(strategy_guide, 'r', encoding='UTF-8') as fd:
        strategy = fd.read().splitlines()
        # print(strategy)
    score = 0
    for round in strategy:
        if round[0] == "A" and round[2] == "X":
            score += 3
        if round[0] == "B" and round[2] == "X":
            score += 1
        if round[0] == "C" and round[2] == "X":
            score += 2
        if round[0] == "A" and round[2] == "Y":
            score += 4
        if round[0] == "B" and round[2] == "Y":
            score += 5
        if round[0] == "C" and round[2] == "Y":
            score += 6
        if round[0] == "A" and round[2] == "Z":
            score += 8
        if round[0] == "B" and round[2] == "Z":
            score += 9
        if round[0] == "C" and round[2] == "Z":
            score += 7
    
        
    print(score)
        
if __name__ == '__main__':
    main()