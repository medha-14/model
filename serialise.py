import pybamm
from model2 import CustomModel

# do the example
dfn_model = CustomModel()
dfn_sim = pybamm.Simulation(dfn_model)
# discretise and build the model
dfn_sim.build()

dfn_sim.save_model("example")