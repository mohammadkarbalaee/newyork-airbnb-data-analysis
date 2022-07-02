higher_longitude_df = csv[csv.longitude > -73.9]
lower_longitude_df = csv[csv.longitude < -74]
higher_longitude_mean = higher_longitude_df['price'].mean()
lower_longitude_mean = lower_longitude_df['price'].mean()
print('total price mean:  ' + str(total_price_mean))
print('specific range price:  '  + str(specific_price_mean))
print('higher range price:  ' + str(higher_longitude_mean))
print('lower range price: ' + str(lower_longitude_mean))
# Output:
# total price mean:  152.7206871868289
# specific range price:  151.8987860137149
# higher range price:  93.99702528507684
# lower range price: 228.11330734966592
