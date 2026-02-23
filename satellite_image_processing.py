import numpy as np
import time

# Simulate 1D satellite data (9,000,000 pixels)
data = np.arange(9000000)

# Start timing
start = time.time()

# Reshape into 3000 x 3000 image
image = data.reshape(3000, 3000)

# Create cloud filter (example: random filter)
cloud_filter = np.random.rand(3000, 3000)

# Apply element-wise multiplication
filtered_image = image * cloud_filter

end = time.time()

print("Processing Time:", end - start)
