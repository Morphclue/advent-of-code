%dw 2.0
output application/json

var grid = (payload splitBy "\n") map ($ splitBy "")

fun countOccurrences(lines) =
  sum([lines map ((line) -> sizeOf((line scan /XMAS/))) reduce ((val, acc=0) -> acc + val),
     lines map ((line) -> sizeOf((line scan /SAMX/))) reduce ((val, acc=0) -> acc + val)])

fun horizontalRead(grid) = grid map ((row) -> row joinBy "")

fun rotate90(grid) =
  (0 to sizeOf(grid[0]) - 1) map ((colIndex) ->
    (sizeOf(grid) - 1 to 0) map ((rowIndex) -> grid[rowIndex][colIndex])
  )

fun diagonals(grid) =
  flatten(
    (-(sizeOf(grid) - 1) to sizeOf(grid[0]) - 1) map ((offset) ->
      (0 to sizeOf(grid) - 1)
      map ((row) ->
        if ((row + offset >= 0) and (row + offset < sizeOf(grid[0])))
          grid[row][row + offset]
        else ''
      ) filter ($ != '') joinBy ""
    )
  )

fun antiDiagonals(grid) =
  flatten(
    (0 to sizeOf(grid[0]) + sizeOf(grid) - 2) map ((offset) ->
      (0 to sizeOf(grid) - 1) map ((row) ->
        if (offset - row >= 0 and offset - row < sizeOf(grid[0]))
          grid[row][offset - row]
        else ''
      ) filter ($ != '') joinBy ""
    )
  )

---
{
  part1: [
    countOccurrences(horizontalRead(grid)),
    countOccurrences(horizontalRead(rotate90(grid))),
    countOccurrences(diagonals(grid)),
    countOccurrences(antiDiagonals(grid)),
  ] reduce ((val, acc=0) -> acc + val)
}
