def log(b, x):
    """Return the base b logarithm of a positive number
    using the upscale-downshift algorithm"""
    import sys

# prepare inputs and parameters
# b = (base of logarithm)
    if b <= 0.0:
        print "We don't do nonpositive bases."; sys.exit()
    elif b < 1.0:
        br = 1.0/b; oppb = -1
    else:
        br = float(b); oppb = 1
# x = (argument of logarithm)
    if x <= 0.0:
        print "We don't do nonpositive arguments."; sys.exit()
    elif x < 1.0:
    	xr = 1.0/x; oppx = -1
    else:
    	xr = float(x); oppx = 1

# fix a positive integer exponent for the calculation (could be 10 or other)
    k = 2
    rk = 1.0/k
# a quitting tolerance
    tol = 10.**(-13)

# two elementary operations on triples (u,s,v)
# u = (current log argument, a composition of transformations applied to x)
#     u is updated to u**k on upscale; to u/br on downshift
#     the corresponding transformations of y=logb(u) are y->k*y and y->y-1
#     inverses of the latter are z->z/k and z->z+1
# s = (current scale factor, the linear part of the composition of inverses)
#     s is updated to s/k on upscale
# v = (current value of proposed output, composition of inverses applied to 0)
#     v is updated to v+s on downshift
# upscale when 1 < u < br
    def upscale(u,s,v): return [u**k, rk*s, v]
# downshift when u > br
    def dnshift(u,s,v): return [u/br, s, v+s]

# operation on (u,s,v) that will upscale as needed, then downshift as needed
    def updn(u,s,v):
    	if u == 1.0:
    	    return [1.0, 0., v]
    	else:
    		tri = [u, s, v];
    		while (1 < tri[0] < br): tri = upscale(*tri)
    		while (br <= tri[0]   ): tri = dnshift(*tri)
    		return tri
	
# now get the logarithm
    usv = [xr, 1.0, 0.0];
    while (usv[1] > tol): usv = updn(*usv)
    return usv[2]*oppb*oppx

