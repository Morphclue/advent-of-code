%dw 2.0
output application/json
var results1 = payload scan /mul\((\d+),(\d+)\)/
---
{
    part1: sum(results1 map((group) -> group[1] * group[2])),
    part2: "TODO"
}
