import pybamm

class BaseModel(pybamm.lithium_ion.BaseModel):
    def __init__(self, options=None, name="Base lithium-ion model"):
        super().__init__(options, name)
