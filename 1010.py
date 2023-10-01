valores = input().split()
a,b,c = valores

cod01 = int(a)
quant01 = int(b)
unit01 = float(c)

valores02 = input().split()
d,e,f = valores02

cod02 = int(d)
quant02 = int(e)
unit02 = float(f)

peca01 = quant01 * unit01 
peca02 = quant02 * unit02
soma = peca01 + peca02

print('VALOR A PAGAR: R$ %0.2f' %soma)