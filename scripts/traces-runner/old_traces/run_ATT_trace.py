import sys
import os
import subprocess
import numpy as np


RUN_SCRIPT = 'run_video.py'
RANDOM_SEED = 42
RUN_TIME = 320  # sec
MM_DELAY = 40   # millisec


def main():
	trace_path = sys.argv[1]
	abr_algo = sys.argv[2]
	process_id = sys.argv[3]
	ip = sys.argv[4]

	sleep_vec = range(1, 10)  # random sleep second

	# files = os.listdir(trace_path)
	# for f in files:
	f1 = 'ATT-LTE-driving.up'
	f2 = 'ATT-LTE-driving.down'

	while True:

		np.random.shuffle(sleep_vec)
		sleep_time = sleep_vec[int(process_id)]
		
		proc = subprocess.Popen('mm-delay ' + str(MM_DELAY) + 
				  ' mm-link --uplink-log=./results/cubic_att_uplink --downlink-log=./results/cubic_att_downlink ' + trace_path + f1 + ' ' + '../cooked_traces/ATT-LTE-driving.down /usr/bin/python ' + RUN_SCRIPT + ' ' + ip + ' ' + abr_algo + ' ' + str(RUN_TIME) + ' ' + process_id + ' ' + f2 + ' ' + str(sleep_time), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

		(out, err) = proc.communicate()

		if out == 'done\n':
			break
		else:
			with open('./chrome_retry_log', 'ab') as log:
				log.write(abr_algo + '_' + f + '\n')
				log.write(out + '\n')
				log.flush()



if __name__ == '__main__':
	main()
