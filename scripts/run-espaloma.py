from rdkit import Chem
from openff.toolkit import Molecule, RDKitToolkitWrapper, AmberToolsToolkitWrapper
from openff.toolkit.utils.toolkit_registry import toolkit_registry_manager, ToolkitRegistry
from espaloma_charge.openff_wrapper import EspalomaChargeToolkitWrapper

# Note whether or not you explicitly pass NAGLRDKitToolkitWrapper this issue still occurs
amber_rdkit = ToolkitRegistry([RDKitToolkitWrapper(), AmberToolsToolkitWrapper()])

m = Molecule.from_smiles('CN')

with toolkit_registry_manager(amber_rdkit):
    print(m.partial_charges)
    m.assign_partial_charges(
        partial_charge_method="espaloma-am1bcc",
        toolkit_registry=EspalomaChargeToolkitWrapper(),
    )
    print(m.partial_charges)
