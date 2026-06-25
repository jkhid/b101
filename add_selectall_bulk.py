"""Add 7 selectAll questions per chapter (Ch 1-3)."""

import json, pathlib

SRC  = pathlib.Path("src/data/content.json")
ROOT = pathlib.Path("content.json")

data = json.loads(SRC.read_text(encoding="utf-8"))

def ch(cid):
    return next(c for c in data["chapters"] if c["id"] == cid)

def add(cid, questions):
    ids = {q["id"] for q in ch(cid)["quiz"]}
    added = 0
    for q in questions:
        if q["id"] not in ids:
            ch(cid)["quiz"].append(q)
            added += 1
    return added

# ══════════════════════════════════════════════════════════════════════════════
# CH 1  — ch1-q-044 through ch1-q-050
# ══════════════════════════════════════════════════════════════════════════════

ch1_new = [
  {
    "id": "ch1-q-044", "type": "selectAll",
    "section": "1.1", "difficulty": "medium",
    "question": "Which are characteristics shared by ALL living things? (Select all that apply.)",
    "choices": [
      "Use energy through metabolism",
      "Respond to stimuli in their environment",
      "Are composed of one or more cells",
      "Reproduce and pass hereditary information to offspring",
      "Maintain homeostasis",
      "Perform photosynthesis to produce their own food",
    ],
    "answerIndices": [0, 1, 2, 3, 4],
    "explanation": (
      "All five life characteristics apply to every living thing. "
      "Photosynthesis is performed only by autotrophs (plants, algae, some bacteria) — "
      "the majority of organisms are heterotrophs that cannot photosynthesize."
    ),
  },
  {
    "id": "ch1-q-045", "type": "selectAll",
    "section": "1.2", "difficulty": "medium",
    "question": "Which kingdoms belong to domain Eukarya? (Select all that apply.)",
    "choices": [
      "Plantae",
      "Animalia",
      "Fungi",
      "Protista",
      "Bacteria",
      "Archaea",
    ],
    "answerIndices": [0, 1, 2, 3],
    "explanation": (
      "Domain Eukarya contains four kingdoms: Plantae, Animalia, Fungi, and Protista — "
      "all have membrane-bound nuclei and other eukaryotic organelles. "
      "Bacteria and Archaea are each their own domain of prokaryotes."
    ),
  },
  {
    "id": "ch1-q-046", "type": "selectAll",
    "section": "1.3", "difficulty": "medium",
    "question": "Which statements about the scientific method are correct? (Select all that apply.)",
    "choices": [
      "Observations and questions lead to testable hypotheses",
      "Hypotheses must be falsifiable — there must be a possible result that could disprove them",
      "A single experiment with a positive result proves a hypothesis true",
      "Control groups provide a baseline by receiving no treatment",
      "Peer review helps identify errors and bias before publication",
    ],
    "answerIndices": [0, 1, 3, 4],
    "explanation": (
      "The scientific method uses testable, falsifiable hypotheses, control groups, and peer review. "
      "A single positive result does NOT prove a hypothesis — it only provides support; "
      "hypotheses can only be supported or rejected, never proven absolutely true."
    ),
  },
  {
    "id": "ch1-q-047", "type": "selectAll",
    "section": "1.1", "difficulty": "hard",
    "question": "Which are examples of emergent properties? (Select all that apply.)",
    "choices": [
      "The ability of a single enzyme molecule to lower activation energy",
      "Consciousness arising from billions of interacting neurons",
      "A bee colony regulating hive temperature through coordinated fanning behavior",
      "The mass of a cell equaling the sum of its individual molecules",
      "Life arising from the organized interaction of nonliving chemical components",
    ],
    "answerIndices": [1, 2, 4],
    "explanation": (
      "Emergent properties arise from the interactions of components and cannot be predicted "
      "from any single component alone. Consciousness, colony thermoregulation, and life itself are emergent. "
      "An enzyme's catalytic ability is a property of that single molecule (not emergent), "
      "and mass is simply additive — it is not an emergent property."
    ),
  },
  {
    "id": "ch1-q-048", "type": "selectAll",
    "section": "1.1", "difficulty": "medium",
    "question": "Which organisms are correctly classified as autotrophs (producers)? (Select all that apply.)",
    "choices": [
      "A maple tree that builds sugars using sunlight and CO2",
      "A mushroom that absorbs nutrients from decaying wood",
      "A photosynthetic cyanobacterium living in a freshwater pond",
      "A deep-sea bacterium that uses hydrogen sulfide as an energy source (chemosynthesis)",
      "A deer that grazes on grass",
    ],
    "answerIndices": [0, 2, 3],
    "explanation": (
      "Autotrophs make their own food from inorganic sources — either via photosynthesis "
      "(maple tree, cyanobacterium) or chemosynthesis (deep-sea bacteria). "
      "Mushrooms are heterotrophic decomposers; deer are heterotrophic consumers — "
      "both must consume organic matter made by others."
    ),
  },
  {
    "id": "ch1-q-049", "type": "selectAll",
    "section": "1.1", "difficulty": "medium",
    "question": "Which levels of biological organization are ABOVE the organism level? (Select all that apply.)",
    "choices": [
      "Population",
      "Community",
      "Organ system",
      "Ecosystem",
      "Biosphere",
      "Tissue",
    ],
    "answerIndices": [0, 1, 3, 4],
    "explanation": (
      "Above the organism: population (same species, same area) → community (all species in an area) "
      "→ ecosystem (community + physical environment) → biosphere (all life on Earth). "
      "Organ system and tissue are levels WITHIN the organism, below the organism level."
    ),
  },
  {
    "id": "ch1-q-050", "type": "selectAll",
    "section": "1.3", "difficulty": "hard",
    "question": "A researcher tests whether caffeine affects heart rate in mice. Which are standardized (controlled) variables that should be kept constant across all groups? (Select all that apply.)",
    "choices": [
      "The age and genetic strain of mice in each group",
      "The dose of caffeine given to the experimental group",
      "The room temperature and lighting conditions during testing",
      "The method used to measure heart rate",
      "The number of mice in each group",
    ],
    "answerIndices": [0, 2, 3, 4],
    "explanation": (
      "Standardized variables are everything kept the same so that the caffeine dose is the "
      "only difference between groups. The caffeine dose is the independent variable "
      "(deliberately changed by the researcher), not something to standardize."
    ),
  },
]

# ══════════════════════════════════════════════════════════════════════════════
# CH 2  — ch2-q-059 through ch2-q-065
# ══════════════════════════════════════════════════════════════════════════════

ch2_new = [
  {
    "id": "ch2-q-059", "type": "selectAll",
    "section": "2.3", "difficulty": "medium",
    "question": "Which properties of water are directly caused by hydrogen bonding between water molecules? (Select all that apply.)",
    "choices": [
      "High specific heat capacity (resists temperature change)",
      "Cohesion and surface tension",
      "Ice being less dense than liquid water (ice floats)",
      "The ability to dissolve nonpolar oils and fats",
      "The ability to dissolve ionic compounds like table salt",
    ],
    "answerIndices": [0, 1, 2, 4],
    "explanation": (
      "Hydrogen bonding explains water's high specific heat (breaking H-bonds absorbs energy), "
      "cohesion/surface tension (H-bonds pull surface molecules inward), "
      "ice's low density (H-bonds form an open lattice in ice), "
      "and dissolving ions (partial charges on water attract ions). "
      "Water CANNOT dissolve nonpolar oils — oils lack charges, so water excludes them."
    ),
  },
  {
    "id": "ch2-q-060", "type": "selectAll",
    "section": "2.5", "difficulty": "medium",
    "question": "Which are functions of proteins in living organisms? (Select all that apply.)",
    "choices": [
      "Catalyzing chemical reactions (enzymes)",
      "Structural support (keratin in hair/nails, collagen in connective tissue)",
      "Long-term energy storage in adipose tissue",
      "Transporting oxygen through the blood (hemoglobin)",
      "Immune defense (antibodies)",
      "Cell signaling and communication (hormones like insulin)",
    ],
    "answerIndices": [0, 1, 3, 4, 5],
    "explanation": (
      "Proteins serve as enzymes, structural materials, transporters, antibodies, and signaling molecules. "
      "Long-term energy storage is primarily a function of LIPIDS (triglycerides in fat tissue), not proteins."
    ),
  },
  {
    "id": "ch2-q-061", "type": "selectAll",
    "section": "2.5", "difficulty": "medium",
    "question": "Which are polysaccharides (polymers built from many monosaccharide units)? (Select all that apply.)",
    "choices": [
      "Starch (energy storage in plant cells)",
      "Glycogen (energy storage in animal liver and muscle)",
      "Glucose (a six-carbon ring sugar)",
      "Cellulose (structural component of plant cell walls)",
      "Chitin (structural polymer in fungal walls and insect exoskeletons)",
      "Sucrose (table sugar)",
    ],
    "answerIndices": [0, 1, 3, 4],
    "explanation": (
      "Starch, glycogen, cellulose, and chitin are polysaccharides — long chains of monosaccharides. "
      "Glucose is a monosaccharide (single sugar unit). "
      "Sucrose is a disaccharide (glucose + fructose, joined by one glycosidic bond), not a polymer."
    ),
  },
  {
    "id": "ch2-q-062", "type": "selectAll",
    "section": "2.5", "difficulty": "medium",
    "question": "Which correctly describe how DNA and RNA differ? (Select all that apply.)",
    "choices": [
      "DNA contains deoxyribose sugar; RNA contains ribose sugar",
      "DNA uses thymine (T); RNA uses uracil (U) in its place",
      "DNA is typically double-stranded; RNA is typically single-stranded",
      "DNA is found ONLY in the nucleus; RNA is found ONLY in the cytoplasm",
      "DNA stores genetic information long-term; RNA helps express that information",
    ],
    "answerIndices": [0, 1, 2, 4],
    "explanation": (
      "DNA uses deoxyribose/thymine/double strands for long-term storage; "
      "RNA uses ribose/uracil/single strands to carry and express genetic information. "
      "DNA is NOT exclusively nuclear — mitochondria and chloroplasts also contain their own DNA. "
      "RNA is also found in the nucleus (e.g., pre-mRNA is processed there before export)."
    ),
  },
  {
    "id": "ch2-q-063", "type": "selectAll",
    "section": "2.5", "difficulty": "medium",
    "question": "Which statements about enzyme function are correct? (Select all that apply.)",
    "choices": [
      "Enzymes lower the activation energy of a reaction",
      "Enzymes are consumed and permanently destroyed during the reactions they catalyze",
      "Enzymes can be denatured (inactivated) by extreme heat or extreme pH",
      "An enzyme's active site is complementary in shape to its specific substrate",
      "A single enzyme molecule can catalyze the same reaction many times",
    ],
    "answerIndices": [0, 2, 3, 4],
    "explanation": (
      "Enzymes lower activation energy, are destroyed by denaturation (extreme heat/pH), "
      "have complementary active sites, and are reused many times. "
      "Enzymes are NOT consumed — they emerge unchanged after each reaction, "
      "making them true catalysts."
    ),
  },
  {
    "id": "ch2-q-064", "type": "selectAll",
    "section": "2.5", "difficulty": "easy",
    "question": "Which are types of lipids found in living organisms? (Select all that apply.)",
    "choices": [
      "Triglycerides (fats and oils used for long-term energy storage)",
      "Phospholipids (the main structural component of cell membranes)",
      "Steroids (including cholesterol, estrogen, and testosterone)",
      "Waxes (waterproofing in plant cuticles and animal coatings)",
      "Glycogen (a branched polymer used for short-term energy storage)",
    ],
    "answerIndices": [0, 1, 2, 3],
    "explanation": (
      "The four main types of lipids are triglycerides, phospholipids, steroids, and waxes — "
      "all are hydrophobic or amphipathic molecules that are insoluble in water. "
      "Glycogen is a polysaccharide carbohydrate, not a lipid."
    ),
  },
  {
    "id": "ch2-q-065", "type": "selectAll",
    "section": "2.5", "difficulty": "hard",
    "question": "Which correctly describe the four levels of protein structure? (Select all that apply.)",
    "choices": [
      "Primary structure is the amino acid sequence, held together by covalent peptide bonds",
      "Secondary structure includes alpha helices and beta sheets, stabilized by hydrogen bonds between backbone atoms",
      "Tertiary structure is the overall 3D shape, resulting from interactions among R groups (side chains)",
      "Quaternary structure refers to a protein made of a single polypeptide chain",
      "Denaturation disrupts secondary, tertiary, and quaternary structure while leaving the primary sequence intact",
    ],
    "answerIndices": [0, 1, 2, 4],
    "explanation": (
      "Primary = amino acid sequence (peptide bonds); secondary = local folding (backbone H-bonds, alpha helices/beta sheets); "
      "tertiary = overall 3D shape from R-group interactions (hydrophobic, ionic, H-bonds, disulfide bridges); "
      "denaturation unfolds 2°/3°/4° but not 1°. "
      "Quaternary structure requires TWO OR MORE polypeptide subunits — "
      "a single polypeptide has no quaternary structure."
    ),
  },
]

# ══════════════════════════════════════════════════════════════════════════════
# CH 3  — ch3-q-062 through ch3-q-068
# ══════════════════════════════════════════════════════════════════════════════

ch3_new = [
  {
    "id": "ch3-q-062", "type": "selectAll",
    "section": "3.5", "difficulty": "medium",
    "question": "Which are functions of the cytoskeleton? (Select all that apply.)",
    "choices": [
      "Maintaining cell shape and providing mechanical support",
      "Separating chromosomes during cell division (mitotic spindle)",
      "Generating ATP for all forms of cellular movement",
      "Serving as tracks for motor proteins transporting organelles and vesicles",
      "Forming cilia and flagella for cell and fluid movement",
      "Synthesizing phospholipids for membrane assembly",
    ],
    "answerIndices": [0, 1, 3, 4],
    "explanation": (
      "The cytoskeleton (microtubules, microfilaments, intermediate filaments) maintains shape, "
      "forms the mitotic spindle, provides motor protein tracks (kinesin/dynein), and builds cilia/flagella. "
      "ATP is generated by mitochondria (not the cytoskeleton itself), "
      "and phospholipid synthesis occurs in the smooth ER."
    ),
  },
  {
    "id": "ch3-q-063", "type": "selectAll",
    "section": "3.6", "difficulty": "medium",
    "question": "Which are types of cell junctions found in ANIMAL cells? (Select all that apply.)",
    "choices": [
      "Tight junctions (seal adjacent cells, blocking paracellular flow)",
      "Gap junctions (channels for direct cytoplasmic communication between cells)",
      "Anchoring junctions / desmosomes (mechanical links between neighboring cells)",
      "Plasmodesmata (cytoplasmic channels through plant cell walls)",
      "Middle lamella (pectin layer cementing adjacent plant cell walls)",
    ],
    "answerIndices": [0, 1, 2],
    "explanation": (
      "Animal cells form three types of junctions: tight junctions (seal, e.g., blood-brain barrier), "
      "gap junctions (communication channels, e.g., heart muscle coordination), "
      "and anchoring junctions/desmosomes (mechanical attachment). "
      "Plasmodesmata and the middle lamella are plant-specific structures."
    ),
  },
  {
    "id": "ch3-q-064", "type": "selectAll",
    "section": "3.3", "difficulty": "medium",
    "question": "Which correctly describe the plasma membrane? (Select all that apply.)",
    "choices": [
      "It is composed of a phospholipid bilayer with embedded and peripheral proteins",
      "It is selectively permeable — nonpolar molecules cross freely, but polar and charged molecules need help",
      "Cholesterol in animal membranes stabilizes fluidity at varying temperatures",
      "It is a rigid, fixed structure that does not change shape or composition over time",
      "Membrane proteins can serve as transporters, enzymes, receptors, adhesion molecules, and recognition markers",
    ],
    "answerIndices": [0, 1, 2, 4],
    "explanation": (
      "The plasma membrane is a fluid mosaic of phospholipids and proteins that is selectively permeable. "
      "Cholesterol buffers fluidity (prevents excessive rigidity in cold, excessive fluidity in heat). "
      "Membrane proteins perform all five major functions. "
      "The membrane is NOT rigid — it is fluid and constantly remodeled (endocytosis, exocytosis, lateral diffusion)."
    ),
  },
  {
    "id": "ch3-q-065", "type": "selectAll",
    "section": "3.4", "difficulty": "medium",
    "question": "Which of the following are membrane-bound organelles? (Select all that apply.)",
    "choices": [
      "Mitochondrion",
      "Ribosome",
      "Nucleus",
      "Lysosome",
      "Chloroplast",
      "Nucleolus",
    ],
    "answerIndices": [0, 2, 3, 4],
    "explanation": (
      "Mitochondria (double membrane), nucleus (double membrane nuclear envelope), "
      "lysosomes (single membrane), and chloroplasts (double membrane) are all membrane-bound. "
      "Ribosomes are large RNA-protein complexes with NO surrounding membrane. "
      "The nucleolus is a region within the nucleus for rRNA synthesis — it has no membrane of its own."
    ),
  },
  {
    "id": "ch3-q-066", "type": "selectAll",
    "section": "3.3", "difficulty": "medium",
    "question": "Which processes move substances INTO the cell? (Select all that apply.)",
    "choices": [
      "Phagocytosis ('cell eating' — membrane engulfs large solid particles)",
      "Pinocytosis ('cell drinking' — membrane folds inward to take up extracellular fluid)",
      "Exocytosis (secretory vesicles fuse with the membrane and release contents outside)",
      "Receptor-mediated endocytosis (specific ligands trigger clathrin-coated pit formation)",
      "Osmosis into the cell when the external solution is hypotonic",
    ],
    "answerIndices": [0, 1, 3, 4],
    "explanation": (
      "Phagocytosis, pinocytosis, receptor-mediated endocytosis, and osmosis (when the cell is in a hypotonic solution) "
      "all bring material into the cell. "
      "Exocytosis is the reverse — it expels contents OUT of the cell by vesicle fusion with the plasma membrane."
    ),
  },
  {
    "id": "ch3-q-067", "type": "selectAll",
    "section": "3.3", "difficulty": "medium",
    "question": "Which are examples of passive transport (no ATP required)? (Select all that apply.)",
    "choices": [
      "Oxygen diffusing down its concentration gradient across the lipid bilayer",
      "Glucose moving into a cell via GLUT carrier proteins (facilitated diffusion)",
      "Water moving through aquaporin channels by osmosis",
      "The Na+/K+ ATPase pump moving Na+ out and K+ in against their gradients",
      "K+ ions moving outward through open potassium channels down their electrochemical gradient",
    ],
    "answerIndices": [0, 1, 2, 4],
    "explanation": (
      "Passive transport moves substances DOWN their concentration or electrochemical gradient without ATP: "
      "simple diffusion (O2), facilitated diffusion (glucose via GLUT), osmosis (water via aquaporins), "
      "and ion channel flow (K+ down gradient). "
      "The Na+/K+ ATPase pump moves ions AGAINST their gradients — that is active transport requiring ATP."
    ),
  },
  {
    "id": "ch3-q-068", "type": "selectAll",
    "section": "3.4", "difficulty": "medium",
    "question": "Which correctly describe mitochondria? (Select all that apply.)",
    "choices": [
      "They have a double membrane; the inner membrane is folded into cristae",
      "They are the primary site of ATP production through aerobic cellular respiration",
      "They contain their own circular DNA and ribosomes, supporting the endosymbiont theory",
      "They produce oxygen as a byproduct of reactions occurring in their matrix",
      "They are found in virtually all eukaryotic cells, including plant and fungal cells",
    ],
    "answerIndices": [0, 1, 2, 4],
    "explanation": (
      "Mitochondria have a cristae-folded inner membrane, produce ATP via aerobic respiration, "
      "carry their own circular DNA (endosymbiont evidence), and are present in nearly all eukaryotes including plants. "
      "Mitochondria do NOT produce oxygen — O2 is released by chloroplasts during the light reactions of photosynthesis."
    ),
  },
]

# ── Apply ──────────────────────────────────────────────────────────────────────

a1 = add("ch1", ch1_new)
a2 = add("ch2", ch2_new)
a3 = add("ch3", ch3_new)

print(f"ch1: +{a1} -> {len(ch('ch1')['quiz'])} questions")
print(f"ch2: +{a2} -> {len(ch('ch2')['quiz'])} questions")
print(f"ch3: +{a3} -> {len(ch('ch3')['quiz'])} questions")

sa_count = lambda cid: sum(1 for q in ch(cid)["quiz"] if q.get("type") == "selectAll")
print(f"\nSelectAll per chapter: ch1={sa_count('ch1')}, ch2={sa_count('ch2')}, ch3={sa_count('ch3')}")

out = json.dumps(data, indent=2, ensure_ascii=False)
SRC.write_text(out, encoding="utf-8")
ROOT.write_text(out, encoding="utf-8")
print("Saved.")
