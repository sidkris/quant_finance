import scipy
import matplotlib.pyplot as plt 

def brownian_motion(dt = 0.1, x0 = 0, N = 1000):

  # initialize W(t) with zeros 
  W = scipy.zeros(N+1)
  t = scipy.linspace(0, N, N+1)

  # we use cumulative sum -- on every step the additional value is drawn from a normal dist with mean 0 and variance dt*dt..N(0, dt*dt)
  W[1:N+1] = scipy.cumsum(scipy.random.normal(0, dt,N))
  return t, W

def plot_brownian_motion(t, W):
  plt.plot(t, W)
  plt.xlabel("Time (t)")
  plt.ylabel("Wiener-Process W(t)")
  plt.title("Wiener-Process")
  plt.show()