"""
Fills identified content gaps:
- Ch 2: protein structure levels, steroids, carbohydrate types (fructose/disaccharides/glycogen/chitin)
- Ch 3: centriole, cytoskeleton, plant-vs-animal comparison, Schleiden/Schwann cell theory
- Ch 1: anabolism/catabolism dedicated flashcard
Skips any ID already present (safe to re-run).
"""

import json, pathlib

SRC  = pathlib.Path("src/data/content.json")
ROOT = pathlib.Path("content.json")

data = json.loads(SRC.read_text(encoding="utf-8"))

def add(chapter_id, flashcards=(), quiz=()):
    ch = next(c for c in data["chapters"] if c["id"] == chapter_id)
    existing_fc = {f["id"] for f in ch["flashcards"]}
    existing_q  = {q["id"] for q in ch["quiz"]}
    added_fc = added_q = 0
    for f in flashcards:
        if f["id"] not in existing_fc:
            ch["flashcards"].append(f); added_fc += 1
    for q in quiz:
        if q["id"] not in existing_q:
            ch["quiz"].append(q); added_q += 1
    print(f"  {chapter_id}: +{added_fc} fc, +{added_q} q  -> {len(ch['flashcards'])} fc / {len(ch['quiz'])} q total")

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — anabolism / catabolism dedicated card
# ══════════════════════════════════════════════════════════════════════════════

ch1_fc = [
  {
    "id": "ch1-fc-016", "section": "1.1", "difficulty": "easy",
    "front": "Anabolism vs. catabolism",
    "back": "Anabolism: building larger molecules from smaller ones (requires energy — endergonic). "
            "Catabolism: breaking down larger molecules into smaller ones (releases energy — exergonic). "
            "Together they make up metabolism."
  },
]

ch1_q = [
  {
    "id": "ch1-q-026", "section": "1.1", "difficulty": "easy",
    "question": "Which of the following is an example of an ANABOLIC process?",
    "choices": [
      "Breaking down glucose during cellular respiration",
      "Hydrolysis of a protein into amino acids",
      "Assembling amino acids into a protein (translation)",
      "Digesting fat in the small intestine"
    ],
    "answerIndex": 2,
    "explanation": "Anabolism builds complex molecules from simpler ones, requiring energy input. Synthesizing a protein from amino acids is anabolic. The others are catabolic (breaking down) processes."
  },
  {
    "id": "ch1-q-027", "section": "1.1", "difficulty": "easy",
    "question": "Metabolism is best defined as:",
    "choices": [
      "Only the energy-releasing reactions in a cell",
      "Only the energy-requiring reactions in a cell",
      "The sum of ALL chemical reactions in an organism, including both anabolic and catabolic pathways",
      "The rate at which an organism consumes oxygen"
    ],
    "answerIndex": 2,
    "explanation": "Metabolism encompasses every chemical reaction in an organism — anabolism (building) AND catabolism (breaking down). Basal metabolic rate is how fast these reactions occur at rest."
  },
]

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — protein structure, steroids, carbohydrate types
# ══════════════════════════════════════════════════════════════════════════════

ch2_fc = [
  # ── Protein structure levels ──────────────────────────────────────────────
  {
    "id": "ch2-fc-019", "section": "2.5", "difficulty": "medium",
    "front": "Protein primary structure",
    "back": "The SEQUENCE of amino acids in a polypeptide chain, held together by covalent peptide bonds. "
            "Determined by DNA. All higher levels of structure ultimately depend on the primary sequence."
  },
  {
    "id": "ch2-fc-020", "section": "2.5", "difficulty": "medium",
    "front": "Protein secondary structure — alpha helix and beta sheet",
    "back": "Local folding patterns stabilized by HYDROGEN BONDS between the backbone's C=O and N-H groups "
            "(NOT side chains). Alpha helix: coiled spring. Beta sheet: pleated, parallel or antiparallel strands. "
            "Example: silk = beta sheet; keratin (hair) = alpha helix."
  },
  {
    "id": "ch2-fc-021", "section": "2.5", "difficulty": "medium",
    "front": "Protein tertiary structure",
    "back": "The OVERALL 3D shape of a single polypeptide, formed by interactions between R groups (side chains): "
            "hydrophobic interactions, hydrogen bonds, ionic bonds, and disulfide bridges (covalent). "
            "This shape determines the protein's function."
  },
  {
    "id": "ch2-fc-022", "section": "2.5", "difficulty": "medium",
    "front": "Protein quaternary structure",
    "back": "Two or more polypeptide subunits (chains) associate to form a functional protein. "
            "Held by the same interactions as tertiary structure (H-bonds, hydrophobic, ionic, disulfide). "
            "Example: hemoglobin (4 subunits), collagen (3 chains). Not all proteins have quaternary structure."
  },
  # ── Steroids ──────────────────────────────────────────────────────────────
  {
    "id": "ch2-fc-023", "section": "2.5", "difficulty": "medium",
    "front": "Steroids — structure and examples",
    "back": "Lipids built on a backbone of FOUR FUSED CARBON RINGS (not fatty acid chains). "
            "Examples: cholesterol (stabilizes animal cell membranes), estrogen, testosterone (sex hormones), "
            "cortisol (stress hormone), bile salts. All derived from cholesterol."
  },
  {
    "id": "ch2-fc-024", "section": "2.5", "difficulty": "easy",
    "front": "Cholesterol — roles in the cell membrane",
    "back": "Cholesterol is a steroid embedded in animal cell membranes. It BUFFERS FLUIDITY: "
            "prevents membranes from becoming too rigid at low temperatures (wedges between phospholipids) "
            "and too fluid at high temperatures (restrains movement). Also the precursor for steroid hormones and vitamin D."
  },
  # ── Carbohydrate types ────────────────────────────────────────────────────
  {
    "id": "ch2-fc-025", "section": "2.5", "difficulty": "easy",
    "front": "Monosaccharides — glucose, fructose, galactose",
    "back": "Monosaccharides are the simplest carbohydrates (single sugars). All three are C6H12O6 isomers "
            "(same formula, different structure). Glucose: cellular fuel; fructose: fruit sugar; galactose: milk sugar. "
            "They differ in the arrangement of -OH groups, giving different tastes and metabolic fates."
  },
  {
    "id": "ch2-fc-026", "section": "2.5", "difficulty": "easy",
    "front": "Disaccharides — sucrose, lactose, maltose",
    "back": "Two monosaccharides joined by a glycosidic bond (dehydration synthesis, releases H2O). "
            "Sucrose = glucose + fructose (table sugar). Lactose = glucose + galactose (milk sugar). "
            "Maltose = glucose + glucose (malt sugar). Broken apart by hydrolysis (adds H2O)."
  },
  {
    "id": "ch2-fc-027", "section": "2.5", "difficulty": "medium",
    "front": "Glycogen vs. starch — polysaccharide energy storage",
    "back": "Both are glucose polymers for energy storage. "
            "Starch: plants store glucose as starch (amylose = unbranched; amylopectin = branched). "
            "Glycogen: animals/fungi store glucose as glycogen (highly branched for rapid mobilization). "
            "Both use alpha-1,4 glycosidic bonds; glycogen has more alpha-1,6 branch points."
  },
  {
    "id": "ch2-fc-028", "section": "2.5", "difficulty": "easy",
    "front": "Chitin — structure and location",
    "back": "A structural polysaccharide made of N-acetylglucosamine (a modified glucose with an amino group). "
            "Forms the cell walls of FUNGI and the exoskeletons of arthropods (insects, crustaceans, spiders). "
            "Strong, flexible, and resistant to hydrolysis. Analogous role to cellulose in plants."
  },
]

ch2_q = [
  # ── Protein structure ──
  {
    "id": "ch2-q-026", "section": "2.5", "difficulty": "easy",
    "question": "What defines the PRIMARY structure of a protein?",
    "choices": [
      "The coiling and folding into alpha helices and beta sheets",
      "The unique sequence of amino acids linked by peptide bonds",
      "The overall 3D shape of the folded polypeptide",
      "The number of polypeptide subunits in the protein"
    ],
    "answerIndex": 1,
    "explanation": "Primary structure is simply the amino acid sequence — the 'alphabet' of the protein, determined by the gene. Every higher level of structure (secondary, tertiary, quaternary) is a consequence of this sequence."
  },
  {
    "id": "ch2-q-027", "section": "2.5", "difficulty": "medium",
    "question": "Alpha helices and beta sheets are examples of _____ structure, stabilized by _____ bonds.",
    "choices": [
      "Primary; peptide bonds between amino acids",
      "Secondary; hydrogen bonds between backbone C=O and N-H groups",
      "Tertiary; interactions between R groups (side chains)",
      "Quaternary; disulfide bridges between subunits"
    ],
    "answerIndex": 1,
    "explanation": "Secondary structure involves local, regular folding patterns (helix or sheet) held by H-bonds between the peptide backbone atoms — NOT between R groups. R-group interactions create tertiary structure."
  },
  {
    "id": "ch2-q-028", "section": "2.5", "difficulty": "medium",
    "question": "The overall 3D shape of a single polypeptide chain is its _____ structure, mainly determined by _____ interactions.",
    "choices": [
      "Secondary; hydrogen bonds along the backbone",
      "Quaternary; attractions between different polypeptide chains",
      "Tertiary; interactions between R groups (hydrophobic, ionic, H-bonds, disulfide bridges)",
      "Primary; the covalent peptide bonds linking amino acids"
    ],
    "answerIndex": 2,
    "explanation": "Tertiary structure is the unique 3D fold of an entire polypeptide. R-group interactions drive it: nonpolar R groups cluster inward (hydrophobic core), while polar/charged groups interact outward. Disulfide bridges (-S-S-) covalently lock the shape."
  },
  {
    "id": "ch2-q-029", "section": "2.5", "difficulty": "medium",
    "question": "Which level of protein structure is ABSENT in myoglobin (a single-chain oxygen-storage protein) but PRESENT in hemoglobin (a 4-chain oxygen-transport protein)?",
    "choices": [
      "Primary structure",
      "Secondary structure",
      "Tertiary structure",
      "Quaternary structure"
    ],
    "answerIndex": 3,
    "explanation": "Quaternary structure requires multiple polypeptide subunits. Hemoglobin has 4 subunits (2 alpha + 2 beta). Myoglobin is a single polypeptide — it has primary, secondary, and tertiary structure, but NO quaternary structure."
  },
  {
    "id": "ch2-q-030", "section": "2.5", "difficulty": "medium",
    "question": "When a protein denatures (e.g., egg white cooking), which bonds are broken FIRST?",
    "choices": [
      "Peptide bonds — the primary structure is destroyed",
      "The weak bonds (hydrogen bonds, hydrophobic, ionic) maintaining secondary and tertiary structure — primary structure remains intact",
      "Only disulfide bridges — all other bonds survive denaturation",
      "Glycosidic bonds connecting sugar groups to the protein"
    ],
    "answerIndex": 1,
    "explanation": "Denaturation disrupts the weak, non-covalent bonds that maintain secondary and tertiary (and quaternary) structure. The covalent peptide bonds of the primary structure generally survive. The protein unfolds and loses function — but its amino acid sequence is unchanged."
  },
  {
    "id": "ch2-q-031", "section": "2.5", "difficulty": "easy",
    "question": "Silk is made of beta-sheet secondary structure; hair (keratin) is made of alpha helices. What do both share?",
    "choices": [
      "They are both held by R-group interactions, not backbone H-bonds",
      "Both are secondary structures stabilized by hydrogen bonds between backbone atoms (C=O···H-N)",
      "Both have quaternary structure with many polypeptide subunits",
      "Both are formed exclusively from nonpolar amino acids"
    ],
    "answerIndex": 1,
    "explanation": "Both alpha helices and beta sheets are secondary structures, stabilized by H-bonds between the carbonyl (C=O) of one peptide bond and the amino (N-H) of another. The difference is the spatial arrangement — coiled vs. extended/pleated."
  },
  # ── Steroids ──
  {
    "id": "ch2-q-032", "section": "2.5", "difficulty": "medium",
    "question": "Steroids belong to which class of macromolecule, and what defines their structure?",
    "choices": [
      "Carbohydrates; long chains of glucose monomers",
      "Proteins; chains of amino acids folded into a ring shape",
      "Lipids; a backbone of four fused carbon rings (NOT fatty acid chains)",
      "Nucleic acids; a sugar-phosphate backbone with nitrogenous bases"
    ],
    "answerIndex": 2,
    "explanation": "Steroids are lipids, but structurally distinct from triglycerides and phospholipids — they are built on four fused carbon rings. Different steroids (cholesterol, estrogen, testosterone, cortisol) vary in the functional groups attached to this ring skeleton."
  },
  {
    "id": "ch2-q-033", "section": "2.5", "difficulty": "medium",
    "question": "Cholesterol is found in animal cell membranes. Its primary function is to:",
    "choices": [
      "Act as an energy reserve, storing twice the calories of carbohydrates",
      "Form the phospholipid bilayer by providing fatty acid tails",
      "Buffer membrane fluidity — preventing membranes from becoming too rigid or too fluid with temperature changes",
      "Transport oxygen across the membrane into the cell"
    ],
    "answerIndex": 2,
    "explanation": "Cholesterol inserts between phospholipids. At low temperatures it prevents tight packing (too rigid); at high temperatures it limits excess movement (too fluid). It is also the precursor molecule for all steroid hormones and vitamin D."
  },
  # ── Carbohydrates ──
  {
    "id": "ch2-q-034", "section": "2.5", "difficulty": "easy",
    "question": "Glucose, fructose, and galactose all share the molecular formula C₆H₁₂O₆. How are they different?",
    "choices": [
      "They differ in the number of carbon atoms",
      "They are structural isomers — same formula but different arrangements of atoms, giving different properties and metabolic fates",
      "They differ in their charge; glucose is neutral, fructose is positive, galactose is negative",
      "They are identical; glucose, fructose, and galactose are different names for the same molecule"
    ],
    "answerIndex": 1,
    "explanation": "These three hexoses are structural isomers — same molecular formula (C₆H₁₂O₆) but different arrangements of -OH groups. This makes them metabolically distinct: glucose is the primary fuel, fructose is metabolized in the liver, and galactose must be converted to glucose before use."
  },
  {
    "id": "ch2-q-035", "section": "2.5", "difficulty": "easy",
    "question": "Table sugar (sucrose) is a disaccharide formed from:",
    "choices": [
      "Glucose + glucose",
      "Glucose + galactose",
      "Glucose + fructose",
      "Fructose + galactose"
    ],
    "answerIndex": 2,
    "explanation": "Sucrose (table sugar) = glucose + fructose, joined by a glycosidic bond. Lactose (milk sugar) = glucose + galactose. Maltose (malt sugar) = glucose + glucose. All disaccharides are formed by dehydration synthesis and broken apart by hydrolysis."
  },
  {
    "id": "ch2-q-036", "section": "2.5", "difficulty": "medium",
    "question": "A disaccharide forms when two monosaccharides join by a glycosidic bond. This reaction is called _____ because it _____.",
    "choices": [
      "Hydrolysis; adds a water molecule to break the bond",
      "Dehydration synthesis (condensation); removes a water molecule to form the bond",
      "Phosphorylation; transfers a phosphate group between the sugars",
      "Oxidation; removes electrons from the sugar monomers"
    ],
    "answerIndex": 1,
    "explanation": "All biological polymers (polysaccharides, proteins, nucleic acids) are built by dehydration synthesis — a water molecule is released as each monomer is added. The reverse reaction (hydrolysis) adds water to break the bond. Digestive enzymes (amylase, lactase) catalyze hydrolysis."
  },
  {
    "id": "ch2-q-037", "section": "2.5", "difficulty": "medium",
    "question": "Starch (in plants) and glycogen (in animals) are both made of glucose. The key difference is:",
    "choices": [
      "Starch uses beta-glucose; glycogen uses alpha-glucose",
      "Glycogen is much more highly branched than starch, allowing faster glucose release when energy is needed quickly",
      "Starch is soluble in water; glycogen is insoluble",
      "Starch is found in animal muscle tissue; glycogen is found in plant seeds"
    ],
    "answerIndex": 1,
    "explanation": "Both use alpha-glucose and alpha-1,4 glycosidic bonds for the main chain. Glycogen has far more alpha-1,6 branch points than starch, giving it more free ends where glucose can be added or removed rapidly. This suits animals, which need quick energy mobilization for fight-or-flight responses."
  },
  {
    "id": "ch2-q-038", "section": "2.5", "difficulty": "medium",
    "question": "Chitin differs from cellulose in that chitin:",
    "choices": [
      "Is made of beta-glucose, while cellulose is made of alpha-glucose",
      "Contains nitrogen — it is made of N-acetylglucosamine (a glucose with an amino group), found in fungal cell walls and arthropod exoskeletons rather than plant cell walls",
      "Is a storage polysaccharide in fungi, while cellulose provides structural support in animals",
      "Is fully soluble in water, making it easy to digest, unlike cellulose"
    ],
    "answerIndex": 1,
    "explanation": "Chitin's monomer is N-acetylglucosamine — glucose with an acetyl-amino group at carbon 2. This nitrogen distinguishes chitin from cellulose (pure beta-glucose). Chitin is structural, strong, and indigestible — useful for exoskeletons and fungal walls."
  },
]

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — centriole, cytoskeleton, plant vs animal, Schleiden/Schwann
# ══════════════════════════════════════════════════════════════════════════════

ch3_fc = [
  {
    "id": "ch3-fc-018", "section": "3.4", "difficulty": "easy",
    "front": "Centriole and centrosome",
    "back": "Centrioles: short cylinders of 9 triplet microtubules. Two centrioles form a centrosome "
            "(microtubule-organizing center) near the nucleus in ANIMAL cells (and some protists). "
            "During cell division, centrosomes form the mitotic spindle poles. Plant cells lack centrioles "
            "but still organize a spindle using other proteins."
  },
  {
    "id": "ch3-fc-019", "section": "3.4", "difficulty": "medium",
    "front": "Cytoskeleton — three main components",
    "back": "The cytoskeleton is a protein scaffold that maintains cell shape, enables movement, and organizes organelles. "
            "Three types: "
            "(1) Microfilaments (actin) — thinnest; cell shape, muscle contraction, cytokinesis. "
            "(2) Intermediate filaments — medium; mechanical strength, nuclear envelope support. "
            "(3) Microtubules (tubulin) — thickest; spindle fibers, cilia/flagella, organelle tracks."
  },
  {
    "id": "ch3-fc-020", "section": "3.4", "difficulty": "medium",
    "front": "Actin microfilaments vs. microtubules — key differences",
    "back": "Actin microfilaments (7 nm): made of actin protein; involved in cell shape changes, "
            "amoeboid movement, muscle contraction (with myosin), and forming the cleavage furrow. "
            "Microtubules (25 nm): made of tubulin dimers (alpha + beta); form the mitotic spindle, "
            "cilia/flagella axoneme, and motor protein highways (kinesin/dynein)."
  },
  {
    "id": "ch3-fc-021", "section": "3.2", "difficulty": "medium",
    "front": "Plant cell vs. animal cell — unique structures",
    "back": "PLANT ONLY: cell wall (cellulose), chloroplasts, large central vacuole, plasmodesmata. "
            "ANIMAL ONLY: centrioles/centrosome, lysosomes (prominent), small/no vacuoles. "
            "BOTH HAVE: plasma membrane, nucleus, mitochondria, ribosomes, rough/smooth ER, Golgi, "
            "cytoskeleton, peroxisomes."
  },
  {
    "id": "ch3-fc-022", "section": "3.1", "difficulty": "easy",
    "front": "Cell theory — three principles and key scientists",
    "back": "1. All living things are made of one or more cells. (Schleiden & Schwann, 1838-39) "
            "2. The cell is the basic unit of life. "
            "3. All cells arise from pre-existing cells. (Virchow, 1855) "
            "Matthias Schleiden (plants), Theodor Schwann (animals), Rudolf Virchow (cell division)."
  },
]

ch3_q = [
  {
    "id": "ch3-q-026", "section": "3.4", "difficulty": "easy",
    "question": "Centrioles are found in animal cells but not in most plant cells. What is their function in animal cells?",
    "choices": [
      "Synthesizing proteins for the cell membrane",
      "Forming the centrosome, which organizes spindle fibers during cell division",
      "Producing ATP for the cell division process",
      "Packaging proteins for secretion via the Golgi apparatus"
    ],
    "answerIndex": 1,
    "explanation": "Centrioles (pairs of 9-triplet microtubule cylinders) form the centrosome, which acts as the microtubule-organizing center (MTOC). During mitosis, centrosomes move to opposite poles and nucleate the spindle fibers that pull chromosomes apart. Plant cells organize spindles without centrioles."
  },
  {
    "id": "ch3-q-027", "section": "3.4", "difficulty": "medium",
    "question": "The cytoskeleton performs which of the following functions?",
    "choices": [
      "Only maintaining cell shape — it is a rigid, unchanging structure like a skeleton",
      "Maintaining cell shape, enabling cell movement and division, providing tracks for organelle transport, and forming cilia and flagella",
      "Only producing ATP needed for cellular movement",
      "Synthesizing lipids for the cell membrane and organelles"
    ],
    "answerIndex": 1,
    "explanation": "The cytoskeleton is dynamic (it assembles and disassembles). It does everything mechanical in the cell: shape, division, movement, intracellular transport. Motor proteins (kinesin, dynein, myosin) 'walk' along cytoskeletal tracks — like freight trains on rails."
  },
  {
    "id": "ch3-q-028", "section": "3.4", "difficulty": "medium",
    "question": "Which cytoskeletal component forms the mitotic spindle and is the main structural element of cilia and flagella?",
    "choices": [
      "Actin microfilaments",
      "Intermediate filaments",
      "Microtubules (made of tubulin)",
      "Spectrin fibers"
    ],
    "answerIndex": 2,
    "explanation": "Microtubules (25 nm wide, made of alpha-tubulin/beta-tubulin dimers) form the mitotic spindle and the '9+2' axoneme of cilia/flagella. Actin microfilaments are thinner and are responsible for cell shape, cleavage furrow, and muscle contraction."
  },
  {
    "id": "ch3-q-029", "section": "3.4", "difficulty": "medium",
    "question": "Actin microfilaments are particularly important for:",
    "choices": [
      "Forming chromosomal spindle fibers during cell division",
      "Providing the structural backbone of the nuclear envelope",
      "Cell shape changes, amoeboid movement, muscle contraction (with myosin), and forming the cleavage furrow during cytokinesis",
      "Building the cell wall in plant cells"
    ],
    "answerIndex": 2,
    "explanation": "Actin filaments (7 nm) interact with myosin motor proteins to produce movement — in muscle cells (sarcomeres), in crawling cells (lamellipodia), and in animal cell cytokinesis (the actin-myosin contractile ring that pinches the cell in two). They also shape microvilli in intestinal cells."
  },
  {
    "id": "ch3-q-030", "section": "3.2", "difficulty": "medium",
    "question": "Which combination of structures is found ONLY in plant cells and NOT in animal cells?",
    "choices": [
      "Mitochondria, ribosomes, and Golgi apparatus",
      "Cell wall, chloroplasts, and large central vacuole",
      "Lysosomes, centrioles, and peroxisomes",
      "Endoplasmic reticulum, nucleus, and plasma membrane"
    ],
    "answerIndex": 1,
    "explanation": "Plant cells uniquely have: a cellulose cell wall, chloroplasts (photosynthesis), and a large central vacuole (turgor pressure, storage). Animal cells uniquely have prominent lysosomes and centrioles. Both cell types share: nucleus, ER, Golgi, mitochondria, ribosomes, plasma membrane, cytoskeleton, peroxisomes."
  },
  {
    "id": "ch3-q-031", "section": "3.2", "difficulty": "medium",
    "question": "A student observes a cell with a large central vacuole, chloroplasts, and a cell wall, but no centrioles. This cell is MOST likely from a:",
    "choices": [
      "Animal muscle tissue",
      "Bacterial colony",
      "Fungal hypha",
      "Plant leaf"
    ],
    "answerIndex": 3,
    "explanation": "The combination of large central vacuole + chloroplasts + cell wall + no centrioles is characteristic of plant cells. Bacteria are prokaryotic (no membrane-bound organelles). Fungi have cell walls (chitin) but no chloroplasts. Animal cells have neither cell walls nor chloroplasts."
  },
  {
    "id": "ch3-q-032", "section": "3.1", "difficulty": "easy",
    "question": "Matthias Schleiden and Theodor Schwann contributed which principle to cell theory?",
    "choices": [
      "All cells arise from pre-existing cells (omnis cellula e cellula)",
      "All living organisms — both plants and animals — are made of cells",
      "Cells can be generated spontaneously from non-living matter",
      "The nucleus controls all cellular activities"
    ],
    "answerIndex": 1,
    "explanation": "Schleiden (1838, plants) and Schwann (1839, animals) together established that all living things are composed of cells. Virchow (1855) later added the third principle: all cells come from pre-existing cells, refuting spontaneous generation at the cellular level."
  },
]

# ── Apply ──────────────────────────────────────────────────────────────────────
print("Filling content gaps...")
add("ch1", flashcards=ch1_fc, quiz=ch1_q)
add("ch2", flashcards=ch2_fc, quiz=ch2_q)
add("ch3", flashcards=ch3_fc, quiz=ch3_q)

out = json.dumps(data, indent=2, ensure_ascii=False)
SRC.write_text(out, encoding="utf-8")
ROOT.write_text(out, encoding="utf-8")
print(f"\nWrote {SRC} and {ROOT}")
print("\nFinal counts:")
for ch in data["chapters"]:
    print(f"  {ch['id']}: {len(ch['flashcards'])} flashcards, {len(ch['quiz'])} quiz questions")
