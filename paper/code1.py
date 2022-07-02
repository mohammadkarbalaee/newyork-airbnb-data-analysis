neighbor_gr_mean_grouped_data = data.groupby(['neighbourhood_group']).mean()
maxprice_neigh_gr = neighbor_gr_mean_grouped_data.idxmax(0)['price']
maxprice_neigh_gr
# OUTPUT: 'Manhattan'
