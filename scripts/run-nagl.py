from openff.toolkit import Molecule, RDKitToolkitWrapper, AmberToolsToolkitWrapper
from openff.nagl.toolkits import NAGLRDKitToolkitWrapper
from openff.toolkit.utils.nagl_wrapper import NAGLToolkitWrapper
from openff.toolkit.utils.toolkit_registry import toolkit_registry_manager, ToolkitRegistry

# Note whether or not you explicitly pass NAGLRDKitToolkitWrapper this issue still occurs
amber_rdkit = ToolkitRegistry([RDKitToolkitWrapper(), AmberToolsToolkitWrapper(), NAGLRDKitToolkitWrapper()])

with toolkit_registry_manager(amber_rdkit):
    m = Molecule.from_smiles('CCC')
    m.assign_partial_charges(
        partial_charge_method="openff-gnn-am1bcc-0.1.0-rc.1.pt",
        toolkit_registry=NAGLToolkitWrapper(),
    )
    print(m)
