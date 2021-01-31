import seaborn as sns
import matplotlib.pyplot as plt

read_lengths = []
path_to_file = input('Enter path to your fastq file: ')

with open(path_to_file) as fastq_file:

    # Collecting data

    line_count = 0
    for line in fastq_file:
        line_count += 1
    fastq_file.seek(0)

    for i in range(int(line_count / 4)):
        fastq_file.readline()
        sequence = fastq_file.readline()
        read_lengths.append(len(sequence) - 1)
        fastq_file.readline()
        fastq_file.readline()

    # Check for distribution presence

    if max(read_lengths) == min(read_lengths):
        print('There is no read length distribution in your fastq file')
        print('All reads\' length is the same and equals', read_lengths[110], 'bp')
    else:
        # Plotting and customization
        optimal_bin_width = (max(read_lengths) - min(read_lengths)) / 50
        sns.histplot(read_lengths, kde=True, binwidth=optimal_bin_width)
        plt.xlabel("Read length, bp", fontsize=12)
        plt.ylabel("")
        plt.title('Read length distribution', fontsize=18)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.show()
