package main
import "fmt"

const rows = 1
const cols = 2
var board = [rows][cols]int{  
   {0,2},
}

func rot_others(i int, j int) {
  //check right
  if i+1 < rows{
    if board[i+1][j] == 1 {
      board[i+1][j] = 2
    }
    
  }
  //check left
  if i-1 >= 0 {
    if board[i-1][j] == 1 {
      board[i-1][j] = 2
    }
  }
  //check above
  if j+1 < cols{
    if board[i][j+1] ==1 {
      board[i][j+1] = 2
    }
  }
  //check below
  if j-1 >= 0{
    if board[i][j-1] ==1 {
      board[i][j-1] = 2
    }
  }
}

func check_board(newboard [rows][cols]int){
  for i := 0; i < rows; i++ {
    for j := 0; j < cols; j++{
      if newboard[i][j] == 2{
        rot_others(i,j)
      }
    }
  }
}
func still_fresh(newboard [rows][cols]int) bool{
  for i := 0; i < rows; i++ {
    for j := 0; j < cols; j++{
      if newboard[i][j] == 1{
        return true
      }
    }
  }
  return false
}

func main() {
  for minute := 0; minute < 10; minute ++{
    var tmpboard = board
    check_board(tmpboard)
    if board == tmpboard{
      if still_fresh(tmpboard) {
        fmt.Print("couldnt get them all")
        minute = -1
        fmt.Println(minute)
        break
      } else {
        fmt.Println("All orages have been currupt")
        fmt.Println(minute)
        break
      }
    }
    fmt.Println(board)
  }
  
}