def first_in_first_out(cola):
  return cola.pop(0)

def shortest_job_first(cola):
  proc = sorted(cola, key=lambda k: k['ejecucion'])[0]
  cola.remove(proc)
  return proc

def highest_response_ratio_next(cola):
  def priority(proc):
    return (proc['espera'] + proc['ejecucion']) / proc['ejecucion']
  
  proc = sorted(cola, key=lambda k: priority(k), reverse=True)[0]
  cola.remove(proc)
  return proc
