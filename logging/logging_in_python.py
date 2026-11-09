# to log messages in our python applicaton we use predefined loggers

# step 1 : import the logger
import logging as log

# step 2 : provide some basic settings
log.basicConfig(level=log.DEBUG)


a = 56 
b = 45

log.info("going to calculate the sum")
print(f"The sum of a and b is : {a + b}")
log.info("I have calculated the sum")

# log levels in python :
# 1. DEBUG  2. INFO  3. WARNING  4. ERROR  5. CRITICAL

