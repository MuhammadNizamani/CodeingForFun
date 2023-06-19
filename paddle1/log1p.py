import paddle

x = paddle.to_tensor([0.5, 1.0, 2.0])
result = paddle.log1p(x)

print(result)
