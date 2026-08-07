package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("Git-Scope: Enterprise Repository Management TUI")
	if len(os.Args) > 1 && os.Args[1] == "--version" {
		fmt.Println("v1.0.0")
		return
	}
	fmt.Println("Run with appropriate arguments or use the interactive dashboard.")
}
