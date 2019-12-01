package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	filename := "test.txt"
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Printf("readfile: %s\n", err)
	}
	lines := strings.Split(string(content), "\n")
	fmt.Printf("%#v\n", lines)
	fmt.Printf("%s\n", lines[0])
}
