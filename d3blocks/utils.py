"""Utils.

Library     : d3blocks
Author      : E.Taskesen
Mail        : erdogant@gmail.com
Github      : https://github.com/d3blocks/d3blocks
License     : GPL3
"""

import numpy as np
import colourmap


# %% Setup colors
def set_colors(X, c, cmap, c_gradient=None):
    """Set colors for in various blocks.

    Description
    -----------
    Given the size of input data X, and the class labels, return the hex colors.
    This optional is possible in the following blocks:
        * scatter
        * chord
    """
    hexok = False
    # In case only one (c)olor is defined. Set all to this value.
    if isinstance(c, str): c = np.repeat(c, X.shape[0])

    # Check whether the input is hex colors.
    hexok = np.all(list(map(lambda x: (x[0]=='#') and (len(x)==7), c)))

    if hexok:
        # Input is hex-colors thus we do not need to touch the colors.
        labels = np.arange(0, X.shape[0]).astype(str)
        c_hex = c
    else:
        # The input are string-labels and not colors. Lets convert to hex-colors.
        labels = c
        c_hex, _ = colourmap.fromlist(c, cmap=cmap, method='matplotlib', gradient=c_gradient, scheme='hex')

    if (c_gradient is not None):
        c_hex = density_color(X, c_hex, c)

    # Return
    return c_hex, labels


# %% Create gradient based based on the labels.
def density_color(X, colors, labels):
    """Determine the density.

    Description
    -----------
    Given (x,y) coordinates, determine the density. This optional is possible in the following blocks:
        * scatter.

    """
    from scipy.stats import gaussian_kde
    uilabels = np.unique(labels)
    density_colors = np.repeat('#ffffff', X.shape[0])

    if (len(uilabels)!=len(labels)):
        for label in uilabels:
            idx = np.where(labels==label)[0]
            if X.shape[1]==2:
                xy = np.vstack([X[idx, 0], X[idx, 1]])
            else:
                xy = np.vstack([X[idx, 0], X[idx, 1], X[idx, 2]])

            try:
                # Compute density
                z = gaussian_kde(xy)(xy)
                # Sort on density
                didx = idx[np.argsort(z)[::-1]]
            except:
                didx=idx

            # order colors correctly based Density
            density_colors[didx] = colors[idx]
            # plt.figure()
            # plt.scatter(X[didx,0], X[didx,1], color=colors[idx, :])
            # plt.figure()
            # plt.scatter(idx, idx, color=colors[idx, :])
        colors = density_colors

    # Return
    return colors
