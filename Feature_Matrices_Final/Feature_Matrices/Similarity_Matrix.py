"""
THIS CODE GENERATES A FILE WITH OUTPUT
"""
import numpy as np
import csv
import sys
import seaborn as sns
import itertools
import matplotlib.pylab as plt

#Read and store the Feature Matrices

script_file_names = ["Devanagari", "Nandinagari", "Brahmi", "Meitei", "Telugu", "Gujarati", "Malayalam", "Kannada", "Tamil", "Modi", "Bengali", "Gurmukhi"]
script_file_names_n = len(script_file_names)
print("total number of hardcoded script names = ", script_file_names_n)

script_combination_list = []

# for L in range(script_file_names_n+1):
#     for subset in itertools.combinations(script_file_names, L):
#         if len(subset) == 2:
#             script_combination_list.append(subset)

for subset in itertools.combinations(script_file_names, 2):
        script_combination_list.append(subset)

print(script_combination_list)

def similarity_matrix_calc(init_matrix_1, init_matrix_2):
    similarity_matrix = np.zeros([init_matrix_1.shape[0], init_matrix_2.shape[0]])
    for i in range(init_matrix_1.shape[0]):
        for j in range(init_matrix_2.shape[0]):
            count = 0
            for k in range(init_matrix_1.shape[1]):
                if init_matrix_1[i,k]==init_matrix_2[j,k]:
                    count += 1
            similarity_matrix[i,j] = count

    return similarity_matrix

for i in script_combination_list:
    file_name_1 = i[0]
    file_name_2 = i[1]

    reader = csv.reader(open(file_name_1+".csv", "r"), delimiter=",")
    x = list(reader)
    script1 = np.array(x).astype("int")

    reader = csv.reader(open(file_name_2+".csv", "r"), delimiter=",")
    x = list(reader)
    script2 = np.array(x).astype("int")

    init_matrix_1 = script1
    init_matrix_2 = script2

    sm = similarity_matrix_calc(init_matrix_1, init_matrix_2)
    plt.style.use("seaborn-v0_8")
    plt.figure(figsize=(10, 10))
    heatmap = sns.heatmap(sm, linewidth=1, annot=True, cmap="coolwarm")
    heatmap.set(xlabel=file_name_2, ylabel=file_name_1)
    heatmap.figure.savefig(file_name_2+"_"+file_name_1+".png")