fileInput = open("..\dataFiles\sequence-cHBV.fasta", "r")
cHBV = ""
for line in fileInput:
	if line[0]== ">":
		continue
	cHBV += line[0:-1]
print(cHBV)
print(len(cHBV))
#90bp :)

startCodons = ["ATG"]
StartCodonFile = open("cHBV_startCodonIndices.txt", 'w')
startcodonCount = 0
for startCodon in startCodons:
	i =0
	while i < len(cHBV) - 2:
		iCodon = cHBV[i:i+3]
		if iCodon == startCodon:
			startcodonCount += 1
			StartCodonFile.write('Start ATG Codon at ' + str(i) + '.\n')
			print("Found start codon", iCodon, "at index", i)
		i += 1
print("The total number of start codons found in the DNA sequence is:", str(startcodonCount))
StartCodonFile.write('The total number of start codons is ' + str(startcodonCount) + '.\n')

StartCodonFile.close()



stopCodons = ['TAG', 'TGA', 'TAA']
StopCodonFile = open("cHBV_stopCodonIndices.txt", 'w')
stopcodonCount = 0
for stopCodon in stopCodons:
	i = 0
	while i < len(cHBV) - 2:
		iCodon = cHBV[i:i+3]
		if iCodon == stopCodon:
			stopcodonCount += 1
			print("Found stop codon", iCodon, "at index", i)
			StopCodonFile.write("Stop Codon at index " + str(i) + '.\n')
		i += 1
print("The total number of stop codons found in the DNA sequence is:", str(stopcodonCount))
StopCodonFile.write('The total number of stop codons is ' + str(stopcodonCount) + '.\n')
