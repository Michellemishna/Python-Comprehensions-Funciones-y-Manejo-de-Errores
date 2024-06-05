#importo el modulo y le pedimos que me de la funcion get_population
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type Country => ')
  country = country.capitalize()
  result = utils.population_by_country(data, country)
  
  if result:
    labels, values = utils.get_population(result)
    charts.generate_bar_chart(labels, values)
  else: 
    print('Country not found')
    
#esto significa que si el archivo main es ejecutado desde la terminal, entonces ejecute 
#run() y si esta siendo llamado por otro archivo, entonces no se ejecute
if __name__ == '__main__':
  run()