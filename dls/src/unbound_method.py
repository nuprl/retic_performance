"hello".unbound_method()

## -----------------------------------------------------------------------------
## Retic

#Traceback (most recent call last):
#  File "unbound_method.py", line 4, in check0
#AttributeError: 'str' object has no attribute 'unbound_method'
#
#During handling of the above exception, another exception occurred:
#
#Traceback (most recent call last):
#  File "/usr/local/bin/retic", line 6, in <module>
#    retic.main()
#  File "/home/ben/code/gradual/reticulated/retic/retic.py", line 155, in main
#    reticulate(program, prog_args=args.args.split(), flag_sets=args)
#  File "/home/ben/code/gradual/reticulated/retic/retic.py", line 107, in reticulate
#    utils.handle_runtime_error(exit=True)
#  File "/home/ben/code/gradual/reticulated/retic/retic.py", line 102, in reticulate
#    _exec(code, __main__.__dict__)
#  File "/home/ben/code/gradual/reticulated/retic/exec3/__init__.py", line 2, in _exec
#    exec (obj, globs, locs)
#  File "unbound_method.py", line 257, in <module>
#  File "unbound_method.py", line 8, in check0
#retic.transient.CheckError: hello

## -----------------------------------------------------------------------------
## Python 3.4.4

#Traceback (most recent call last):
#  File "unbound_method.py", line 1, in <module>
#    "hello".unbound_method()
#AttributeError: 'str' object has no attribute 'unbound_method'
