from rdkit import Chem
from openff.toolkit import Molecule, RDKitToolkitWrapper, AmberToolsToolkitWrapper
from openff.nagl.toolkits import NAGLRDKitToolkitWrapper
from openff.toolkit.utils.nagl_wrapper import NAGLToolkitWrapper
from openff.toolkit.utils.toolkit_registry import toolkit_registry_manager, ToolkitRegistry

# Note whether or not you explicitly pass NAGLRDKitToolkitWrapper this issue still occurs
amber_rdkit = ToolkitRegistry([RDKitToolkitWrapper(), AmberToolsToolkitWrapper()])

supp = Chem.SDMolSupplier("datafiles/CN.sdf", removeHs=False)

m = [Molecule.from_rdkit(i) for i in supp][0]

with toolkit_registry_manager(amber_rdkit):
    m.assign_partial_charges(
        partial_charge_method="openff-gnn-am1bcc-0.1.0-rc.1.pt",
        toolkit_registry=NAGLToolkitWrapper(),
    )
    print(m)
