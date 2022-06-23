from main import main
import multiprocessing
import time
from constants import SERVER_HOST, ENCODE_PATH, DECODE_PATH
from tests_utils import test_single_encoding_decoding, bcolors
import datetime

# start main
proc = multiprocessing.Process(target=main, args=())
proc.start()
time.sleep(1)  # waiting for server to start

number_of_enc_dec = 500
start = datetime.datetime.now()

# run multiple tests
for i in range(number_of_enc_dec):
    test_passed = test_single_encoding_decoding(SERVER_HOST, ENCODE_PATH, DECODE_PATH)
    if not test_passed:
        print(bcolors.FAIL + "PERFORMANCE TEST FAILED")
        proc.terminate()
        exit(1)


end = datetime.datetime.now()
diff = end - start
print(
    str(number_of_enc_dec)
    + " encodings+decodings took: "
    + str(diff.microseconds / 1000)
    + " ms "
    + "thats "
    + str(diff.microseconds / 1000 / number_of_enc_dec)
    + " ms/request"
)
print(bcolors.OKGREEN + "PERFORMANCE TEST PASSED")
proc.terminate()
quit()
