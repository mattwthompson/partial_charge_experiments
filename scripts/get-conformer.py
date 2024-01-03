import pathlib

from rdkit import Chem
from openff.units import unit
from openff.toolkit import Molecule
from openff.toolkit.utils import rdkit_wrapper

supp = Chem.SDMolSupplier("datafiles/hif2a.sdf", removeHs=False)

rdmols = [mol for mol in supp]

pathlib.Path("./conformers").mkdir(parents=True, exist_ok=True)

for m in rdmols:
    mol = Molecule.from_rdkit(m)
    mol._conformers = None
    mol.generate_conformers(
        n_conformers=1,
        rms_cutoff=0.25 * unit.angstrom,
        toolkit_registry=rdkit_wrapper.RDKitToolkitWrapper(),
    )

    rdmol = mol.to_rdkit()

    with Chem.SDWriter(f'conformers/{mol.name}.sdf') as writer:
        writer.write(rdmol, confId=0)
