from pyexcs import Pyexcs
#
pyexcs = Pyexcs('YOUR_OPENAI_API_KEY', 'spanish')

@pyexcs.handle_errors
def my_func():
    r = '1' + 1
    print('This will never happen.')
    
my_func()