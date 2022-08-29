import numpy as np

sequence_1 = input('Enter the first sequence: ')
sequence_2 = input('Enter the second sequence: ')

if sequence_1 and sequence_2 not in ['A','T','G','C']:
    raise ValueError('Please enter a proper sequnece')

match_score = 1
mismatch_penalty = -1
gap_penalty = -2

total_score = 0

seq1 = len(sequence_1)
seq2 = len(sequence_2)

main_matrix = np.zeros((seq1+1,seq2+1),dtype=int)
match_mismatch = np.zeros((seq1,seq2),dtype=int)

for i in range(seq1):
    for j in range(seq2):

        if sequence_1[i] == sequence_2[j]:
            match_mismatch[i][j] = match_score
        
        else:
            match_mismatch[i][j] = mismatch_penalty

for i in range(seq1+1):
    main_matrix[i][0] = i*gap_penalty

for j in range(seq2+1):
    main_matrix[0][j] = j*gap_penalty

for i in range(1,seq1+1):
    for j in range(1,seq2+1):

        main_matrix[i][j] = max(main_matrix[i-1][j-1] + match_mismatch[i-1][j-1],
                                main_matrix[i-1][j] + gap_penalty,
                                main_matrix[i][j-1] + gap_penalty)

aligned1 = ''
aligned2 = ''

while (seq1 > 0 and seq2 > 0):

    if (seq1 > 0 and seq2 > 0 and main_matrix[seq1][seq2] == main_matrix[seq1-1][seq2-1] + match_mismatch[seq1-1][seq2-1]):

        aligned1 += sequence_1[seq1-1] 
        aligned2 += sequence_2[seq2-1]

        seq1 -= 1
        seq2 -= 1
    
    elif(seq1 > 0 and main_matrix[seq1][seq2] == main_matrix[seq1-1][seq2] + gap_penalty):

        aligned1 += sequence_1[seq1-1] 
        aligned2 += '_'

        total_score += gap_penalty
        seq1 -= 1
    
    else:

        aligned1 += '_'
        aligned2 += sequence_2[seq2-1]

        total_score += gap_penalty
        seq2 -= 1

print(aligned1[::-1])
print(aligned2[::-1])
    




