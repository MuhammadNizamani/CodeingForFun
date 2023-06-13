# print(100*"isjaqie\n")
import paddle

x = paddle.to_tensor([-0.4, -0.2, 0.1, 0.3])
out = paddle.erf(x)
print(out)