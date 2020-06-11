import json
import schedulers

with open('./procesos.json') as proc_archivo:
  procs = json.load(proc_archivo)

for proc in procs:
  proc['empezado'] = 0
  proc['terminado'] = 0
  proc['espera'] = 0

cola = []
actual = None
tiempo = 0
while True:
  print('t={}'.format(tiempo))

  # Encontrar el tiempo de espera para HRRN
  for proc in cola:
    proc['espera'] = tiempo - proc['llegada']

  # Confirmar proceso de llegada
  llegado = [proc for proc in procs if proc['llegada'] == tiempo]
  llegado = sorted(llegado, key=lambda k: k['id'])
  cola += llegado

  # Comprobar proceso de apagado
  if actual:
    if actual['ejecucion'] + actual['empezado'] == tiempo:
      print('p{} terminado'.format(actual['id']))
      actual['terminado'] = tiempo
      actual = None

  # Verificar el proceso actual
  if not actual:
    try:
      # actual = schedulers.first_in_first_out(cola)
      # actual = schedulers.shortest_job_first(cola)
      actual = schedulers.highest_response_ratio_next(cola)
    except:
      break
    print('p{} empezado'.format(actual['id']))
    actual['empezado'] = tiempo

  tiempo += 1

print('\n=== resultados ===')
awt = 0
att = 0
for proc in procs:
  print('#p{}'.format(proc['id']), end='')
  wt = proc['empezado'] - proc['llegada']
  print(', tiempo en espera: {}'.format(wt), end='') # 대기 시간
  tt = proc['terminado'] - proc['llegada']
  print(', termination tiempo: {}'.format(tt)) # 반환 시간
  awt += wt
  att += tt
awt /= len(procs)
att /= len(procs)
print('\nAWT: {}\nATT: {}'.format(awt, att))
