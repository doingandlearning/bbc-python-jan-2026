# int("not in a number")
import traceback
from bbc_error import NumberOutOfRangeError
# anything that might go wrong
try:
  # 1 - 50
  user_input = 51
  raise NumberOutOfRangeError(f"Number out of range - user entered {user_input}", code="ERR_OUT_OF_RANGE")
  
except ZeroDivisionError:
  print("You can't divide by zero - duh!")
except ValueError as e:
  # print("That wasn't a number - you can only use digits!")
  print(e)
  print(traceback.format_exc())
except NumberOutOfRangeError as e:
  print(e.code)
except Exception as e: 
  print("Something unexpected happened. Please try again later.")
  print(traceback.format_exc())
finally:
  print("All done!")

