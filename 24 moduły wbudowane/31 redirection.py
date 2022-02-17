import sys

saved_stdout = sys.stdout

file = open('logs.txt', 'w')
sys.stdout = file

print('Logging...')
print('Connecting...')
print('Closing...')

file.close()
sys.stdout = saved_stdout
print('Completed successfully')
