from pymprog import *


c = (50.,20.,30.,80.)
A = [(400.,200.,150.,500.),(3.,2.,0.,0.),(2.,2.,4.,4.),(2.,4.,1.,5.)]
b = (500.,6.,10.,8.)

begin('Segundo')
verbose(True)
x = var('x',4)
minimize(sum(c[i]*x[i] for i in range(4)))
for i in range(4):
	sum(A[i][j]*x[j] for j in range(4)) >= b[i]

"""begin('Primero')
verbose(True)
x = var('x',2)
maximize(22.0*x[0] + 20.0*x[1])
2.5*x[0] + 3*x[1] <= 4500.0
3.0*x[0] + 6.0*x[1] <= 8400.0
14.0*x[0] + 10.0*x[1] <= 20000.0
x[0] >= 600
x[0] + x[1] <= 1700"""


solve()
sensitivity()
end()