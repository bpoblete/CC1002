# jaliscoCachipun: str -> str
# entrega la jugada ganadora del cachipun dada una entrada valida
# ejemplo: jaliscoCachipun('tijera') debe retornar 'piedra'
def ganarCachipun(jugada):
  if jugada == 'tijera':
    return 'piedra'
  elif jugada == 'papel':
    return 'tijera'
  else:
    return 'papel'

# test
assert ganarCachipun('tijera')=='piedra'

