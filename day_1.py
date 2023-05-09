from collections import defaultdict, Counter

def main():
    calorie_count = 'day_1.txt'
    
    with open(calorie_count, 'r', encoding='utf-8') as fd:
        calorie_list = fd.read().splitlines()   
    
    elf = 1
    elf_dict = defaultdict(int)
    # elf_dict = {}
    for item in calorie_list:
        if item != '':
            elf_dict[elf] += int(item)
        else:
            elf += 1
    
    value = 0
    for val in elf_dict.values():
        if val > value:
            value = val
    print(f"The most calories being carried is {value}")
        
    k = Counter(elf_dict)
    high_3 = k.most_common(3)
    total = 0
    print("The top three calorie counting elfs are")
    for i in high_3:
        print(f"Elf {i[0]} who is carrying {i[1]} calories")
        total += i[1]
    print(f"Together they have a total of {total} cals")

if __name__ == '__main__':
    main()
