import onnx
import torch
from onnx2torch import convert

onnx_model = onnx.load('./armor.onnx')
torch_model = convert(onnx_model)
torch.save(torch_model, './armor.pth')