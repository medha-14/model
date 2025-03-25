import pybamm

model = pybamm.BaseModel()

# Define variables, equations, etc.
x = pybamm.Variable("x")
y = pybamm.Variable("y")
dxdt = 4 * x - 2 * y
dydt = 3 * x - y
model.rhs = {x: dxdt, y: dydt}
model.initial_conditions = {x: pybamm.Scalar(1), y: pybamm.Scalar(2)}
model.variables = {"x": x, "y": y, "z": x + 4 * y}
