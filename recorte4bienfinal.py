# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:26:23 2024

@author: pablo
"""
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib.pyplot as plt
import numpy as np
import os


def read_coordinates_from_file(ra_file, dec_file):
    with open(ra_file, 'r') as ra_file:
        ra_list = [float(line.strip()) for line in ra_file.readlines()]

    with open(dec_file, 'r') as dec_file:
        dec_list = [float(line.strip()) for line in dec_file.readlines()]

    return ra_list, dec_list

def create_stamps(fits_file, ra_list, dec_list):
    # Open FITS file and obtain WCS information
    hdul = fits.open(fits_file)
    wcs = WCS(hdul[0].header)
    data = hdul[0].data

    # Create PRUEBA21 folder if it doesn't exist
    output_folder = "RECORTE4BIEN"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define stamp size
    stamp_size = 140

    # Create stamps for each RA, DEC
    for i, (ra, dec) in enumerate(zip(ra_list, dec_list), 1):
        # Convert RA, DEC to pixel coordinates
        x, y = wcs.all_world2pix(ra, dec, 0)

        # Extract stamp from the data
        stamp = data[int(y - stamp_size):int(y + stamp_size), int(x - stamp_size):int(x + stamp_size)]

        # Apply different stretches to enhance brightness and contrast
        stretches = [ np.arcsinh(stamp * 10) / 3 ,
                     np.arcsinh(stamp),
                     np.sqrt(np.maximum(stamp, 0)),  # Ensure no negative values for square root
                     np.cbrt(stamp)]

        # Create a subplot with 2 rows and 2 columns for the 4 stamps
        fig, axs = plt.subplots(2, 2, figsize=(8, 8), squeeze=False, gridspec_kw={'hspace': 0, 'wspace': 0})

        # Loop through stretches and plot each one in a subplot
        for j, stretched_stamp in enumerate(stretches, 0):
            # Display the image in the corresponding subplot
            ax = axs[j//2, j%2]
            ax.imshow(stretched_stamp, cmap='gray', origin='lower', extent=(-stamp_size, stamp_size, -stamp_size, stamp_size))
            ax.axis('off')

        # Set a title for the entire figure
        fig.suptitle(f'Image {i} - RA: {ra}, DEC: {dec}')

        # Save the figure with RA and DEC in the filename
        ra_str = str(ra).replace(".", "_")
        dec_str = str(dec).replace(".", "_")
        output_file = os.path.join(output_folder, f'image_{i}_RA_{ra_str}_DEC_{dec_str}.jpeg')
        plt.savefig(output_file, format='jpeg', dpi=400, bbox_inches='tight', pad_inches=0)  # Save as JPEG
        plt.close()  # Close the figure for the next iteration

    # Close FITS file
    hdul.close()
    
    
if __name__ == "__main__":
    fits_file_path = r"\Users\pablo\OneDrive\Escritorio\Apuntes\TFG2\abell2744clu-grizli-v7.0-f200w-clear_drc_sci.fits"
    ra_file_path = r"\Users\pablo\OneDrive\Escritorio\Apuntes\TFG2\ar.txt"
    dec_file_path = r"\Users\pablo\OneDrive\Escritorio\Apuntes\TFG2\dec.txt"

    ra_list, dec_list = read_coordinates_from_file(ra_file_path, dec_file_path)
    create_stamps(fits_file_path, ra_list, dec_list)
