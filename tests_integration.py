from main import main
import multiprocessing
import time
import requests
from constants import SERVER_HOST, ENCODE_PATH, DECODE_PATH
from tests_utils import test_single_encoding_decoding, bcolors


# start main
proc = multiprocessing.Process(target=main, args=())
proc.start()
time.sleep(1)  # waiting for server to start

# run single test
test_passed = test_single_encoding_decoding(SERVER_HOST, ENCODE_PATH, DECODE_PATH)
if not test_passed:
    print(bcolors.FAIL + "INTEGRATION TEST FAILED")
    proc.terminate()
    exit(1)


print(bcolors.OKGREEN + "INTEGRATION TEST PASSED")
proc.terminate()
quit()
