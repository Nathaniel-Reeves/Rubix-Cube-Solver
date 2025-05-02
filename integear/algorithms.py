def alg1(c):
    steps = ["R","U","R'","U'"]
    for move in steps:
        c.do_move(move)

def alg2(c):
    steps = ["R","U","U","R'","U","R","U","U","R'","U","F'","U'","F"]
    for move in steps:
        c.do_move(move)

def alg3(c):
    steps = ["U","R","U'","R'","U'","F'","U'","F"]
    for move in steps:
        c.do_move(move)

def alg4(c):
    steps = ["R'","U'","R'","U'","R'","U","R","U","R"]
    for move in steps:
        c.do_move(move)

def alg5(c):
    steps = ["F","R","U","R'","U'","F"]
    for move in steps:
        c.do_move(move)

def alg6(c):
    steps = ["R'","U","U","R","U","R'","U","R"]
    for move in steps:
        c.do_move(move)

def alg7(c):
    steps = ["U'","R","U'","U'","R'","U'","R","U'","R"]
    for move in steps:
        c.do_move(move)

def alg8(c):
    steps = ["R","B'","R","F","F","R'","B","R","F","F","R","R"]
    for move in steps:
        c.do_move(move)

def alg9(c):
    steps = ["R","U'","R","U","R","U","R","U'","R'","U'","R","R"]
    for move in steps:
        c.do_move(move)

def alg10(c):
    steps = ["R","R","U","R","U","R'","U'","R'","U'","R'","U","R"]
    for move in steps:
        c.do_move(move)

def step1(c):
    """Solve the yellow cross on the bottom."""
    pass

def step2(c):
    """Solve four corner piees on the bottom."""
    pass

def step3(c):
    """Solve four edge pieces in the middle layer."""
    pass

def step4(c):
    """Solve the white edges on the top facet."""
    pass

def step5(c):
    """Solve the white corners on the top facet."""
    pass

def step6(c):
    """Orient the white corners on the top layer."""
    pass

def step7(c):
    """Orient the white edges on the top layer."""
    pass