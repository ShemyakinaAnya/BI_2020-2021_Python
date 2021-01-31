import matplotlib.pyplot as plt

# Data on bacteria growth (personal resources)

xs = [0, 12, 18, 25, 36, 47, 66.5, 86.5]
ys_Glc = [0.08, 2.3, 3.78, 3.49, 3.15, 3.21, 3.38, 3.26]
ys_Ac = [0.08, 0.38, 0.61, 0.94, 1.52, 1.82, 1.87, 1.99]
ys_Glc_Ac = [0.08, 1.33, 4.92, 5.6, 5.4, 5.52, 5.34, 5.27]
ys_LB = [0.08, 0.72, 1.58, 2.91, 4.29, 4.03, 4.54, 4.45]
ys_BH = [0.08, 2.38, 4.21, 6.21, 9.31, 8.5, 8.83, 8.16]

# Plotting

plt.plot(xs, ys_Glc, color='yellow', marker='o', markersize=8, linewidth=3, label='Mineral medium with Glucose')
plt.plot(xs, ys_Ac, color='deepskyblue', marker='v', markersize=8, linewidth=3, label='Mineral medium with Acetate')
plt.plot(xs, ys_Glc_Ac, color='chartreuse', marker='s', markersize=8, linewidth=3,
         label='Mineral medium with Glucose and Acetate')
plt.plot(xs, ys_LB, color='orange', marker='x', markersize=12, linewidth=3, label='Luria-Bertani broth')
plt.plot(xs, ys_BH, color='orangered', marker='1', markersize=20, linewidth=3, label='Brain heart infusion')

# Customization

plt.title('Growth of $Rhodococcus$ bacterium on different growth media', fontsize=22)
plt.xlabel('Time, hours', fontsize=18)
plt.ylabel('Optical density at 492 nm', fontsize=18)
plt.legend(prop={'size': 12})
plt.grid()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()
