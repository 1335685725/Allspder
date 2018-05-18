def tracer(msg):
    print("[TRACE] %s" % msg)

def logger(func):
    tracer("logger")
    def inner(username, password):
        tracer("inner")
        print("call %s" % func.__name__)
        return func(username, password)
    return inner

def login_debug_helper(show_debug_info=False):
    tracer("login_debug_helper")
    def proxy_fun(func):
        tracer("proxy_fun")
        def delegate_fun(username, password):
            tracer("delegate_fun")
            if show_debug_info:
                print("username: %s\npassword: %s" % (username, password))
            return func(username, password)
        return delegate_fun
    return proxy_fun

print('Declaring login_a')

@logger
@login_debug_helper(show_debug_info=True)
def login_a(username, password):
    tracer("login_a")
    print("do some login authentication")
    return True

print('Call login_a')
login_a("mdl", "pwd")
#对于只有 login_debug_helper 的情况，现在就应该是执行玩login_a输出结果的时刻了，
# 但是如果现在在加上logger 装饰器的话，那么这个 login_debug_helper(show_debug_info=True)(login_a)('mdl', 'pwd')就被延迟执行，
# 而将 login_debug_helper(show_debug_info=True)(login_a) 作为参数传递给 logger，
# 我们令 login_tmp = login_debug_helper(show_debug_info=True)(login_a)，则调用过程等价于:
# login_tmp = login_debug_helper(show_debug_info=True)(login_a)
# login_a = logger(login_tmp)
# login_a('mdl', 'pwd')