# while True:
#     report_minute = 50
#     temp = report_minute + 1
#     print(f'{report_minute}, {temp}')

opc_address1 = 2
opc_address2 = 5
a = '200.4.1.1'
print(type(a), a)

a = a[:4] + str(opc_address1) + '.' + str(opc_address2) + a[7:]

print(type(a), a)
