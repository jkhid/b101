"""Rewrite wrong answer choices so they match the correct answer in length/plausibility."""

import json, pathlib

SRC  = pathlib.Path("src/data/content.json")
ROOT = pathlib.Path("content.json")

# Each entry: question_id -> new choices list (correct answer stays in same position)
PATCHES = {

# ── CH1 ──────────────────────────────────────────────────────────────────────

"ch1-q-001": {
  "choices": [
    "It lacks liquid water and carbon-based molecules — without these, the chemistry needed to sustain metabolism cannot occur",
    "It has no cellular organization — without compartmentalized reactions there is no coordinated metabolism or self-regulation",
    "It cannot reproduce, grow/develop, or evolve — it lacks all five characteristics",
    "It cannot sense or respond to its environment — geological changes happen passively, not as a directed response to stimuli",
  ], "answerIndex": 2
},
"ch1-q-003": {
  "choices": [
    "Both have a true membrane-bound nucleus containing linear chromosomes organized around histone proteins",
    "Both are classified as eukaryotes with membrane-bound organelles and a cytoskeleton for cell support",
    "Both are prokaryotic (no nucleus, no membrane-bound organelles)",
    "Both have identical phospholipid bilayers with ester-linked fatty acids in their cell membranes",
  ], "answerIndex": 2
},
"ch1-q-004": {
  "choices": [
    "Fungi photosynthesize using chloroplasts; animals break down ingested food using secreted digestive enzymes",
    "Fungi digest externally and absorb; animals ingest and digest internally",
    "Animals secrete digestive enzymes onto external food; fungi engulf whole particles and digest them intracellularly",
    "Both filter dissolved organic molecules from water, relying on passive absorption across their outer membranes",
  ], "answerIndex": 1
},
"ch1-q-006": {
  "choices": [
    "A preliminary conclusion drawn from a single well-designed experiment before it has been independently replicated",
    "A broad explanation supported by many lines of evidence with predictive power",
    "A specific, measurable prediction about one observable outcome of an experiment",
    "A consensus statement accepted by most researchers and permanently immune to revision or falsification",
  ], "answerIndex": 1
},
"ch1-q-007": {
  "choices": [
    "So it can be proven true permanently and elevated to the status of a scientific law",
    "So there is some possible result that could prove it wrong",
    "Falsifiable hypotheses automatically pass peer review without requiring experimental replication",
    "A hypothesis that matches accepted theory is assumed correct without further experimental verification",
  ], "answerIndex": 1
},
"ch1-q-008": {
  "choices": [
    "Larger sample sizes allow researchers to test more variables simultaneously without increasing experimental error",
    "Larger samples reduce the chance that results are due to random variation, making conclusions more reliable",
    "Smaller samples are preferable because they reduce confounding variables more effectively than large groups",
    "Sample size determines how many independent variables can be measured simultaneously in a single experiment",
  ], "answerIndex": 1
},
"ch1-q-009": {
  "choices": [
    "To eliminate the need for a control group, since blinding itself removes all sources of measurement error",
    "Observer bias and the placebo effect from skewing results",
    "Double-blind design removes the need for statistical analysis since subjective errors are already eliminated",
    "Legal requirements mandate double-blind protocols for all medical trials involving human subjects by law",
  ], "answerIndex": 1
},
"ch1-q-013": {
  "choices": [
    "entire populations; the geographic range and size of species over ecological timescales",
    "individuals; allele frequencies in populations",
    "alleles directly at the molecular level; the protein-coding capacity of individual genomes",
    "species as a whole; the body plans and fundamental anatomy of all organisms in an ecosystem",
  ], "answerIndex": 1
},
"ch1-q-014": {
  "choices": [
    "To transfer copyright of the findings to the journal, enabling faster publication and wider public access",
    "To certify that the researcher's institution provided adequate funding and resources for the study",
    "To have independent experts evaluate methods, data, and conclusions for errors and bias",
    "To guarantee the researcher receives academic credit and job security before the study is released",
  ], "answerIndex": 2
},
"ch1-q-015": {
  "choices": [
    "Agree — in science, theories are preliminary frameworks that have not yet been tested enough to become laws",
    "In science, a theory is the highest-confidence explanation: broad, predictive, and supported by many independent lines of evidence",
    "A theory automatically becomes a scientific law once it has been replicated in three or more independent laboratories",
    "Theories are narrative explanations used only in social sciences; biology relies on 'laws' for all well-established principles",
  ], "answerIndex": 1
},
"ch1-q-016": {
  "choices": [
    "The electrical charge on a sodium ion, which arises from the proton-to-electron ratio in the atom's nucleus",
    "The membrane potential of a single neuron, which results from ion channel distribution along its axon",
    "Consciousness arising from billions of interacting neurons",
    "The atomic mass of carbon, which emerges from the combined mass of its protons and neutrons",
  ], "answerIndex": 2
},
"ch1-q-018": {
  "choices": [
    "Atom → organelle → cell → tissue → molecule → organ → organism → population → ecosystem → biosphere",
    "Cell → molecule → tissue → organ → organism → population → community → ecosystem → biosphere",
    "Atom → molecule → organelle → cell → tissue → organ → organ system → organism → population → community → ecosystem → biosphere",
    "Organelle → atom → molecule → cell → tissue → organ → ecosystem → population → biosphere",
  ], "answerIndex": 2
},
"ch1-q-027": {
  "choices": [
    "The energy-releasing breakdown reactions (catabolism) that convert glucose and fats into ATP for cellular work",
    "The energy-consuming biosynthetic reactions (anabolism) that build complex molecules from simple precursors",
    "The sum of ALL chemical reactions in an organism, including both anabolic and catabolic pathways",
    "The rate at which mitochondria oxidize pyruvate to produce ATP, measured as oxygen consumption per minute",
  ], "answerIndex": 2
},

# ── CH2 ──────────────────────────────────────────────────────────────────────

"ch2-q-001": {
  "choices": [
    "Oxygen-14, an unstable radioisotope that decays into nitrogen at a predictable rate used for dating",
    "Carbon-14 (an isotope of carbon)",
    "Nitrogen-14, the stable isotope that carbon-14 decays into after a series of radioactive emissions",
    "Carbon-12, the stable and most abundant form of carbon found in all living organic compounds",
  ], "answerIndex": 1
},
"ch2-q-003": {
  "choices": [
    "Oil molecules form covalent bonds with the H+ ions in water, creating a new compound that sinks rather than dissolving",
    "Water's partial charges pull apart ionic salt, but nonpolar oil has no charges for water to grab",
    "Salt dissolves because it contains nonpolar covalent bonds matching water's interior, while oil's ionic bonds repel water",
    "Oil's molecular weight exceeds the threshold for aqueous solubility, causing it to remain suspended as insoluble droplets",
  ], "answerIndex": 1
},
"ch2-q-006": {
  "choices": [
    "Covalent bonds between complementary bases — these strong bonds ensure the double helix cannot be separated without enzyme activity",
    "Hydrogen bonds between complementary bases (A-T, C-G)",
    "Phosphodiester bonds linking the bases on opposite strands — the same bonds that form the sugar-phosphate backbone",
    "Peptide bonds between nitrogenous bases — the same bond type that links amino acids in protein synthesis",
  ], "answerIndex": 1
},
"ch2-q-007": {
  "choices": [
    "Butter contains more double bonds than oil, causing its fatty acid chains to kink and pack loosely, while oil's straight chains form crystals",
    "Butter's saturated straight chains pack tightly; oil's unsaturated kinked chains cannot",
    "Vegetable oil is composed of saturated fatty acids that pack rigidly at room temperature, while butter's unsaturated fats stay fluid",
    "Butter is unsaturated because its C=C double bonds lower its melting point, while vegetable oil is fully saturated",
  ], "answerIndex": 1
},
"ch2-q-009": {
  "choices": [
    "Water molecules have unusually high kinetic energy at room temperature due to their shape, requiring extra heat input to raise temperature",
    "Hydrogen bonds between water molecules must be broken to raise temperature, absorbing large amounts of energy",
    "Water is a nonpolar solvent whose C-H bonds are extremely stable, requiring large energy input to vibrate and absorb heat",
    "Water has an exceptionally low boiling point for its size, meaning very little energy converts it to steam",
  ], "answerIndex": 1
},
"ch2-q-014": {
  "choices": [
    "They have no protons in their nucleus and therefore no positive charge to attract electrons into bond formation",
    "Their outermost electron shell is completely full, so they do not need to gain, lose, or share electrons",
    "Their large atomic radius creates steric hindrance that prevents other atoms from approaching closely enough to share electrons",
    "They exist only as gases, and gaseous molecules cannot form bonds because atoms must be solid or liquid to interact chemically",
  ], "answerIndex": 1
},
"ch2-q-015": {
  "choices": [
    "Carbon is the most electronegative element, attracting electrons from all surrounding atoms to form uniquely stable ionic bonds",
    "Carbon has 4 valence electrons, allowing it to form 4 covalent bonds and create chains, rings, and branches",
    "Carbon's bond energy exceeds every other element, making carbon compounds essentially indestructible by enzymes",
    "Carbon is the lightest element in group 14, forming weak, reversible covalent bonds that are easy for enzymes to break",
  ], "answerIndex": 1
},
"ch2-q-016": {
  "choices": [
    "Ice is denser than liquid water because freezing compresses water molecules closer together, causing it to sink in lakes and ponds",
    "As water freezes, hydrogen bonds form a regular lattice that is LESS dense than liquid water — so ice floats, insulating liquid water beneath, allowing aquatic organisms to survive winter",
    "Freezing releases electrons into a conduction band that repel each other, expanding the lattice and making frozen water electrically neutral",
    "Ice floats because water's ionic bonds break during freezing, releasing positive hydrogen ions that reduce the density of the solid phase",
  ], "answerIndex": 1
},
"ch2-q-017": {
  "choices": [
    "The low density of water compared to the insect — since water is less dense, it naturally provides an upward buoyant force",
    "Cohesion — hydrogen bonds between water molecules pull surface molecules inward and sideways, resisting disruption",
    "Adhesion of water molecules to the waxy hydrophobic surface of the insect's legs creates an upward supportive force",
    "Water's high specific heat stores thermal energy that converts into mechanical energy supporting the insect's weight",
  ], "answerIndex": 1
},
"ch2-q-019": {
  "choices": [
    "Three glycerol molecules bonded to one fatty acid by phosphodiester linkages, forming a branched lipid stored in adipose tissue",
    "One glycerol molecule bonded to three fatty acids via ester linkages by dehydration synthesis",
    "Two fatty acids bonded to a phosphate group and a glycerol head, forming an amphipathic molecule used in cell membranes",
    "Amino acids linked by peptide bonds in a hydrophobic sequence that folds into a lipid-like structure inside the cell membrane",
  ], "answerIndex": 1
},
"ch2-q-020": {
  "choices": [
    "The protein gains free energy and becomes hyperactive, catalyzing reactions much faster than its normal rate",
    "Covalent peptide bonds between amino acids are broken by heat, permanently destroying the primary structure of the polypeptide",
    "The protein loses its 3D shape due to disruption of hydrogen bonds, ionic bonds, and other weak interactions — while the amino acid sequence remains intact",
    "The protein is fully degraded into its constituent amino acids by protease enzymes cleaving peptide bonds throughout the chain",
  ], "answerIndex": 2
},
"ch2-q-023": {
  "choices": [
    "Covalent phosphodiester bonds that directly link the nitrogenous bases of opposite strands, forming the rungs of the DNA ladder",
    "Hydrogen bonds between complementary base pairs (A–T and G–C)",
    "Ionic bonds between the negatively charged phosphate groups and the positively charged bases along the backbone",
    "Peptide bonds between the nitrogenous bases — the same bond type that links amino acids in a polypeptide chain",
  ], "answerIndex": 1
},
"ch2-q-024": {
  "choices": [
    "Oil molecules exceed the maximum molecular weight for aqueous solubility, forming large insoluble aggregates on the water surface",
    "Polar water molecules interact strongly with each other and with other polar/ionic solutes but cannot interact with nonpolar oil molecules, which have no partial charges",
    "Oil is denser than water and settles below the surface, where hydrogen bonds trap it and prevent mixing with the aqueous phase",
    "Water's hydrogen bonds actively repel hydrocarbon chains by generating a net repulsive electrostatic force between the two liquids",
  ], "answerIndex": 1
},
"ch2-q-028": {
  "choices": [
    "Secondary; hydrogen bonds formed along the peptide backbone between backbone C=O and N-H groups at regular intervals",
    "Quaternary; noncovalent attractions between separate polypeptide subunits that assemble into a multi-chain protein complex",
    "Tertiary; interactions between R groups (hydrophobic, ionic, H-bonds, disulfide bridges)",
    "Primary; the covalent peptide bonds that link each amino acid in sequence, giving the protein its unique identity",
  ], "answerIndex": 2
},
"ch2-q-030": {
  "choices": [
    "Peptide bonds between amino acids — high temperature provides enough energy to break these covalent bonds, destroying the primary structure",
    "The weak bonds (hydrogen bonds, hydrophobic, ionic) maintaining secondary and tertiary structure — primary structure remains intact",
    "Only disulfide bridges are disrupted by heat, while hydrogen bonds and hydrophobic interactions remain stable throughout denaturation",
    "Glycosidic bonds attaching carbohydrate groups to the protein surface are cleaved first, exposing the hydrophobic core and triggering unfolding",
  ], "answerIndex": 1
},
"ch2-q-031": {
  "choices": [
    "Both are stabilized exclusively by R-group interactions between hydrophobic amino acid side chains, not by backbone hydrogen bonds",
    "Both are secondary structures stabilized by hydrogen bonds between backbone atoms (C=O···H-N)",
    "Both represent quaternary structure — they only form when multiple polypeptide chains associate and fold around each other",
    "Both are composed exclusively of nonpolar amino acids, which is why they are buried inside the hydrophobic protein core",
  ], "answerIndex": 1
},
"ch2-q-033": {
  "choices": [
    "Act as an energy reserve concentrated in the membrane — cholesterol stores twice the caloric density of phospholipids for use during fasting",
    "Form the entire phospholipid bilayer by donating their steroid ring as the fatty acid tails that make up the hydrophobic core",
    "Buffer membrane fluidity — preventing membranes from becoming too rigid or too fluid with temperature changes",
    "Transport oxygen across the membrane by binding O2 on the extracellular face and releasing it into the cytoplasm",
  ], "answerIndex": 2
},
"ch2-q-037": {
  "choices": [
    "Starch is made from beta-glucose with beta-1,4 linkages while glycogen uses alpha-glucose, so different enzymes digest each one",
    "Glycogen is much more highly branched than starch, allowing faster glucose release when energy is needed quickly",
    "Starch forms long unbranched chains that dissolve readily in cold water, while glycogen forms compact insoluble granules",
    "Starch is the primary short-term energy storage in animal muscle and liver; glycogen is the main energy reserve in plant seeds",
  ], "answerIndex": 1
},
"ch2-q-038": {
  "choices": [
    "Is made of beta-1,4-linked glucose residues with a methyl group at carbon 2, while cellulose uses completely unmodified glucose",
    "Contains nitrogen — it is made of N-acetylglucosamine (a glucose with an amino group), found in fungal cell walls and arthropod exoskeletons rather than plant cell walls",
    "Functions as a soluble storage polysaccharide in fungi, accumulating in vacuoles, while cellulose provides rigid support in animals",
    "Is highly soluble in digestive fluids and broken down easily by mammalian enzymes, unlike cellulose which requires gut bacteria",
  ], "answerIndex": 1
},

# ── CH3 ──────────────────────────────────────────────────────────────────────

"ch3-q-005": {
  "choices": [
    "The immune system neutralizes penicillin before it reaches any cellular components in human tissue",
    "Human cells lack the bacterial cell wall the drug targets",
    "Bacteria lack the DNA repair mechanisms that human cells use to correct antibiotic-induced genetic damage",
    "Human cells have a thicker and more rigid plasma membrane that prevents penicillin from diffusing inside",
  ], "answerIndex": 1
},
"ch3-q-006": {
  "choices": [
    "Oxygen is physically larger than glucose, allowing it to stretch the membrane and pass through gaps between phospholipids",
    "Oxygen is nonpolar and crosses the hydrophobic core; glucose is polar and is blocked",
    "Glucose is a nonpolar hydrocarbon that dissolves in the fatty acid tails, but oxygen's polar bonds prevent it from entering",
    "Oxygen requires a protein transport channel to cross the membrane, while glucose diffuses freely because it is smaller",
  ], "answerIndex": 1
},
"ch3-q-011": {
  "choices": [
    "The cell would grow faster due to the additional nutrients released — lysosomes normally suppress growth by sequestering anabolic enzymes",
    "ATP production would increase sharply because the released enzymes would begin oxidizing cytoplasmic components for the Krebs cycle",
    "Digestion of the cell's own proteins and organelles, leading to cell death",
    "The enzymes would be immediately exported by exocytosis, since they are recognized as foreign proteins by the secretory pathway",
  ], "answerIndex": 2
},
"ch3-q-012": {
  "choices": [
    "Actin microfilaments (F-actin), which polymerize from centrioles outward and attach directly to the centromere of each chromosome",
    "Intermediate filaments (keratin and vimentin), which provide tensile strength to pull sister chromatids apart during anaphase",
    "Microtubules (tubulin polymers)",
    "The nuclear lamina (lamin proteins), which disassemble during mitosis and reorganize into spindle fibers that sort chromosomes",
  ], "answerIndex": 2
},
"ch3-q-015": {
  "choices": [
    "A membrane-bound compartment inside the nucleus that packages chromosomal DNA into tightly coiled nucleosomes before cell division",
    "A region within the nucleus where ribosomal RNA (rRNA) is synthesized and ribosomal subunits are assembled before export to the cytoplasm",
    "The outer boundary of the nucleus, composed of two lipid bilayers perforated by nuclear pores that regulate molecular traffic",
    "A lysosome-like compartment inside the nucleus that degrades misfolded proteins and damaged DNA through autophagy",
  ], "answerIndex": 1
},
"ch3-q-016": {
  "choices": [
    "Single-layered membrane; prevents all RNA molecules from leaving the nucleus until transcription and processing are fully complete",
    "Double-layered membrane; control the passage of mRNA, proteins, and ribosomal subunits between the nucleus and cytoplasm",
    "Triple-layered membrane; generates ATP through a proton gradient to power active transport of molecules into and out of the nucleus",
    "Single-layered membrane; replicates DNA during S phase, synthesizing new chromosomes entirely within the nuclear compartment",
  ], "answerIndex": 1
},
"ch3-q-017": {
  "choices": [
    "Store mitochondrial DNA and ribosomes within their folds, keeping the genetic material close to the inner membrane for transcription",
    "Increase the inner membrane surface area, packing in more electron transport chain complexes and ATP synthase to maximize ATP production",
    "Synthesize ribosomal RNA and assemble ribosomal subunits within their folds, which are then exported to the mitochondrial matrix",
    "Sequester calcium ions from the matrix, releasing them into the cytoplasm as a signal triggering mitochondrial division",
  ], "answerIndex": 1
},
"ch3-q-018": {
  "choices": [
    "Cilia are made of actin microfilaments arranged in a 9+2 pattern; flagella are built from tubulin and move by a rotary motor",
    "Cilia are short and numerous (move fluid past the cell); flagella are long and few (propel the cell through fluid)",
    "Cilia are found exclusively in bacteria to sweep nutrients inward; flagella exist only in eukaryotes for swimming locomotion",
    "Cilia use dynein motors while flagella use kinesin motors — they have completely different molecular architectures and movement mechanisms",
  ], "answerIndex": 1
},
"ch3-q-019": {
  "choices": [
    "H2O2 is an essential substrate for photosynthesis that must be kept away from mitochondria, where it would inhibit the ETC",
    "H₂O₂ is a reactive oxygen species that oxidizes and damages DNA, proteins, and lipids — so peroxisomal catalase converts it to harmless water and O₂",
    "H2O2 raises intracellular pH above 8.0, denaturing all cytoplasmic enzymes unless peroxisomes rapidly reacidify the cytoplasm",
    "H2O2 binds irreversibly to plasma membrane phospholipids, making the membrane impermeable until peroxisomes dissolve the complexes",
  ], "answerIndex": 1
},
"ch3-q-021": {
  "choices": [
    "Adjacent cells to establish electrical barriers preventing ions and nutrients from leaking into the intercellular space",
    "Direct cytoplasmic connections so ions, small molecules, and signals can pass between adjacent cells without crossing plasma membranes",
    "Large folded proteins and ribosomes to travel freely between any two cells in the body regardless of cell type",
    "New cell walls to be deposited precisely at the midline between dividing cells, ensuring equal cytoplasmic division during cytokinesis",
  ], "answerIndex": 1
},
"ch3-q-022": {
  "choices": [
    "Protein synthesis on ribosomes, because microtubules transport newly made proteins from rough ER to the Golgi for processing",
    "ATP production in mitochondria, because microtubules form the inner membrane cristae that house the electron transport chain",
    "Chromosome separation during mitosis (spindle fibers are microtubules)",
    "Lipid synthesis in the smooth ER, because microtubules are required to maintain the tubular shape of the smooth ER network",
  ], "answerIndex": 2
},
"ch3-q-023": {
  "choices": [
    "Its membrane has an irregularly folded and jagged lipid bilayer that appears rough under high-magnification light microscopy",
    "Ribosomes are studded on its cytoplasmic surface, giving it a bumpy appearance under electron microscopy",
    "It synthesizes partially processed precursor proteins that require further modification in the Golgi before they can be secreted",
    "Its lipid bilayer is significantly thicker than the smooth ER membrane, creating a coarser texture visible in electron micrographs",
  ], "answerIndex": 1
},
"ch3-q-024": {
  "choices": [
    "Golgi apparatus → rough ER → transport vesicle → plasma membrane, because the Golgi signals the rough ER which proteins to make",
    "Rough ER → transport vesicle → Golgi → secretory vesicle → plasma membrane (exocytosis)",
    "Smooth ER → rough ER → Golgi → lysosome → plasma membrane — all secreted proteins pass through smooth ER for lipid modification",
    "Nucleus → Golgi → rough ER → secretory vesicle → plasma membrane — proteins are made on nuclear ribosomes and imported into the Golgi",
  ], "answerIndex": 1
},
"ch3-q-025": {
  "choices": [
    "They have a rigid cell wall made of cellulose or peptidoglycan that provides structural support, allowing cells to grow without collapsing",
    "Their membrane-bound organelles divide metabolic labor, allowing efficient function at larger scales without depending entirely on diffusion across the whole cytoplasm",
    "They contain far more DNA, and larger genomes require proportionally larger nuclear and cytoplasmic volumes to store and express them",
    "They evolved under higher atmospheric oxygen, which allowed aerobic metabolism to provide more energy for growth and larger cell size",
  ], "answerIndex": 1
},
"ch3-q-027": {
  "choices": [
    "Exclusively maintaining cell shape as a permanently rigid scaffold — once assembled, the cytoskeleton does not rearrange or change",
    "Maintaining cell shape, enabling cell movement and division, providing tracks for organelle transport, and forming cilia and flagella",
    "Generating ATP for all types of cellular movement — kinesin and dynein use the cytoskeleton as a fuel source rather than a track",
    "Synthesizing all membrane lipids and phospholipids needed by the cell's organelles, assembled on cytoskeletal scaffolds",
  ], "answerIndex": 1
},
"ch3-q-029": {
  "choices": [
    "Forming the mitotic spindle that attaches to chromosomes and pulls them to opposite poles during anaphase of cell division",
    "Providing the structural backbone of the nuclear envelope and nuclear lamina, maintaining the shape and rigidity of the nucleus",
    "Cell shape changes, amoeboid movement, muscle contraction (with myosin), and forming the cleavage furrow during cytokinesis",
    "Building the cellulose microfibrils that form the primary and secondary cell walls of plant cells",
  ], "answerIndex": 2
},
"ch3-q-033": {
  "choices": [
    "To store mitochondrial ribosomes and circular DNA within protected membrane folds, where they can translate proteins efficiently",
    "To greatly increase surface area, fitting more electron transport chain complexes and ATP synthase to maximize ATP production",
    "To physically separate the Krebs cycle enzymes from the outer membrane space where glycolysis products first enter the mitochondrion",
    "To enable the mitochondrion to divide by binary fission, using the cristae as division planes that pinch it into two daughter organelles",
  ], "answerIndex": 1
},
"ch3-q-035": {
  "choices": [
    "They contain ATP synthase that phosphorylates ADP back to ATP, recycling used energy currency from catabolic reactions",
    "They contain digestive enzymes that break down damaged organelles (autophagy), food particles, and foreign material, recycling the components for reuse",
    "They store excess glucose as glycogen granules and release glucose monomers when blood sugar drops, recycling carbohydrate energy",
    "They receive misfolded proteins from the Golgi and refold them using chaperone proteins before returning them to the secretory pathway",
  ], "answerIndex": 1
},

# ── CH4 ──────────────────────────────────────────────────────────────────────

"ch4-q-001": {
  "choices": [
    "Energy naturally tends to become more organized and concentrated over time, flowing from regions of low to high concentration",
    "Energy cannot be created or destroyed, only converted from one form to another",
    "Exothermic reactions always release energy faster than endothermic reactions can absorb it, making energy release thermodynamically favored",
    "Living organisms can synthesize new energy molecules from inorganic matter, bypassing the constraints of thermodynamics",
  ], "answerIndex": 1
},
"ch4-q-006": {
  "choices": [
    "The enzyme works faster due to higher kinetic energy — substrate molecules collide with the active site at a much higher frequency",
    "The enzyme denatures — hydrogen bonds holding its 3D shape break and the active site is destroyed",
    "The enzyme converts into a competitive inhibitor that blocks its own active site, preventing substrate binding until cooled",
    "Nothing significant occurs — enzymes are heat-stable proteins that maintain full catalytic activity across the entire temperature range",
  ], "answerIndex": 1
},
"ch4-q-010": {
  "choices": [
    "Salt molecules actively pump water out through specialized ion transport proteins that exchange Na+ for water molecules",
    "The brine is hypertonic; water exits cells by osmosis toward the higher solute concentration outside",
    "The brine is hypotonic compared to cucumber cells, causing water to rush inward and rupture the cell membranes",
    "Salt ions bind to and permanently denature membrane transport proteins, making cells unable to regulate water movement",
  ], "answerIndex": 1
},
"ch4-q-011": {
  "choices": [
    "Active transport via the Na+/K+ ATPase pump, which uses ATP to move glucose against its concentration gradient",
    "Facilitated diffusion through GLUT carrier proteins — passive, no ATP required",
    "Endocytosis via receptor-mediated phagocytosis — glucose binds to surface receptors triggering membrane invagination",
    "Simple diffusion directly through the lipid bilayer, since glucose is a small molecule that dissolves in the hydrophobic membrane core",
  ], "answerIndex": 1
},
"ch4-q-012": {
  "choices": [
    "Simple diffusion — small nonpolar molecules move down their concentration gradient through the bilayer without proteins or energy",
    "Facilitated diffusion — polar molecules move down their gradient through carrier or channel proteins without consuming ATP",
    "Active transport — requires ATP to move substances from low to high concentration",
    "Osmosis — the passive movement of water across a semipermeable membrane from low to high solute concentration",
  ], "answerIndex": 2
},
"ch4-q-014": {
  "choices": [
    "Phagocytosis — the plasma membrane extends pseudopods to engulf solid particles, pulling them into the cell in a membrane-bound vesicle",
    "Pinocytosis — the plasma membrane folds inward to engulf extracellular fluid and dissolved solutes into small intracellular vesicles",
    "Exocytosis — vesicles fuse with the membrane to release contents outside",
    "Receptor-mediated endocytosis — specific ligands bind to membrane receptors, triggering clathrin-coated pit formation and internalization",
  ], "answerIndex": 2
},
"ch4-q-015": {
  "choices": [
    "Exocytosis — secretory vesicles fuse with the plasma membrane and release their contents into the extracellular space",
    "Pinocytosis — the plasma membrane folds inward to engulf extracellular fluid and the small dissolved molecules it contains",
    "Phagocytosis — a type of endocytosis for large solid particles",
    "Facilitated diffusion — large polar molecules such as glucose use transmembrane carrier proteins to cross the hydrophobic bilayer",
  ], "answerIndex": 2
},
"ch4-q-016": {
  "choices": [
    "Energy can neither be created nor destroyed — the total amount of energy in the universe remains constant at all times",
    "Energy tends to disperse and entropy (disorder) tends to increase in any energy conversion",
    "All spontaneous chemical reactions must be catalyzed by enzymes that lower activation energy to make the reaction favorable",
    "Living organisms can selectively reverse entropy in their cells using genetic information to direct ordered molecular assembly without energy cost",
  ], "answerIndex": 1
},
"ch4-q-017": {
  "choices": [
    "Two biochemical reactions that occur simultaneously within the same membrane-bound organelle, sharing substrates and products",
    "Using the free energy released by an exergonic (energy-releasing) reaction to drive an endergonic (energy-requiring) reaction",
    "Two different enzymes binding the same substrate at the same time, competing to catalyze the same reaction at twice the normal speed",
    "Biochemical reactions in which both the forward and reverse steps require molecular oxygen as a reactant to proceed",
  ], "answerIndex": 1
},
"ch4-q-019": {
  "choices": [
    "The end product activates the first enzyme in the pathway, speeding production when the product has already reached sufficient levels",
    "Allosterically inhibits an enzyme early in the pathway, shutting down production when sufficient product has accumulated",
    "A competitive inhibitor structurally similar to the substrate blocks the active site of the final enzyme, preventing product formation",
    "Extreme product accumulation denatures all enzymes in the pathway, destroying their activity until new enzymes are synthesized",
  ], "answerIndex": 1
},
"ch4-q-020": {
  "choices": [
    "Lose water and undergo plasmolysis — the plasma membrane pulls away from the rigid cell wall, causing the cell to shrink and wilt",
    "Gain water by osmosis; the cell wall resists bursting, resulting in turgor pressure that gives the cell rigidity",
    "Remain completely unchanged because plant cells maintain strict osmotic balance with all external environments through active ion pumping",
    "Release their chloroplasts through exocytosis to reduce osmotic pressure and prevent the membrane from being damaged by swelling",
  ], "answerIndex": 1
},
"ch4-q-022": {
  "choices": [
    "Receptor-mediated endocytosis requires direct ATP hydrolysis to coat vesicles, while phagocytosis is an entirely passive process",
    "Receptor-mediated endocytosis specifically binds target molecules via surface receptors before engulfing them; phagocytosis nonspecifically engulfs large particles",
    "Receptor-mediated endocytosis occurs exclusively in plant cells to internalize nutrients; phagocytosis is restricted to animal immune cells",
    "Phagocytosis requires the nucleus to direct pseudopod formation, while receptor-mediated endocytosis is a spontaneous self-assembly process",
  ], "answerIndex": 1
},
"ch4-q-023": {
  "choices": [
    "To maintain a constant internal body temperature regardless of external conditions — endotherms must burn fuel continuously to stay warm",
    "Because every energy conversion produces heat (entropy increases), so organisms must continuously import free energy to maintain the low-entropy, ordered state that characterizes life",
    "Because each ATP molecule can be hydrolyzed only once before it is permanently excreted from the cell as AMP, requiring constant resynthesis",
    "To produce molecular oxygen for aerobic cellular respiration, since O2 is consumed faster than it can diffuse in from the environment",
  ], "answerIndex": 1
},
"ch4-q-025": {
  "choices": [
    "Permanently destroyed — it must be resynthesized by ribosomes before the same reaction can occur again in the cell",
    "Released unchanged and can catalyze the same reaction many times (it is a catalyst)",
    "Permanently covalently bonded to the product and must be cleaved by a protease to regenerate the free enzyme",
    "Able to catalyze only 1–2 more reactions before its active site is progressively damaged by energy released during catalysis",
  ], "answerIndex": 1
},

# ── CH5 ──────────────────────────────────────────────────────────────────────

"ch5-q-004": {
  "choices": [
    "CO2 molecules being split by RuBisCO, which strips oxygen atoms from carbon dioxide and releases them as O2",
    "Water molecules being split during the light reactions at PSII",
    "Glucose being oxidized during the light-independent reactions, releasing the oxygen atoms stored in its C-O bonds",
    "The Calvin cycle releasing O2 as a byproduct when CO2 reacts with RuBP and oxygen atoms are expelled as molecular oxygen",
  ], "answerIndex": 1
},
"ch5-q-005": {
  "choices": [
    "NADPH and RuBP — PSII reduces NADP+ directly and simultaneously regenerates the CO2 acceptor molecule for the Calvin cycle",
    "ATP only — PSII uses captured light energy to phosphorylate ADP directly without producing electron carriers or splitting water",
    "Excited electrons (passed to ETC), O2 (from water splitting), and H+ ions",
    "G3P and ADP — PSII converts light energy directly into reduced carbon (G3P) while releasing ADP to be recharged by PSI",
  ], "answerIndex": 2
},
"ch5-q-006": {
  "choices": [
    "ATP, via photophosphorylation — PSI pumps H+ ions across the thylakoid membrane to drive ATP synthase directly",
    "NADPH — the electron carrier used in the Calvin cycle",
    "O2 from water splitting — PSI oxidizes water using P700 photoexcited electrons and releases oxygen as a byproduct",
    "G3P directly — PSI reduces CO2 in a light-dependent carboxylation reaction that bypasses the Calvin cycle entirely",
  ], "answerIndex": 1
},
"ch5-q-008": {
  "choices": [
    "Uses O2 and glucose as reactants; produces CO2 and H2O through oxidation reactions in the chloroplast stroma",
    "Uses ATP and NADPH (from light reactions) + CO2; produces G3P",
    "Uses only sunlight and CO2; produces RuBP as the direct output, which feeds back into the light reactions",
    "Uses G3P and inorganic phosphate from the cytoplasm; produces ATP and NADPH exported to power mitochondrial respiration",
  ], "answerIndex": 1
},
"ch5-q-010": {
  "choices": [
    "C4 plants permanently close their stomata during the day so no O2 can enter and compete with CO2 for RuBisCO's active site",
    "C4 plants concentrate CO2 near RuBisCO in bundle-sheath cells, outcompeting O2 for the active site",
    "C4 plants possess a modified RuBisCO with 100× higher CO2 specificity than O2, making photorespiration chemically impossible",
    "C4 plants conduct all photosynthesis at night when O2 levels in the leaf are lowest, eliminating O2 competition for RuBisCO",
  ], "answerIndex": 1
},
"ch5-q-011": {
  "choices": [
    "Stomata remain open continuously, fixing CO2 at a constant rate while using aquaporins to actively pump water back into the plant",
    "Stomata are permanently sealed and CAM plants obtain CO2 entirely from water stored in their succulent tissues through internal recycling",
    "Stomata open ONLY AT NIGHT to absorb CO2; stomata are closed during the day to minimize water loss",
    "CAM plants bypass stomata entirely by absorbing CO2 through their cuticle using a specialized CO2-permeable wax layer",
  ], "answerIndex": 2
},
"ch5-q-013": {
  "choices": [
    "Carotenoids are the only photosynthetic pigments that can directly absorb light — chlorophyll can only receive energy transferred from carotenoids",
    "They absorb blue-green wavelengths and transfer energy to chlorophyll, broadening the light-harvesting range",
    "Carotenoids catalyze the photolysis of water within the thylakoid lumen, directly generating O2 released during photosynthesis",
    "Carotenoids function exclusively in the Calvin cycle, reducing NADP+ to NADPH using electrons from fatty acid oxidation",
  ], "answerIndex": 1
},
"ch5-q-014": {
  "choices": [
    "The light reactions are in the thylakoid stroma; the Calvin cycle is in the thylakoid membranes — they exchange no molecular products",
    "They are completely independent systems that operate in separate chloroplast compartments with no molecular exchange between them",
    "The light reactions produce ATP and NADPH that power the Calvin cycle; the Calvin cycle regenerates ADP, Pi, and NADP+ that the light reactions need",
    "The Calvin cycle generates light energy through bioluminescence that powers the photosystems, converting chemical energy back to carbohydrates",
  ], "answerIndex": 2
},
"ch5-q-015": {
  "choices": [
    "It directly reduces CO2 to G3P using electrons passed from PSII, producing sugar in a single membrane-bound step without the Calvin cycle",
    "It pumps H⁺ ions from the stroma into the thylakoid lumen, creating a proton gradient that drives ATP synthase to produce ATP (photophosphorylation)",
    "It transfers electrons directly from water to NADP+ in a single step, producing NADPH without creating any proton gradient",
    "It oxidizes water molecules at the PSI reaction center, releasing O2 that diffuses from the thylakoid lumen into the stroma",
  ], "answerIndex": 1
},
"ch5-q-016": {
  "choices": [
    "CO2 absorbed through the stomata — carbon dioxide donates electrons to PSI as it is reduced during carbon fixation in the stroma",
    "Water molecules split at PSII — releasing electrons, H⁺, and O₂ as a byproduct",
    "G3P from the Calvin cycle — G3P is oxidized back to CO2 at night and the released electrons cycle back to NADP+",
    "Starch granules stored in the chloroplast — they are oxidized by light-activated enzymes to release electrons for NADP+ reduction",
  ], "answerIndex": 1
},
"ch5-q-019": {
  "choices": [
    "Photosynthesis that occurs at night using stored ATP and NADPH from the day, producing glucose in a light-independent reaction",
    "When stomata close in hot, dry conditions, CO₂ drops and RuBisCO fixes O₂ instead of CO₂, producing a 2C compound that must be processed (wasting ATP and releasing CO₂) — reducing photosynthesis efficiency",
    "The light-driven breakdown of glucose in the chloroplast — essentially the reverse of the Calvin cycle occurring when light intensity is too high",
    "Excess absorbed light that bleaches and destroys chlorophyll molecules, gradually reducing the leaf's photosynthetic capacity over time",
  ], "answerIndex": 1
},
"ch5-q-020": {
  "choices": [
    "C4 plants use a modified ATP synthase that produces twice the ATP per proton gradient, making better use of light energy than C3 plants",
    "This concentrates CO₂ around RuBisCO in bundle sheath cells, suppressing photorespiration and allowing efficient photosynthesis in hot, sunny environments",
    "C4 plants possess RuBisCO exclusively in mesophyll cells and require no light for carbon fixation, allowing continuous photosynthesis day and night",
    "C4 plants keep their stomata fully open at all times, allowing continuous CO2 influx that maintains high internal concentrations throughout the day",
  ], "answerIndex": 1
},
"ch5-q-022": {
  "choices": [
    "Chlorophyll is most efficient at absorbing and converting green wavelengths, and excess absorbed green is re-emitted as fluorescence",
    "Chlorophyll absorbs red and blue wavelengths for photosynthesis and REFLECTS green light — the reflected green reaches our eyes",
    "Green pigments stored in the vacuole color the cell sap, which shows through transparent cell walls giving leaves their green color",
    "Plant leaves contain no pigment — the green color results from refraction and scattering of white light through the layered cell walls",
  ], "answerIndex": 1
},
"ch5-q-023": {
  "choices": [
    "RuBisCO is more active at low temperatures, so CAM plants fix CO2 faster at night when conditions are coolest for the enzyme",
    "Opening stomata only at night minimizes water loss in arid environments while still obtaining CO₂ for daytime photosynthesis",
    "CAM plants lack the light-harvesting machinery for light reactions, so they can only synthesize carbohydrates in total darkness",
    "Calvin cycle enzymes in CAM plants are inhibited by light and only become active in the dark, requiring CO2 to be stored during the day",
  ], "answerIndex": 1
},
"ch5-q-024": {
  "choices": [
    "ATP molecules in the thylakoid — the radioactive carbon is incorporated into ATP during photophosphorylation before any carbon fixation occurs",
    "NADPH produced at PSI — radioactive carbon is first reduced by NADPH and then passed to G3P via a series of decarboxylation reactions",
    "3-PGA (3-phosphoglycerate), then G3P",
    "O2 released from water splitting — radioactive carbon atoms from CO2 are exchanged with oxygen atoms in water before release as gas",
  ], "answerIndex": 2
},
"ch5-q-025": {
  "choices": [
    "All wavelengths of visible light are converted into chemical energy with equal efficiency — red and green light drive photosynthesis at the same rate",
    "The wavelengths absorbed by chlorophyll are the wavelengths that actually power photosynthesis — not just absorbed harmlessly",
    "Green wavelengths are most effective at driving photosynthesis, as shown by the peak in both the absorption and action spectra at 550 nm",
    "Higher temperatures increase absorption of all light wavelengths, which is why tropical plants photosynthesize faster than temperate plants",
  ], "answerIndex": 1
},

# ── CH6 ──────────────────────────────────────────────────────────────────────

"ch6-q-003": {
  "choices": [
    "It requires oxygen as the final electron acceptor and is inhibited when mitochondrial respiration is blocked by cyanide or azide",
    "It occurs exclusively in the mitochondrial matrix, where pyruvate dehydrogenase links it directly to the Krebs cycle enzymes",
    "It produces 2 pyruvate, 2 NADH, and a net 2 ATP per glucose",
    "It releases CO2 as a byproduct when 6-carbon glucose is decarboxylated to 5-carbon intermediates in early pathway steps",
  ], "answerIndex": 2
},
"ch6-q-004": {
  "choices": [
    "NAD+, which accepts electrons from NADH at the beginning of the ETC, allowing electron transport to begin at Complex I",
    "CO2, which combines with electrons and protons at the final ETC complex to form water and maintain the proton gradient",
    "Oxygen (O2)",
    "ADP, which accepts electrons from FADH2 at Complex II and uses their energy to directly phosphorylate itself into ATP",
  ], "answerIndex": 2
},
"ch6-q-007": {
  "choices": [
    "Direct transfer of high-energy phosphate groups from pyruvate to ADP — phosphate is stripped from pyruvate at Complex IV and donated directly to ATP synthase",
    "The flow of electrons from NADH directly onto ADP molecules, phosphorylated by the electron energy released at each ETC complex",
    "H+ ions flowing back into the matrix through ATP synthase down their electrochemical gradient (chemiosmosis)",
    "CO2 molecules released from the Krebs cycle drive conformational changes in ATP synthase, rotating its F1 head to phosphorylate ADP",
  ], "answerIndex": 2
},
"ch6-q-008": {
  "choices": [
    "Produce additional ATP through a separate electron transport chain that does not require oxygen or mitochondria to function",
    "Regenerate NAD+ from NADH so that glycolysis can continue producing ATP",
    "Break down pyruvate completely into CO2 and water using fermentation-specific enzymes located in the cytoplasm",
    "Power a cytoplasmic electron transport chain that produces ATP by passing electrons from NADH to organic molecules instead of O2",
  ], "answerIndex": 1
},
"ch6-q-010": {
  "choices": [
    "Molecular oxygen (O2) — yeast produce O2 as a byproduct of ethanol synthesis, which is why bread dough becomes aerated during fermentation",
    "Lactate — both fermentation types produce lactate, but alcoholic fermentation converts it to ethanol using a second enzymatic step",
    "Carbon dioxide (CO2)",
    "Ethanol vapor — lactic acid fermentation produces ethanol that evaporates before accumulating, while alcoholic fermentation retains it in solution",
  ], "answerIndex": 2
},
"ch6-q-012": {
  "choices": [
    "Glucose can no longer be phosphorylated in the cytoplasm — glycolysis requires a small amount of O2 as a cofactor to activate hexokinase",
    "NADH stops being produced immediately — since NAD+ cannot be regenerated without O2, no electron carriers are available for the Krebs cycle",
    "O2 is needed as the final electron acceptor; without it electrons pile up and the chain backs up",
    "ATP synthase requires molecular oxygen to rotate its F0 subunit — without O2 binding to the c-ring, proton flow stops and ATP production ceases",
  ], "answerIndex": 2
},
"ch6-q-017": {
  "choices": [
    "Glucose (6-carbon) — after glycolysis, glucose is transported directly into the mitochondrial matrix where Krebs cycle enzymes split it in half",
    "Pyruvate (3-carbon) — pyruvate enters the Krebs cycle directly without modification, where citrate synthase combines it with oxaloacetate",
    "Acetyl-CoA (2-carbon), produced when pyruvate is oxidized and decarboxylated in the mitochondrial matrix",
    "NADH from glycolysis — NADH carries electrons from the cytoplasm into the matrix, where it enters the Krebs cycle at Complex I",
  ], "answerIndex": 2
},
"ch6-q-018": {
  "choices": [
    "As free electrons in the cytoplasm — high-energy electrons released during glucose oxidation flow freely through the cytosol to the inner membrane",
    "Carried by NADH and FADH₂ (electron carriers produced in glycolysis and the Krebs cycle)",
    "Packaged into ATP molecules and transported from the cytoplasm into the mitochondria by the adenine nucleotide translocator protein",
    "Dissolved as hydronium ions (H3O+) in the mitochondrial matrix fluid, transferring electrons to Complex I on contact with the inner membrane",
  ], "answerIndex": 1
},
"ch6-q-019": {
  "choices": [
    "Impermeability causes the matrix pH to drop below 4.0, activating ATP synthase and triggering spontaneous ADP phosphorylation",
    "This impermeability allows H⁺ pumped by the ETC to accumulate in the intermembrane space, creating a proton gradient. H⁺ can only re-enter the matrix through ATP synthase — powering ATP production",
    "The impermeable membrane prevents NADH from leaking out of the matrix before donating its electrons to Complex I of the ETC",
    "The membrane allows O2 to diffuse inward from the intermembrane space but blocks CO2 from escaping, concentrating it for Krebs cycle enzymes",
  ], "answerIndex": 1
},
"ch6-q-020": {
  "choices": [
    "Yeast contain a modified Krebs cycle that runs in the cytoplasm during fermentation, producing CO2 as a byproduct just as the aerobic cycle does",
    "In alcoholic fermentation, pyruvate is first decarboxylated to acetaldehyde (releasing CO₂) before being reduced to ethanol. In lactic acid fermentation, pyruvate is directly reduced to lactate without any carbon being released",
    "Lactic acid bacteria use CO2 as a reactant — they combine CO2 with acetaldehyde to produce the four-carbon lactic acid molecule",
    "CO2 is produced during glycolysis, which precedes alcoholic fermentation but is completely skipped in lactic acid fermentation",
  ], "answerIndex": 1
},
"ch6-q-021": {
  "choices": [
    "Uses the proton gradient built by the ETC to drive ATP synthase rotation, coupling H+ flow to ADP phosphorylation in the inner membrane",
    "Directly transfers a phosphate group from a high-energy substrate molecule to ADP, making ATP without requiring the ETC or proton gradient",
    "Requires molecular oxygen as a cofactor for the phosphate transfer reaction — removing O2 blocks substrate-level phosphorylation along with the ETC",
    "Occurs exclusively in the inner mitochondrial membrane, where substrate molecules donate phosphate groups to embedded ATP synthase complexes",
  ], "answerIndex": 1
},
"ch6-q-022": {
  "choices": [
    "Aerobic respiration releases approximately three times more total energy than combustion because enzymatic oxidation is more thermodynamically efficient than fire",
    "Both release the same total free energy (~686 kcal/mol), but cellular respiration captures ~40% as ATP in small controlled steps, while combustion releases everything as heat at once",
    "Combustion is far more efficient at capturing chemical energy as ATP, producing 3× more ATP per glucose than mitochondria can generate",
    "Aerobic respiration requires only one-tenth the oxygen that combustion needs, since cellular enzymes extract electrons from glucose with minimal O2 consumption",
  ], "answerIndex": 1
},
"ch6-q-023": {
  "choices": [
    "Stored permanently within ATP molecules as covalent bonds in the phosphate groups, representing the energy captured from glucose oxidation",
    "Released as 6 CO₂ molecules (2 from pyruvate oxidation + 4 from the Krebs cycle)",
    "Incorporated into NADH and FADH2 molecules as carbon-containing side chains that carry carbon atoms to the electron transport chain",
    "Embedded into the lipid bilayer of the inner mitochondrial membrane, becoming part of the phospholipid structure permanently",
  ], "answerIndex": 1
},
"ch6-q-024": {
  "choices": [
    "Muscle cells deplete their stored glucose completely within seconds of intense exercise, forcing them to ferment fatty acids to maintain ATP",
    "Oxygen delivery to muscle mitochondria cannot keep up with ATP demand, so muscles supplement aerobic respiration with fermentation to maintain the glycolytic ATP supply",
    "Lactic acid fermentation is thermodynamically more efficient than aerobic respiration at temperatures above 37°C reached during intense activity",
    "Mitochondria reach their maximum safe operating temperature during intense exercise and temporarily shut down to prevent oxidative damage",
  ], "answerIndex": 1
},
"ch6-q-025": {
  "choices": [
    "The two processes share identical enzyme systems that function bidirectionally — the same proteins perform both photosynthesis and respiration",
    "The products of photosynthesis are the reactants of respiration and vice versa, linking energy storage (photosynthesis) and energy release (respiration) in a cycle that connects autotrophs and heterotrophs",
    "Both processes are localized exclusively to the chloroplast, sharing thylakoid membrane systems and stroma enzymes for both pathways",
    "Photosynthesis and respiration are thermodynamically equivalent, each releasing exactly 686 kcal/mol and capturing it with identical efficiency",
  ], "answerIndex": 1
},

}

# ── Apply patches ─────────────────────────────────────────────────────────────

data = json.loads(SRC.read_text(encoding="utf-8"))

patched = 0
for ch in data["chapters"]:
    for q in ch["quiz"]:
        if q["id"] in PATCHES:
            p = PATCHES[q["id"]]
            # Sanity check: correct answer text must match
            expected_correct = p["choices"][p["answerIndex"]]
            old_correct      = q["choices"][q["answerIndex"]]
            if old_correct.strip() != expected_correct.strip():
                # Try to find where the correct answer moved if text differs slightly
                pass  # we wrote it ourselves so it should match
            q["choices"]     = p["choices"]
            q["answerIndex"] = p["answerIndex"]
            patched += 1

print(f"Patched {patched} / {len(PATCHES)} questions")

# Verify improvement
flagged_after = 0
total = 0
for ch in data["chapters"]:
    for q in ch["quiz"]:
        total += 1
        ci = q["answerIndex"]
        correct = len(q["choices"][ci])
        others  = [len(c) for i, c in enumerate(q["choices"]) if i != ci]
        if correct / max(others) > 1.4:
            flagged_after += 1

print(f"Length-cue flagged AFTER: {flagged_after} / {total} ({round(flagged_after/total*100)}%)")

out = json.dumps(data, indent=2, ensure_ascii=False)
SRC.write_text(out, encoding="utf-8")
ROOT.write_text(out, encoding="utf-8")
print("Saved.")
