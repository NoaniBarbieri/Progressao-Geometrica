n=int(input("entre com um valor"))
a1=int(input("entre com o primeiro valor"))
q=float(input("entre com a razão"))
an=a1*(q**(n-1))
if n==1:
    print("o n-ésimo termo será {}".format(a1))
else:
    print("o n-ésimo termo será {}".format(an))
