package tui

import (
	"bufio"
	"fmt"
	"os"
)

// Run launches a minimal interactive stub for Git-Scope.
func Run() {
	fmt.Println("Git-Scope TUI (stub)")
	fmt.Println("Type 'help' for commands. Type 'exit' to quit.")
	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print("> ")
		if !scanner.Scan() {
			fmt.Println("\nexiting")
			return
		}
		cmd := scanner.Text()
		switch cmd {
		case "help":
			fmt.Println("Available commands: help, version, exit")
		case "version":
			fmt.Println("v1.0.0")
		case "exit", "quit":
			fmt.Println("bye")
			return
		default:
			fmt.Println("unrecognized command; type 'help'")
		}
	}
}
