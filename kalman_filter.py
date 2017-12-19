import numpy as np
import cv2

def kalman_filter(NUM_FEATURES, sigma_measurement = 0.5, sigma_process = 0.03):
	'''
	Kalman filter equations:
		xk+1 = Fxk + Buk + noise
		zk = Hxk + noise

	'''
	kalman = cv2.KalmanFilter(NUM_FEATURES*4, NUM_FEATURES*2,0)
	H = np.hstack((1.*np.eye(NUM_FEATURES*2,NUM_FEATURES*2, dtype = np.float32), np.zeros((NUM_FEATURES*2,NUM_FEATURES*2),dtype=np.float32)))
	F = np.hstack((1.*np.eye(NUM_FEATURES*4,NUM_FEATURES*2,dtype=np.float32), 1.*np.eye(NUM_FEATURES*4,NUM_FEATURES*2,dtype=np.float32)))

	kalman.measurementMatrix = H
	kalman.transitionMatrix = F
	kalman.processNoiseCov = np.eye(NUM_FEATURES*4,dtype=np.float32)* sigma_process
	kalman.measurementNoiseCov = np.eye(NUM_FEATURES*2, NUM_FEATURES*2,dtype=np.float32) * sigma_measurement
	kalman.errorCovPost = 1e-1 * np.eye(NUM_FEATURES*4, NUM_FEATURES*4,dtype=np.float32)

	return kalman

def get_new_state(filter, measurement, NUM_FEATURES):
	measurement = np.array(measurement, dtype=np.float32)

	prediction = filter.predict()

	observation = filter.correct(measurement[:NUM_FEATURES*2,:])

	observation = np.reshape(observation[:NUM_FEATURES*2,:],(NUM_FEATURES,2))

	return observation
