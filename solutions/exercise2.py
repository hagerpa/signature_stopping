plt.plot(X[k, :, 0], X[k, :, 0], linewidth=.5, linestyle="dashed")
plt.plot(X[k, :, 0], X[k, :, 1], linewidth=.5, linestyle="dashed")
plt.plot(X[k, :, 0], 0.5 * (Sig[k, :, 3] - Sig[k, :, 4]),
         label=r"$\frac{1}{2}\left(\int X^1 dX^2 - \int X^2 dX^1\right)$")
plt.legend();
