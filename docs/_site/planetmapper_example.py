import glob
import planetmapper

for path in sorted(glob.glob('../Data/JWST/*.fits')):
    # Running from Python allows you to customise SPICE settings like the aberration correction
    observation = planetmapper.Observation(path, aberration_correction='CN+S')

    # Run some custom setup
    observation.add_other_bodies_of_interest('Io', 'Europa', 'Ganymede', 'Callisto')
    observation.set_plate_scale_arcsec(42) # set a custom plate scale
    observation.rotation_from_wcs() # get the disc rotation from the header's WCS info

    # Run the GUI to fit the observation interactively
    # This will open a GUI window every loop
    coords = observation.run_gui()

    # More custom code can go here to use the fitted observation...
    # for example, we can print some values for the last click location
    if coords:
        x, y = coords[-1]
        print(observation.xy2lonlat(x, y))