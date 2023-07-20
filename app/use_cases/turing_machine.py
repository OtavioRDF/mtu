from automata.tm.dtm import DTM
from app.utils.logger import logger
from app.entities.schemas import EmailSchema
from app.use_cases.send_mail import simple_send

async def tm(request_values, info):
  dtm = DTM(
      states= request_values.get("states"),
      input_symbols= request_values.get("input_symbols"),
      tape_symbols= request_values.get("tape_symbols"),
      transitions= request_values.get("transitions"),
      initial_state= request_values.get("initial_state"),
      blank_symbol= request_values.get("blank_symbol"),
      final_states= request_values.get("final_states"),
  )
  
  email_schema = EmailSchema(email=["to@example.com"])

  if dtm.accepts_input(request_values.get("input")):
    await simple_send(email_schema, result="accepted", configuration=str(info))
    logger.info("Input accepted")
    return True

  await simple_send(email_schema, result="rejected", configuration=str(info))
  logger.error("Input rejected")
  return False