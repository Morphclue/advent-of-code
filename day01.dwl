%dw 2.0
import isNumeric from dw::core::Strings
output application/json

var digitLists = payload splitBy "\n"
    map (line) -> 
        (line filter (char) -> isNumeric(char)) 
        splitBy "" 
---
sum(digitLists map ($[0] ++ $[-1]) map $ as Number)
