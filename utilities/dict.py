#coding: utf-8
import types

#获取字典中的objkey对应的值，适用于字典嵌套
#dict:字典
#objkey:目标key
#default:找不到时返回的默认值
def dict_get(dict, objkey, default):
    tmp = dict
    for k,v in tmp.items():
        if k == objkey:
            return v
        else:
            if type(v) is dict:
                ret = dict_get(v, objkey, default)
                if ret is not default:
                    return ret
    return default

# #如
dicttest={"result":{"code":"110002","msg":"设备设备序列号或验证码错误"},"alien":"alien_hu"}
# ret=dict_get(dicttest, 'msg', None)
# print(ret)

# def test_dict(dict,key):
#     for k,v in dicttest.items():
#         if k == "key":
#             return v
#         else:
#             if type(v) is dict:
#                 ret = test_dict(v,key)
#                 if ret:
#                     return ret
#
# r = test_dict(dicttest,'msg')
# print(r)


dicttest={"msg":"设备设备序列号或验证码错误","alien":"alien_hu"}

def test_dict(dicttest):
    for k, v in dicttest.items():
        if k=="alien":
            return v

r = test_dict(dicttest)
print(r)




