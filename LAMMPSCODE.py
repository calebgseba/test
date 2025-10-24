import numpy as np
import lammps

# Create an LAMMPS instance
lmp = lammps('example.lammpstr', 'style_x86/atom')

# Initialize simulation
lmp.init_style('MD')
lmp.set_periodic(True)
lmp.set_timestep(1e-14)  # fs

# Define the box dimensions
box_size = [10, 10, 10]
lmp.create_box(box_size)

# Add atoms and molecules to the simulation
atoms = [
    ('H', [0, 0, 0], 'solute'),
    ('O', [1.5, 2.5, 3.5], 'solute')
]
molecules = [('H2O', atoms)]
lmp.add_atoms(atoms)
lmp.add_molecules(molecules)

# Equilibration run
lmp.equil(100, 2000)  # 100 steps of MD, 2000 fs total

# Print simulation statistics
print(lmp.get_stats())

# Finalize the simulation
lmp.finalize()