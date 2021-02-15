import numpy as np
import tikzplotlib as tlp
import matplotlib.pyplot as plt
from matplotlib import ticker


fig, ax = plt.subplots(1, 1)
ax.plot(np.arange(5), 0.2 * np.arange(5), "-or", label="example")
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.legend()
plt.tight_layout()

tlp.save(
    "../doc/filename.tex", 
    axis_width = "\\figwidth",
    axis_height = "\\figheight",
    tex_relative_path_to_data = "./",
    strict = True,
)
