package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func read() ([]int, []int) {
	f, _ := os.Open("day1/data.txt")
	defer f.Close()

	s := bufio.NewScanner(f)
	inputs := make([]string, 0)
	for s.Scan() {
		inputs = append(inputs, s.Text())
	}

	col1 := make([]int, 0)
	col2 := make([]int, 0)
	for _, row := range inputs {
		splits := strings.Split(row, " ")

		c1, _ := strconv.Atoi(splits[0])
		col1 = append(col1, c1)

		c2, _ := strconv.Atoi(splits[3])
		col2 = append(col2, c2)
	}
	return col1, col2
}

func main() {
	col1, col2 := read()

	sort.Slice(col1, func(i, j int) bool {
		return col1[i] < col1[j]
	})
	sort.Slice(col2, func(i, j int) bool {
		return col2[i] < col2[j]
	})

	sims := make(map[int]int)
	for _, n1 := range col1 {
		sims[n1] = 0
	}

	for _, n2 := range col2 {
		val, ok := sims[n2]
		if ok {
			sims[n2] = val + 1
		}
	}

	total := 0
	for _, n3 := range col1 {
		total += n3 * sims[n3]
	}
	fmt.Println(total)
}
