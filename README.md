# Solving the 1D Poisson Equation with FEniCS
This repository provides a complete, runnable example for solving the 1D Poisson equation using the FEniCS library, drawing inspiration from the book "2016_Solving PDEs in Python with FEniCS."

# FEniCS Implementation
This section contains the full Python script to solve the problem. The code demonstrates the complete workflow, from defining the mesh and boundary conditions to solving the problem and visualizing the results.

### Import needed package
```
from dolfin import *
```

### Define mesh
```
N = 10
mesh = UnitIntervalMesh(N)
```

### Define function space
```
V = FunctionSpace(mesh, 'P', 1)
u = TrialFunction(V)
v = TestFunction(V)
```

### Define boundary conditions (BCs)
```
u_D = Expression('0', degree=1)

def boundary(x, on_boundary):
    return on_boundary

bc = DirichletBC(V, u_D, boundary)
```

### Define variational problem
```
f = Constant(-1.0)
a = dot(grad(u), grad(v))*dx
L = f*v*dx
```

### Solve PDE
```
u = Function(V)
solve(a == L, u, bc)
```

### Visualize the output
```
file = File("poisson_solution.pvd")
file << u
```


# Collaboration
We welcome contributions! Feel free to fork this repository, submit pull requests, or open issues to improve this example or add new ones.
