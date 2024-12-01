%dw 2.0
output application/json
var rows = payload splitBy ("\n") map ($ splitBy /\s+/) map ($ map ((x) -> x as Number))
var left = rows map ((row) -> row[0])
var right = rows map ((row) -> row[1])
---
(left orderBy (x) -> x)
    zip (right orderBy (x) -> x)
    map ((pair) -> abs(pair[0] - pair[1]))
    reduce ((sum, diff) -> sum + diff)
