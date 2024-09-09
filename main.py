from astropy.table import Table
import matplotlib.pyplot as plt


# Read the spectra_list
spectra_list = Table.read("spectra_list.csv", format ="ascii.csv")


filenames = spectra_list['filename']




spectra = [Table.read(fr"C:\Users\damia\Documents\GitHub\ALOP-PROBLEM-1\spectra\{filename}", format ="ascii.csv") for filename in filenames]


wavelengths_list = [data['wavelength'] for data in spectra]
fluxes_list = [data['flux'] for data in spectra]


# Loop through the first three files
for i in range(3):
    # Filter data where wavelength is between 3000 and 9000
    mask = (wavelengths_list[i] >= 3000) & (wavelengths_list[i] <= 9000)
    plt.plot(wavelengths_list[i][mask], fluxes_list[i], label=(filenames[i][mask], os.path.splitext(filenames[i])[0])

# Adding labels and title
plt.xlabel('Wavelength')
plt.ylabel('Flux')
plt.title('First Three Spectra')
plt.legend()  # Display the legend
plt.grid(True)  # Add a grid for better readability

# Show the plot
plt.show()