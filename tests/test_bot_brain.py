from bot_memory.bot_brain import Brain
from time import sleep
test_bb = Brain()

print("starting tests..")

test_bb.set_last_user_spoken_to("tom_the_tester")
print(test_bb.get_last_user_spoken_to())
sleep(1)
test_bb.set_time_initialized()
print(test_bb.get_time_initialized())
sleep(1)
test_bb.set_time_last_message_sent()
print(test_bb.get_time_last_message_sent())
sleep(1)
test_bb.set_time_last_message_received()
print(test_bb.get_time_last_message_received())
