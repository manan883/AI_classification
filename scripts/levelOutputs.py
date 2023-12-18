import logging
import sys

# Create a root logger
root = logging.getLogger()

# Set the root logger level to DEBUG
root.setLevel(logging.DEBUG)

# Create a stream handler for stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
# Create a stream handler for stderr

# Create formatters for both handlers
formatter_stdout = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Set the formatters for both handlers
stdout_handler.setFormatter(formatter_stdout)

# Add both handlers to the root logger
root.addHandler(stdout_handler)


