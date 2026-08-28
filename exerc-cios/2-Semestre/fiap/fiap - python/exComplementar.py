def mostrarValores(*args):
    return args
print(mostrarValores(5, 10))


def somarNum(*nums):
    return sum(nums)
print(somarNum(10, 109, 209))

def listarRecursos(*args):
    for t in args:
        return t
print(listarRecursos("hdr", "grade"))
print(listarRecursos("hdr", "grade", "foco"))

def mostrarConfig(**configuracoes):
    for config in configuracoes:
        print(configuracoes[config])
mostrarConfig(modo="noturno", qualidade="Alta")
