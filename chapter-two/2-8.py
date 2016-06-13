# exercise 8

current_time = input( "What time is it now? (hours in 24h format) >>" )
offset = input( "Number of hours to wait >>" )
result = (current_time + offset) % 24
print( "After " + str(offset) + " hours later the clock shows " + str(result) + "." )

