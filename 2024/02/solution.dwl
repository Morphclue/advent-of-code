%dw 2.0
import * from dw::core::Arrays
output application/json
var reports = payload
        splitBy("\n")
        map($ splitBy " " map((x) -> x as Number))

fun isSafe(report) =
    ((0 to (sizeOf(report) - 2)) every ((idx) ->
        report[idx + 1] - report[idx] >= 1 and
        report[idx + 1] - report[idx] <= 3
    )) and
    (
        if (report[1] > report[0])
            ((0 to (sizeOf(report) - 2)) every ((idx) -> report[idx + 1] > report[idx]))
        else
            ((0 to (sizeOf(report) - 2)) every ((idx) -> report[idx + 1] < report[idx]))
    )

fun isSafeWithDampener(report) =
    isSafe(report) or
    ((0 to (sizeOf(report) - 1)) some ((idx) ->
        isSafe(
            if (idx == 0)
                report[1 to sizeOf(report) - 1]
            else if (idx == sizeOf(report) - 1)
                report[0 to idx - 1]
            else
                report[0 to idx - 1] ++ report[idx + 1 to sizeOf(report) - 1]
        )
    ))
---
{
    part1: sizeOf(reports filter ((report) -> isSafe(report))),
    part2: sizeOf(reports filter ((report) -> isSafeWithDampener(report)))
}
