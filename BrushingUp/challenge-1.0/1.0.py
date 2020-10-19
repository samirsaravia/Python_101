"""
Question 1
Write a short program that will print out the version of python you are
using.
"""
import sysconfig

python_version = sysconfig.get_python_version()
print(f'You are using  version {python_version} ')
