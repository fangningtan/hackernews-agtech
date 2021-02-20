# this function checks whether the k-means algorithm outputs match each other
# by comparing the index of the smallest value in the distance from centroid vectors
# to the assigned cluster number of an observation
def check_centroid(my_dist_from_centroids, my_km_labels):
    #import relevant packages
    import numpy as np

    # choose a random integer between 0 and 374
    integer=np.random.randint(low=0, high=375)

    # obtain corresponding row from dist_from_clusters matrix
    selected_row = my_dist_from_centroids[integer,:]

    # and gets the index of the min value in the vector
    min_index = np.argmin(selected_row)

    # select the corresponding element from the km labels array
    corresponding_cluster = my_km_labels[integer]

    # print them side by side
    print(f'Index: {integer}')
    print(f'Nearest centroid: {min_index}')
    print(f'Assigned cluster: {corresponding_cluster}')