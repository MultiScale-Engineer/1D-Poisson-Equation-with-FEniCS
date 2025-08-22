from dolfin import *

#Define mesh
N=10
mesh = UnitIntervalMesh(N)

#Define space of elements
V = FunctionSpace(mesh, 'P', 1)
u = TrialFunction(V)
v = TestFunction(V)

#Define BCs
u_D = Expression('0', degree=1)
def boundary(x, on_boundary):
    return on_boundary
bc = DirichletBC(V, u_D, boundary)

#Define variational problem
f = Constant(-1.0)
a = dot(grad(u), grad(v))*dx
L = f*v*dx

#Solve PDE
u = Function(V)
solve(a == L, u, bc)

# Plot the mesh and the solution
plot(mesh, title='Mesh')
plot(u, title='Solution')

#Visualize the output
file = File("poisson_solution.pvd")
file << u
