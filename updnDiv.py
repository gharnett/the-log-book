def div(x, b):
    """Return quotient of x by b
    using the upscale-downshift logarithm algorithm,
    mutatis mutandis"""
    import sys

# prepare inputs and parameters
# b = (divisor of quotient)
    if b == 0.0:
        print "We don't divide by zero."; sys.exit()
    elif b < 0.0:
        br = -b; oppb = -1
    else:
        br =  b; oppb = 1
# x = (dividend)
    if x < 0.0:
    	xr = -float(x); oppx = -1
    else:
    	xr =  float(x); oppx = 1
# a fixed positive multiplier for the calculation
    k = 10
    rk = 1.0/k
# a quitting tolerance
    tol = 10.**(-14)

# two elementary operations on triples (u,s,v)
# u = (current dividend, composition of transformations applied to x)
#     u is updated to u*k on upscale; to u-br on downshift
#     the corresponding transformations of y=u/br are y->k*y and y->y-1
#     inverses of the latter are z->z/k and z->z+1
# s = (current scale factor, the linear part of the composition of inverses)
#     s is updated to s/k on upscale
# v = (current value of proposed output, composition of inverses applied to 0)
#     v is updated to v+s on downshift
# upscale when 0 < u < br
    def upscale(u,s,v): return [u*k, rk*s, v]
# downshift when  br <= br
    def dnshift(u,s,v): return [u-br, s, v+s]

# operation on (u,s,v) that will upscale as needed, then downshift
    def updn(u,s,v):
    	if u == 0.0:
    	    return [0.0, 0, v]
    	else:
    		tri = [u, s, v];
    		while (0 < tri[0] < br): tri = upscale(*tri)
     		while (br <= tri[0]   ): tri = dnshift(*tri)
    		return tri
	
# now do the division
    usv = [xr, 1.0, 0.0];
    while (usv[1] > tol): usv = updn(*usv)
    return usv[2]*oppb*oppx







































