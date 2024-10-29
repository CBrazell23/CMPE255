import pandas as pd
import statistics

data = pd.read_csv('20164.csv')

# Net Inpatient Revenue formula = [GrossInpatientRevenueTotal ÷ (GrossInpatientRevenueTotal + GrossOutpatientRevenueTotal)] * NetPatientRevenueTotal
# CSV Form: [GRIP_TOT ÷ (GRIP_TOT + GROP_TOT)] * NET_TOT

# Net Outpatient Revenue formula = [GrossOutpatientRevenueTotal ÷ (GrossInpatientRevenueTotal + GrossOutpatientRevenueTotal)] * NetPatientRevenueTotal
# CSV Form: [GROP_TOT ÷ (GRIP_TOT + GROP_TOT)] * NET_TOT

grossInpatientRevenueTotal = data['GRIP_TOT'].tolist()
grossOutpatientRevenueTotal = data['GROP_TOT'].tolist()
netPatientRevenueTotal = data['NET_TOT'].tolist()
totalInpatients = data['DIS_TOT'].tolist()
totalOutpatients = data['VIS_TOT'].tolist()

grossInpatientRevenueTotalCleaned = []
sum = 0
numHospitalsWithData = 0
for x in grossInpatientRevenueTotal:
  x = x.replace(" ", "")
  x = x.replace(",", "")
  if x != '0':
    grossInpatientRevenueTotalCleaned.append(int(x))
    sum += int(x)
    numHospitalsWithData += 1
  else:
    grossInpatientRevenueTotalCleaned.append(0)

meanGrossInpatientRevenueTotal = sum / numHospitalsWithData

grossInpatientRevenueTotalReplaced = []

for x in grossInpatientRevenueTotalCleaned:
  if x == 0:
    grossInpatientRevenueTotalReplaced.append(round(meanGrossInpatientRevenueTotal))
  else:
    grossInpatientRevenueTotalReplaced.append(x)



grossOutpatientRevenueTotalCleaned = []
sum = 0
numHospitalsWithData = 0
for x in grossOutpatientRevenueTotal:
  x = x.replace(" ", "")
  x = x.replace(",", "")
  if x != '0':
    grossOutpatientRevenueTotalCleaned.append(int(x))
    sum += int(x)
    numHospitalsWithData += 1
  else:
    grossOutpatientRevenueTotalCleaned.append(0)

meanGrossOutpatientRevenueTotal = sum / numHospitalsWithData

grossOutpatientRevenueTotalReplaced = []

for x in grossOutpatientRevenueTotalCleaned:
  if x == 0:
    grossOutpatientRevenueTotalReplaced.append(round(meanGrossOutpatientRevenueTotal))
  else:
    grossOutpatientRevenueTotalReplaced.append(x)



netPatientRevenueTotalCleaned = []
sum = 0
numHospitalsWithData = 0
for x in netPatientRevenueTotal:
  x = x.replace(" ", "")
  x = x.replace(",", "")
  if x != '0':
    netPatientRevenueTotalCleaned.append(int(x))
    sum += int(x)
    numHospitalsWithData += 1
  else:
    netPatientRevenueTotalCleaned.append(0)

meanNetPatientRevenueTotal = sum / numHospitalsWithData

netPatientRevenueTotalReplaced = []

for x in netPatientRevenueTotalCleaned:
  if x == 0:
    netPatientRevenueTotalReplaced.append(round(meanNetPatientRevenueTotal))
  else:
    netPatientRevenueTotalReplaced.append(x)



totalInpatientCleaned = []
sum = 0
numHospitalsWithData = 0
for x in totalInpatients:
  x = x.replace(" ", "")
  x = x.replace(",", "")
  if x != '0':
    totalInpatientCleaned.append(int(x))
    sum += int(x)
    numHospitalsWithData += 1
  else:
    totalInpatientCleaned.append(0)

meanTotalInpatientCleaned = sum / numHospitalsWithData

totalInpatientReplaced = []

for x in totalInpatientCleaned:
  if x == 0:
    totalInpatientReplaced.append(round(meanTotalInpatientCleaned))
  else:
    totalInpatientReplaced.append(x)



totalOutpatientCleaned = []
sum = 0
numHospitalsWithData = 0
for x in totalOutpatients:
  x = x.replace(" ", "")
  x = x.replace(",", "")
  if x != '0':
    totalOutpatientCleaned.append(int(x))
    sum += int(x)
    numHospitalsWithData += 1
  else:
    totalOutpatientCleaned.append(0)

meanTotalOutpatientCleaned = sum / numHospitalsWithData

totalOutpatientReplaced = []

for x in totalOutpatientCleaned:
  if x == 0:
    totalOutpatientReplaced.append(round(meanTotalOutpatientCleaned))
  else:
    totalOutpatientReplaced.append(x)

    

netInpatientRevenueSum = 0
for i in range(len(grossInpatientRevenueTotalReplaced)):
  netInpatientRevenueSum += (grossInpatientRevenueTotalReplaced[i] / (grossInpatientRevenueTotalReplaced[i] + grossOutpatientRevenueTotalReplaced[i]) * netPatientRevenueTotalReplaced[i])
netInpatientRevenueAvg = netInpatientRevenueSum / len(grossInpatientRevenueTotalReplaced)

netOutpatientRevenueSum = 0
for i in range(len(grossOutpatientRevenueTotalReplaced)):
  netOutpatientRevenueSum += (grossOutpatientRevenueTotalReplaced[i] / (grossOutpatientRevenueTotalReplaced[i] + grossInpatientRevenueTotalReplaced[i]) * netPatientRevenueTotalReplaced[i])
netOutpatientRevenueAvg = netOutpatientRevenueSum / len(grossOutpatientRevenueTotalReplaced)

print(netInpatientRevenueAvg / statistics.mean(totalInpatientReplaced))
print(netOutpatientRevenueAvg / statistics.mean(totalOutpatientReplaced))
