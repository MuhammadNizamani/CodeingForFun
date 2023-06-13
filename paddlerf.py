# print(100*"isjaqie\n")
import paddle

x = paddle.to_tensor([0, 0.3, 0.7, 0.842])
out = paddle.erf(x)
print(out)