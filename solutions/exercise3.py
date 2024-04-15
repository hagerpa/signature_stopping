w = lin_strat.layers[0].weight.detach().numpy() # converting weights to numpy
np.allclose(Sig.dot(w.T).flatten(), theta.detach().numpy().flatten())