def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /): #postional only
    print(arg)

def kwd_only_arg(*, arg): #keyword only
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1, standard=2, kwd_only=3)