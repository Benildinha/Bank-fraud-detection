import numpy as np
import random

def main():
    N = 100  # Tamanho do problema (N x N)
    steps = 3000  # Número total de iterações
    tracks = 50  # Número de trilhas de otimização

    def generator(x, y, x0=0.0, y0=0.0):
        return np.sin((x / N - x0) * np.pi) + np.sin((y / N - y0) * np.pi) + \
               0.07 * np.cos(12 * (x / N - x0) * np.pi) + 0.07 * np.cos(12 * (y / N - y0) * np.pi)

    x0 = np.random.random() - 0.5
    y0 = np.random.random() - 0.5
    h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
    peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

    x = np.random.randint(0, N, tracks)
    y = np.random.randint(0, N, tracks)

    for step in range(steps):
        T = max(0.01, ((steps - step) / steps) ** 3 - 0.005)

        for i in range(tracks):
            x_new = np.random.randint(max(0, x[i] - 2), min(N, x[i] + 3))
            y_new = np.random.randint(max(0, y[i] - 2), min(N, y[i] + 3))

            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            if S_new > S_old or random.random() < np.exp(-(S_old - S_new) / T):
                x[i], y[i] = x_new, y_new

    num_tracks_at_peak = sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])
    print(f"Number of tracks at the peak: {num_tracks_at_peak}")

main()
