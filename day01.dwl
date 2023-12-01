%dw 2.0
import isNumeric from dw::core::Strings
output application/json

var digitLists = payload splitBy "\n"
    map (line) -> 
        (line 
            replace "one" with "o1e"
            replace "two" with "t2o"
            replace "three" with "t3e"
            replace "four" with "f4r"
            replace "five" with "f5e"
            replace "six" with "s6x"
            replace "seven" with "s7n"
            replace "eight" with "e8t"
            replace "nine" with "n9e"
            filter (char) -> isNumeric(char)
        )
        splitBy "" 
---
sum(digitLists map ($[0] ++ $[-1]) map $ as Number)
