actual_value = 100
annual_rate = 4.3
years = 20
future_value = actual_value * (1+ annual_rate/100)**years

print(actual_value , "in" , years , "years" , "will be equal to :" , round(future_value, 2))