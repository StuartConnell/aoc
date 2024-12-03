import re


def get_input() -> str:

    s = ""
    with open("data.txt") as f:
        lines = f.readlines()

    for line in lines:
        s += line
    return s


def filter_mem(mem: str) -> str:
    do_regex = re.compile(r"do\(\)")
    dont_regex = re.compile(r"don't\(\)")

    string_to_search = mem
    while True:

        dont_idxs = [m.start() for m in re.finditer(dont_regex, string_to_search)] 
        if len(dont_idxs) == 0:
            break

        dont_idx = dont_idxs[0]

        do_idxs = [m.start() for m in re.finditer(do_regex, string_to_search)] 
        do_idx = -1
        for idx in do_idxs:
            if idx > dont_idx:
                do_idx = idx
                break

        if do_idx == -1:
            string_to_search = string_to_search[:dont_idx]
            print(string_to_search)
        else:
            string_to_search = string_to_search[:dont_idx] + string_to_search[do_idx:]
            print(string_to_search)
    return string_to_search
            


def main():
    mem = get_input() 
    mem = filter_mem(mem)

    regex = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
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
