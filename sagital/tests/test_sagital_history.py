
import numpy as np

def test_basic():
    # Make new output file
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

    # Run sagital brain file to generate output
    exec(open("sagital_brain.py").read())

    # Load output
    loaded = np.loadtxt('brain_average.csv', delimiter=',')

    # Expected output
    expected = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0])

    # Check the values are identical
    np.testing.assert_array_equal(loaded, expected)


def test_better():
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')



'''

import subprocess 
import numpy as np

# generated data
data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

# run 
subprocess.run(["python", "sagital_brain.py"]) 

# read output to then compare
result = np.loadtxt('brain_average.csv', delimiter=',')

# Generate an expected result

expected = np.zeros(20)
expected[-1] = 1

np.testing.assert_array_equal(result, expected) # error if it fails

'''