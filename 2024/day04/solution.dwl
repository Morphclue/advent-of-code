%dw 2.0
output application/json

fun splitTrim(numbers) =
    numbers splitBy " "
        map((number) -> trim(number))
        filter((number) -> number != "")
        distinctBy ((number) -> number)

---
payload splitBy "\n"
    map((games) -> (games splitBy ": ")[1] splitBy  "| ")
    map((card) -> do {
            var wins = splitTrim(card[0])
            var scratches = splitTrim(card[1])
            ---
            sizeOf(scratches filter (wins contains $))
    })
    reduce ((item, points=0) ->
        if(item > 0)
            points + pow(2, (item-1))
        else
            points
    )
