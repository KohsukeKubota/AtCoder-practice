N = int(input())
hour, mod = divmod(N, 3600)
minute, sec = divmod(mod, 60)
print('{:02}:{:02}:{:02}'.format(hour, minute, sec))
