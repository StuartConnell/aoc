import re


def get_input() -> str:

    s = ""
    with open("data.txt") as f:
        lines = f.readlines()

    for l in lines:
        s += l
    return s

def main():
    mem = get_input() 
    regex = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")

    idx = [m for m in re.finditer(regex, mem)]

    matches = []
    for i in idx:
        matches.append(mem[i.start():i.end()])
    
    results = []
    for m in matches:
        nums = m[4:-1]
        num_lst = nums.split(",")
        result = int(num_lst[0]) * int(num_lst[1])
        results.append(result)

    total = 0
    for r in results:
        total += r 
    print(total)

if __name__ == "__main__":
    main()
