import asyncio, aio_pika, json
from app.use_cases.turing_machine import tm

def format_dict(tm_states):
  for key, value in tm_states.items():
        if isinstance(value, list):
            tm_states[key] = set(value)
  
  return tm_states

async def main():
  connection = await aio_pika.connect_robust(
    "amqp://mtu:mtutp@rabbitmq"
  )

  queue_name = "mtu"

  async with connection:
    channel = await connection.channel()

    await channel.set_qos(prefetch_count=10)

    queue = await channel.declare_queue(queue_name, auto_delete=False)

    async with queue.iterator() as queue_iter:
      async for message in queue_iter:
        async with message.process():
          tm_states = format_dict(json.loads(message.body))
          await tm(tm_states, tm_states)

if __name__ == "__main__":
  asyncio.run(main())