from random import uniform
import matplotlib.pyplot as plt
import math
def main():

  n = int(input("n: "))
  m = 0 # contador de pontos no quadrado
  x_c = []
  y_c = []
  x_q = []
  y_q = []
  tries = []
  i_arr = []

  for i in range(n):
    x_p = uniform(-3, 3)
    y_p = uniform(0, 2)

    if(y_p - 1/((2*math.pi)**0.5)*math.exp(-0.5*x_p**2) <= 0):
      x_c.append(x_p)
      y_c.append(y_p)
      m += 1
    else:
      x_q.append(x_p)
      y_q.append(y_p)
    tries.append(12*m/(i+1)) # aproximacoes
    i_arr.append(i+1)

  print(12*m/n)
  s = 0
  for i in range(len(tries)):
    s = s + tries[i]
  #print(s/len(tries))
  #print("|e| = " + str(abs(math.asin(1)*2 - 4*m/n)))

  plt.title("Convergência do método de Monte Carlo")
  plt.scatter(i_arr, tries, color = "red")
  plt.xlabel("Amostras")
  plt.ylabel("Aproximação")
  plt.annotate('Valor aproximado da integral', xy=(4000, (12*m/n)), xytext=(3000, (12*m/n + 0.1)), arrowprops=dict(facecolor = 'black'))
  plt.show()

  xcyc = zip(x_c, y_c)
  xqyq = zip(x_q, y_q)

  plt.title("Figuras do método de Monte Carlo")
  plt.scatter(x_c, y_c, color = "red")
  plt.scatter(x_q, y_q, color = "blue")
  plt.show()

main()
