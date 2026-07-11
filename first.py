import numpy as np

# Input values
income = 0.8        # Normalized
credit_score = 0.9
employment = 1.0

# Weights
w1 = 0.4
w2 = 0.5
w3 = 0.3

# Bias
bias = -0.6

# Weighted sum
z = (income*w1) + (credit_score*w2) + (employment*w3) + bias

# Step activation
if z >= 0:
    output = 1
else:
    output = 0

print("Weighted Sum =", round(z,2))
print("Loan Decision =", output)
