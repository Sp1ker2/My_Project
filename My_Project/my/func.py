def lab_1_2():

    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    # from sklearn import metrics
    X = np.loadtxt('lab01.csv', delimiter=';')
    num_clusters = 7
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], marker='o', facecolors='none',
                edgecolors='black', s=80)
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    plt.title('Input data')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

    # Create KMeans object
    kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)

    # Train the KMeans clustering model
    kmeans.fit(X)

    # Step size of the mesh
    step_size = 0.01

    # Define the grid of points to plot the boundaries
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    x_vals, y_vals = np.meshgrid(np.arange(x_min, x_max, step_size),
                                 np.arange(y_min, y_max, step_size))

    # Predict output labels for all the points on the grid
    output = kmeans.predict(np.c_[x_vals.ravel(), y_vals.ravel()])

    # Plot different regions and color them
    output = output.reshape(x_vals.shape)
    plt.figure()
    plt.clf()
    plt.imshow(output, interpolation='nearest',
               extent=(x_vals.min(), x_vals.max(),
                       y_vals.min(), y_vals.max()),
               cmap=plt.cm.Paired,
               aspect='auto',
               origin='lower')

    # Overlay input points
    plt.scatter(X[:, 0], X[:, 1], marker='o', facecolors='none',
                edgecolors='black', s=80)

    # Plot the centers of clusters
    cluster_centers = kmeans.cluster_centers_
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1],
                marker='o', s=210, linewidths=4, color='white',
                zorder=5, facecolors='black')

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    plt.title(' clusters')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def lab_1_1():
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.cluster import MeanShift, estimate_bandwidth
    from itertools import cycle

    # Load data from input file
    X = np.loadtxt('lab01.csv', delimiter=';')

    # Estimate the bandwidth of X
    bandwidth_X = estimate_bandwidth(X, quantile=0.13598, n_samples=len(X))

    # Cluster data with MeanShift
    meanshift_model = MeanShift(bandwidth=bandwidth_X, bin_seeding=True)
    meanshift_model.fit(X)

    # Extract the centers of clusters
    cluster_centers = meanshift_model.cluster_centers_
    print('\nCenters of clusters:\n', cluster_centers)

    # Estimate the number of clusters
    labels = meanshift_model.labels_
    num_clusters = len(np.unique(labels))
    print("\nNumber of clusters in input data =", num_clusters)

    # Plot the points and cluster centers
    plt.figure()
    markers = 'o*xvs1p3'
    for i, marker in zip(range(num_clusters), markers):
        # Plot points that belong to the current cluster
        plt.scatter(X[labels == i, 0], X[labels == i, 1], marker=marker, color='black')

        # Plot the cluster center
        cluster_center = cluster_centers[i]
        plt.plot(cluster_center[0], cluster_center[1], marker='o',
                 markerfacecolor='black', markeredgecolor='black',
                 markersize=15)

    plt.title('Clusters')
    plt.show()


def lab_1_3():
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import metrics
    from sklearn.cluster import KMeans

    # Load data from input file
    X = np.loadtxt('lab01.csv', delimiter=';')

    # Plot input data
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], color='black', s=80, marker='o', facecolors='none')
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    plt.title('Input data')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

    # Initialize variables
    scores = []
    values = np.arange(2, 15)

    # Iterate through the defined range
    for num_clusters in values:
        # Train the KMeans clustering model
        kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=15)
        kmeans.fit(X)
        score = metrics.silhouette_score(X, kmeans.labels_,
                                         metric='euclidean', sample_size=len(X))

        print("\nВихідні точки =", num_clusters)
        print("Бар діаграмма score =", score)

        scores.append(score)

    # Plot silhouette scores
    plt.figure()
    plt.bar(values, scores, width=0.9, color='black', align='center')
    plt.title('Бар діаграмма score')

    # Extract best score and optimal number of clusters
    num_clusters = np.argmax(scores) + values[0]
    print('\nOptimal number of clusters =', num_clusters)

    plt.show()


def lab_1_4():
    import matplotlib
    import matplotlib.pyplot as plt
    import seaborn as sns;
    sns.set()
    import numpy as np
    from sklearn.cluster import KMeans

    from sklearn.datasets import make_blobs
    # from sklearn.datasets.samples_generator import make_blobs
    X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)
    plt.scatter(X[:, 0], X[:, 1], s=20)
    plt.show()
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    # from sklearn.datasets.samples_generator import make_blobs
    X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=20, cmap='summer')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='blue', s=100, alpha=0.9);
    plt.show()


# lab_1_3()
# lab_1_1()
# while True:
#
#     func = int(input("""Виберіть одну із лабороторних
# 1  Центри кластерів (метод зсуву середнего)
# 2  Кластеризованные данные с областями кластеризации
# 3  Бар діаграмма score(number of clusters)
# 4  Вихідні точки на площині
# 0  Вихід
#     """))
#     match func:
#         case 1:
#             lab_1_1()
#         case 2:
#             lab_1_2()
#         case 3:
#             lab_1_3()
#         case 4:
#             lab_1_4()
#         case 0:
#             break
