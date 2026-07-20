# Start_codon_&_Stop_codon_determination
Start codon and stop codon is determined from a DNA sequence taking from User. 
BIOLOGICAL SIGNIFICANCE:
The start codon signals the initiation of protein translation and indicates the start of a protein-coding region.
The stop codons signal the termination of protein translation and indicate the end of a protein-coding region. 
The determination of stop codon helps to identify the gene ending point. 
INPUT: 
DNA sequence from user.
On terminal
         Enter the DNA Sequence: 
OUTPUT:
If DNA sequence is not in proper codon form: 
On terminal
        WARNING!!!, DNA SEQUENCE LENGTH IS NOT IN PROPER CODON LENGTH
If DNA contains a start codon:
On terminal:
      Enter the DNA Sequence: atgaac 
      Start codon present in the DNA seq at position 0
      No stop codon found
If DNA contains a stop codon:
On terminal:
      Enter the DNA Sequence: ttcgatacttaa
      Stop codon present in the DNA seq at position 9
      No start codon found
If both start codon and stop codon are present:
      Enter the DNA Sequence: atgcatgctagataa
      Start codon present in the DNA seq at position 0
      Stop codon present in the DNA seq at position 12
No stop codon found:
On terminal:
      No stop codon found
CODE WORKING:
The code takes DNA sequence from the user and make it in Upper case and remove all the white spaces.
The code checks for the DNA sequence length to determine if proper codons can be formed.
If the DNA sequence length is not divisible by 3 warning and does not perform codon determination analysis.
If formed it checks for the codons from the flag variable and shows the exact location of the start codon and stop codon.
If after checking the whole length no stop codon or start codon is present. 
If the start codon is present the exact position of start codon on the terminal. 
If the start codon is present the exact position of start codon on the terminal. 
The terminal shows no stop codon found, no start codon found and terminates the program. 
