package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/ehtishamiqbal433-cell/infra-scope/internal/tui"
)

var version = "v1.0.0"

func main() {
	ver := flag.Bool("version", false, "print version")
	flag.Parse()

	if *ver {
		fmt.Println(version)
		return
	}

	// If any args passed (non-flag), keep behavior for compatibility
	if len(os.Args) > 1 {
		for _, a := range os.Args[1:] {
			if a == "--version" {
				fmt.Println(version)
				return
			}
		}
	}

	fmt.Println("Starting Git-Scope interactive UI (stub). Press Ctrl+C to exit.")
	tui.Run()
}
