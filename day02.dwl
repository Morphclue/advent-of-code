%dw 2.0
import * from dw::util::Values
output application/json
var maxRed = 12
var maxGreen = 13
var maxBlue = 14

fun part1(payload) = (
    sum(
        payload splitBy "\n"
        map ((lines) -> (lines splitBy ": ")[1])
        map ((games) -> 
            games splitBy "; "
            map ((pulls) -> 
                pulls splitBy ", "
                map ((pull) -> 
                    do {
                      var count = (pull splitBy " ")[0]
                      var color = (pull splitBy " ")[1]
                      ---
                      isValid:
                        if (color == "red") maxRed >= count
                        else if (color == "green") maxGreen >= count
                        else if (color == "blue") maxBlue >= count
                        else false
                    }
                )
                reduce ((item, accumulator = true) -> item.isValid and accumulator)
            )
            reduce ((item, accumulator = true) -> item and accumulator)
        )
        map ((item, index) -> if(item) index + 1 else null)
        filter(index) -> index != null
    )
)

fun part2(payload) = sum(
    payload splitBy "\n"
        map ((lines) -> (lines splitBy ": ")[1])
        map ((games) -> 
            games splitBy "; "
            map ((pulls) -> 
                pulls splitBy ", "
                map ((pull) -> 
                    do {
                      var count = (pull splitBy " ")[0]
                      var color = (pull splitBy " ")[1]
                      ---
                      {
                          count: count as Number, 
                          color: color
                      }
                    }
                )
            ) 
            flatMap ((item) -> item)
            reduce ((item, colorGroup={red: 0, green: 0, blue: 0}) ->    
                colorGroup update item.color with max([item.count, (colorGroup[item.color] as Number)])
            )
       ) 
       map ((item) -> item.red * item.green * item.blue)
)
---
{
    part1: part1(payload),
    part2: part2(payload)
}
