from automata.tm.dtm import DTM
from utils.logger import logger

def tm(request_values):
  dtm = DTM(
      states= request_values.get("states"),
      input_symbols= request_values.get("input_symbols"),
      tape_symbols= request_values.get("tape_symbols"),
      transitions= request_values.get("transitions"),
      initial_state= request_values.get("initial_state"),
      blank_symbol= request_values.get("blank_symbol"),
      final_states= request_values.get("final_states"),
  )
  
  if dtm.accepts_input(request_values.get("input")):
        logger.info("Input accepted")
        return True
  logger.error("Input rejected")
  return False