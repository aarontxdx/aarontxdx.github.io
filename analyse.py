import matplotlib.pyplot as plt
import numpy as np

def readFile(fileName):
    # Datei öffnen und Daten einlesen
    with open(fileName, 'r') as f:
        lines = f.readlines()

    # Index of Difficulty (IoD) und Bewegungszeit in separate Listen speichern
    iod_values = []
    bewegungszeit_values = []

    # Daten verarbeiten
    for i in range(3, 13):
        iod_values.append(float(lines[i]))
    for i in range(15, 25):
        bewegungszeit_values.append(int(lines[i]))

    return iod_values, bewegungszeit_values

def calculate_slope(x, y):
    """
    Berechnet die Steigung der Regressionsgeraden aus den gegebenen Arrays x und y.

    Args:
        x (numpy.ndarray): Array mit den X-Werten.
        y (numpy.ndarray): Array mit den Y-Werten.

    Returns:
        float: Die Steigung der Regressionsgeraden.
    """
    slope, yAchse = np.polyfit(x, y, 1)
    return slope, yAchse

iodDavidLayout1 = []
bwgDavidLayout1 = []
iodDavidLayout2 = []
bwgDavidLayout2 = []

iodAaronLayout1 = []
bwgAaronLayout1 = []
iodAaronLayout2 = []
bwgAaronLayout2 = []

for i in range(1, 21):
    iod_values, bwg_values = readFile('results/resultsLayout1David/result-' + str(i) + '.txt')
    iodDavidLayout1 = iodDavidLayout1 + iod_values
    bwgDavidLayout1 = bwgDavidLayout1 + bwg_values
for i in range(1, 21):
    iod_values, bwg_values = readFile('results/resultsLayout2David/result-' + str(i) + '.txt')
    iodDavidLayout2 = iodDavidLayout2 + iod_values
    bwgDavidLayout2 = bwgDavidLayout2 + bwg_values

for i in range(1, 21):
    iod_values, bwg_values = readFile('results/resultsLayout1Aaron/result-' + str(i) + '.txt')
    iodAaronLayout1 = iodAaronLayout1 + iod_values
    bwgAaronLayout1 = bwgAaronLayout1 + bwg_values
for i in range(1, 21):
    iod_values, bwg_values = readFile('results/resultsLayout2Aaron/result-' + str(i) + '.txt')
    iodAaronLayout2 = iodAaronLayout2 + iod_values
    bwgAaronLayout2 = bwgAaronLayout2 + bwg_values

allIod = iodDavidLayout1 + iodAaronLayout1
allBwg = bwgDavidLayout1 + bwgAaronLayout1
slope, yAchse = calculate_slope(allIod, allBwg)

regX = []
regY = []
for i in range(0,6):
    regX.append(i)
    regY.append(yAchse + slope*i)

plt.plot(regX, regY, color='red')
plt.scatter(allIod, allBwg, color='b', marker='o')



# Achsenbeschriftungen
plt.xlabel('ID')
plt.ylabel('MT')

# Titel
plt.title('Regressionsgerade Layout 1')

# Gitterlinien
plt.grid(True)

# Anzeigen
plt.show()
