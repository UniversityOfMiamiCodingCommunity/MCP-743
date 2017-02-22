# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################
fileInput = open("/Users/SamuelDelOlio/GitHub/MCP-743/dataFiles/sequence-p53.fasta", "r")
dna = ""
for line in fileInput:
	dna += line[0:-1]
print(dna)

# 2)
# Find all possible start codons in parsed DNA sequence.

startCodon = "ATG"
i = 0
while i < len(dna)-2:
	iCodon = dna[i:i+3]
	if iCodon == startCodon:
		print("Start Codon Found at Index:", i)
	i += 1

#startCodonCount = dna.count(startCodon)
#print(startCodonCount)	

# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################





