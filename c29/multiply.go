package main

import "fmt"

func multiply(x int,y int) int {
  if y > x {
    return multiply(y,x)
  } else if y != 0 {
    return x + multiply(x,y-1)
  } else {
    return 0
  } 
}

func main() {
  fmt.Println(multiply(10,6))
}
