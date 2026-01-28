import traceback
class NumberOutOfRangeError(Exception):
  # pass
  def __init__(self, error_message, code="ERR_RANGE"):
    super().__init__(error_message)
    self.code = code
    self.traceback = traceback.format_exc()
    

