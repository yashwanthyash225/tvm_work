import torch
from torch import nn

import tvm
from tvm import relay

from tvm.contrib import graph_executor

### Creating a simple FC layer model
model = nn.Linear(in_features=3, out_features=2)
model = model.eval()

### Configuring the input shape for the model
input_shape = [1, 3]
input_data = torch.tensor([[1.0, 2.0, 3.0]])
input_name = "input0"
shape_list = [(input_name, input_shape)]

### Converting the pytorch model to TorchScript
scripted_model = torch.jit.trace(model, input_data).eval()

### Converting TorchScript to Relay Graph/IR
mod, params = relay.frontend.from_pytorch(scripted_model, shape_list)
# print(mod["main"])  # Prints the Relay IR of the model

### Compiling the Relay Graph/IR for specified target
target = tvm.target.Target("llvm -mcpu=sandybridge")
with tvm.transform.PassContext(opt_level=3):
    lib = relay.build(mod, target=target, params=params)
# print(lib.get_lib().get_source())  # Prints the LLVM IR of the model

### Running the model
device = tvm.cpu(0)
m = graph_executor.GraphModule(lib["default"](device))
m.set_input(input_name, input_data)
m.run()
tvm_output = m.get_output(0)
print(tvm_output)
