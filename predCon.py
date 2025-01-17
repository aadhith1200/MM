# Python3 code for solving the differential equation
# using Predictor-Corrector or Modified-Euler method
# with the given conditions, y(0) = 0.5, step size(h) = 0.2
# to find y(1)

# consider the differential equation
# for a given x and y, return v
def f(x, y):
	v = y - 2 * x * x + 1;
	return v;

# predicts the next value for a given (x, y)
# and step size h using Euler method
def predict(x, y, h):
	
	# value of next y(predicted) is returned
	y1p = y + h * f(x, y);
	return y1p;

# corrects the predicted value
# using Modified Euler method
def correct(x, y, x1, y1, h):
	
	# (x, y) are of previous step
	# and x1 is the increased x for next step
	# and y1 is predicted y for next step
	e = 0.00001;
	y1c = y1;

	while (abs(y1c - y1) > e + 1):
		y1 = y1c;
		y1c = y + 0.5 * h * (f(x, y) + f(x1, y1));

	# every iteration is correcting the value
	# of y using average slope
	return y1c;

def printFinalValues(x, xn, y, h):
	while (x < xn):
		x1 = x + h;
		y1p = predict(x, y, h);
		y1c = correct(x, y, x1, y1p, h);
		x = x1;
		y = y1c;

	# at every iteration first the value
	# of for next step is first predicted
	# and then corrected.
	print("The final value of y at x =",
					int(x), "is :", y);

# Driver Code
if __name__ == '__main__':
	
	# here x and y are the initial
	# given condition, so x=0 and y=0.5
	x = 0; y = 0.5;

	# final value of x for which y is needed
	xn = 1;

	# step size
	h = 0.2;

	printFinalValues(x, xn, y, h);

# This code is contributed by Rajput-Ji
