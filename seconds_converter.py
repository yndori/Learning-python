total_seconds = 100000000

SECS_PER_MIN = 60
SECS_PER_HOUR = 60 * 60
SECS_PER_DAY = 24 * SECS_PER_HOUR
SECS_PER_MONTH = 30 * SECS_PER_DAY
SECS_PER_YEAR = 12 * SECS_PER_MONTH

years = total_seconds//SECS_PER_YEAR
rest = total_seconds%SECS_PER_YEAR

months = rest//SECS_PER_MONTH
rest %= SECS_PER_MONTH

days = rest//SECS_PER_DAY
rest %= SECS_PER_DAY

hours = rest//SECS_PER_HOUR
rest %= SECS_PER_HOUR

minutes = rest//SECS_PER_MIN
seconds = rest % SECS_PER_MIN


print(years , "years", months , "months" , days , "days" , hours , "hours" , minutes , "minutes" , seconds , "seconds")