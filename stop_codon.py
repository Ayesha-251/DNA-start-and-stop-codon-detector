#Determining the stop codon present in the given DNA Sequence
DNA=input("Enter the DNA Sequence: ").upper().strip()
stop_codon_found=False
stop_codons=["TAG", "TGA", "TAA"]
if len(DNA)%3 !=0:
    print("WARNING!!!, DNA SEQUENCE LENGTH IS NOT IN PROPER CODON LENGTH")  
else:
    for i in range(0, len(DNA), 3):
        if DNA[i:i+3] in stop_codons:
            print(f"Stop codon present in the DNA seq at position {i}")
            stop_codon_found=True
    if not stop_codon_found:
        print("No stop codon found")
