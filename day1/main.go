package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func read() ([]int, []int) {
	f, err := os.Open("day1/data.txt")
	if err != nil {
		log.Fatal(err.Error())
	}
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
		c1, err := strconv.Atoi(splits[0])
		if err != nil {
			log.Fatal(err.Error())
		}
		c2, err := strconv.Atoi(splits[3])
		if err != nil {
			log.Fatal(err.Error())
		}

		col1 = append(col1, c1)
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
