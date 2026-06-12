"""
Adds ~10-12 more quiz questions to each of chapters 1-6.
Skips any question ID that already exists (safe to re-run).
Targets ~25 quiz questions per chapter for better rotation.
"""

import json, pathlib, sys

SRC = pathlib.Path("src/data/content.json")
ROOT = pathlib.Path("content.json")

data = json.loads(SRC.read_text(encoding="utf-8"))

# ── helpers ────────────────────────────────────────────────────────────────────

def extend_quiz(chapterId, extra_questions):
    ch = next((c for c in data["chapters"] if c["id"] == chapterId), None)
    if not ch:
        print(f"  ERROR: chapter {chapterId} not found"); return
    existing_ids = {q["id"] for q in ch["quiz"]}
    added = 0
    for q in extra_questions:
        if q["id"] not in existing_ids:
            ch["quiz"].append(q)
            added += 1
    print(f"  {chapterId}: added {added} -> now {len(ch['quiz'])} quiz questions")


# ── Chapter 1 — extra questions ────────────────────────────────────────────────
ch1_extra = [
  {
    "id": "ch1-q-016", "section": "ch1-s1", "difficulty": "easy",
    "question": "Which of the following is an example of an emergent property?",
    "choices": [
      "The individual sodium atom's charge",
      "A single neuron's electrical signal",
      "Consciousness arising from billions of interacting neurons",
      "The atomic mass of carbon"
    ],
    "answerIndex": 2,
    "explanation": "Emergent properties arise from interactions among components — no single neuron is conscious, but billions networked together produce consciousness. Life itself is an emergent property of interacting chemicals."
  },
  {
    "id": "ch1-q-017", "section": "ch1-s2", "difficulty": "medium",
    "question": "In deductive reasoning, a scientist:",
    "choices": [
      "Observes many specific cases and forms a general principle",
      "Applies a general principle to predict a specific, testable outcome",
      "Proves a hypothesis is definitely true",
      "Collects data without any prior hypothesis"
    ],
    "answerIndex": 1,
    "explanation": "Deductive reasoning moves from general to specific: 'If my hypothesis is true, then I predict this specific outcome.' Inductive reasoning moves from many specific observations to a general principle."
  },
  {
    "id": "ch1-q-018", "section": "ch1-s1", "difficulty": "easy",
    "question": "Which is the CORRECT order of levels of biological organization from smallest to largest?",
    "choices": [
      "Atom → cell → molecule → tissue → organ → organism",
      "Atom → molecule → organelle → cell → tissue → organ → organ system → organism → population → community → ecosystem → biosphere",
      "Cell → molecule → tissue → organ → organism → biosphere",
      "Organelle → atom → cell → organ → population"
    ],
    "answerIndex": 1,
    "explanation": "The hierarchy runs: atom → molecule → organelle → cell → tissue → organ → organ system → organism → population → community → ecosystem → biosphere. Each level has emergent properties not present at the level below."
  },
  {
    "id": "ch1-q-019", "section": "ch1-s2", "difficulty": "easy",
    "question": "Homeostasis is best defined as:",
    "choices": [
      "The tendency for systems to increase entropy over time",
      "Maintaining a relatively stable internal environment despite external changes",
      "The process of converting one form of energy to another",
      "The cycling of nutrients through an ecosystem"
    ],
    "answerIndex": 1,
    "explanation": "Homeostasis keeps internal conditions (temperature, pH, blood sugar, etc.) within a narrow range compatible with life. Your body sweating when hot and shivering when cold are homeostatic responses."
  },
  {
    "id": "ch1-q-020", "section": "ch1-s2", "difficulty": "easy",
    "question": "Metabolism refers to:",
    "choices": [
      "Only the reactions that break down molecules for energy",
      "The movement of materials across cell membranes",
      "All chemical reactions occurring within an organism",
      "How genetic information is passed to offspring"
    ],
    "answerIndex": 2,
    "explanation": "Metabolism encompasses ALL chemical reactions in an organism — both catabolism (breakdown) and anabolism (synthesis). Every living thing must maintain metabolism to sustain life."
  },
  {
    "id": "ch1-q-021", "section": "ch1-s2", "difficulty": "medium",
    "question": "In a well-designed experiment, which variable is deliberately changed by the researcher?",
    "choices": [
      "Dependent variable",
      "Controlled variable",
      "Independent variable",
      "Confounding variable"
    ],
    "answerIndex": 2,
    "explanation": "The independent variable is what the researcher manipulates. The dependent variable is what is measured in response. Controlled variables are kept constant to ensure the independent variable is the only thing changing."
  },
  {
    "id": "ch1-q-022", "section": "ch1-s1", "difficulty": "easy",
    "question": "A bacterium divides in two by binary fission. Which characteristic of life does this BEST represent?",
    "choices": [
      "Homeostasis",
      "Metabolism",
      "Evolution",
      "Reproduction"
    ],
    "answerIndex": 3,
    "explanation": "Reproduction — the ability to produce offspring — is one of the universal characteristics of life. Binary fission in bacteria is asexual reproduction. Without reproduction, a lineage goes extinct."
  },
  {
    "id": "ch1-q-023", "section": "ch1-s1", "difficulty": "medium",
    "question": "Two organisms are MOST closely related when they share:",
    "choices": [
      "The same geographic location",
      "The same body size and shape",
      "The most similar DNA sequences",
      "The same habitat type"
    ],
    "answerIndex": 2,
    "explanation": "DNA sequence similarity is the most reliable measure of evolutionary relatedness. Organisms that share a recent common ancestor have accumulated fewer differences in their DNA than distantly related organisms."
  },
  {
    "id": "ch1-q-024", "section": "ch1-s1", "difficulty": "easy",
    "question": "Which of these is NOT one of the three domains of life?",
    "choices": [
      "Bacteria",
      "Archaea",
      "Eukarya",
      "Protista"
    ],
    "answerIndex": 3,
    "explanation": "The three-domain system is Bacteria, Archaea, and Eukarya. Protista is a kingdom within Eukarya — it is not a domain. Fungi, Plantae, and Animalia are also kingdoms within Eukarya."
  },
  {
    "id": "ch1-q-025", "section": "ch1-s2", "difficulty": "medium",
    "question": "A scientist hypothesizes that fertilizer increases plant height. She grows 50 plants WITH fertilizer and 50 WITHOUT. Plant height is the _____ variable.",
    "choices": [
      "Independent variable — it is deliberately manipulated",
      "Dependent variable — it is measured in response to the manipulation",
      "Controlled variable — it is held constant throughout",
      "Confounding variable — it is unrelated to the experiment"
    ],
    "answerIndex": 1,
    "explanation": "Plant height is what is measured (the outcome), so it is the dependent variable. Fertilizer presence/absence is the independent variable. Things like water, soil type, and light would be controlled variables."
  },
]

# ── Chapter 2 — extra questions ────────────────────────────────────────────────
ch2_extra = [
  {
    "id": "ch2-q-014", "section": "ch2-s1", "difficulty": "easy",
    "question": "Why are noble gases (helium, neon, argon) chemically unreactive?",
    "choices": [
      "They have no protons in their nucleus",
      "Their outermost electron shell is completely full, so they do not need to gain, lose, or share electrons",
      "They are too large to form bonds with other elements",
      "They exist only as gases and cannot interact with solids"
    ],
    "answerIndex": 1,
    "explanation": "Atoms react to complete their valence shell (8 electrons for most, 2 for helium). Noble gases already have full valence shells and are therefore chemically stable and do not form bonds under normal conditions."
  },
  {
    "id": "ch2-q-015", "section": "ch2-s1", "difficulty": "easy",
    "question": "Why is carbon considered the backbone of all organic molecules?",
    "choices": [
      "Carbon is the most abundant element in the universe",
      "Carbon has 4 valence electrons, allowing it to form 4 covalent bonds and create chains, rings, and branches",
      "Carbon's bonds are stronger than those of any other element",
      "Carbon is the lightest element capable of forming long chains"
    ],
    "answerIndex": 1,
    "explanation": "Carbon's 4 valence electrons let it bond to 4 other atoms simultaneously, including other carbons, enabling the vast structural diversity of organic molecules — straight chains, branched chains, rings, and combinations."
  },
  {
    "id": "ch2-q-016", "section": "ch2-s2", "difficulty": "medium",
    "question": "Ice floats on liquid water. What causes this unusual property and why is it biologically important?",
    "choices": [
      "Ice is denser than liquid water, causing denser water to sink beneath it",
      "As water freezes, hydrogen bonds form a regular lattice that is LESS dense than liquid water — so ice floats, insulating liquid water beneath, allowing aquatic organisms to survive winter",
      "Freezing releases electrons that make ice lighter",
      "Ice floats because water is an ionic compound"
    ],
    "answerIndex": 1,
    "explanation": "In ice, hydrogen bonds organize water into an open crystalline lattice with greater spacing than liquid water. This makes ice less dense (~0.917 g/cm³ vs 1.0 g/cm³), so it floats. This insulating ice layer lets aquatic life survive in the liquid water below in winter."
  },
  {
    "id": "ch2-q-017", "section": "ch2-s2", "difficulty": "medium",
    "question": "Water's surface tension (which allows insects to walk on water) results from:",
    "choices": [
      "Water's low density compared to most solids",
      "Cohesion — hydrogen bonds between water molecules pull surface molecules inward and sideways, resisting disruption",
      "Adhesion of water to the insect's hydrophobic legs",
      "Water's high specific heat capacity"
    ],
    "answerIndex": 1,
    "explanation": "Cohesion is the attraction of water molecules to each other via hydrogen bonds. Surface water molecules are pulled inward and to the sides (not upward), creating tension. This is distinct from adhesion (water sticking to other surfaces)."
  },
  {
    "id": "ch2-q-018", "section": "ch2-s3", "difficulty": "easy",
    "question": "Which polysaccharide provides structural support in plant cell walls and cannot be digested by humans?",
    "choices": [
      "Starch",
      "Glycogen",
      "Cellulose",
      "Chitin"
    ],
    "answerIndex": 2,
    "explanation": "Cellulose is made of beta-glucose linked so the chains can hydrogen-bond with neighbors, forming strong microfibrils. Humans lack the enzyme (cellulase) to break these beta linkages, so cellulose passes as dietary fiber. Starch (alpha linkages) IS digestible."
  },
  {
    "id": "ch2-q-019", "section": "ch2-s3", "difficulty": "medium",
    "question": "A triglyceride is formed by:",
    "choices": [
      "Three glycerol molecules bonded to one fatty acid",
      "One glycerol molecule bonded to three fatty acids via ester linkages by dehydration synthesis",
      "Two fatty acids bonded to a phosphate and glycerol head",
      "Amino acids linked by peptide bonds"
    ],
    "answerIndex": 1,
    "explanation": "Triglycerides = one glycerol + three fatty acids. Each fatty acid attaches to glycerol by an ester bond formed by dehydration synthesis (loss of water). Saturated triglycerides are solid fats; unsaturated ones are liquid oils."
  },
  {
    "id": "ch2-q-020", "section": "ch2-s4", "difficulty": "medium",
    "question": "Protein denaturation means:",
    "choices": [
      "The protein gains energy and becomes hyperactive",
      "The amino acid sequence (primary structure) is destroyed by breaking peptide bonds",
      "The protein loses its 3D shape due to disruption of hydrogen bonds, ionic bonds, and other weak interactions — while the amino acid sequence remains intact",
      "The protein is completely hydrolyzed into free amino acids"
    ],
    "answerIndex": 2,
    "explanation": "Denaturation unfolds a protein's secondary and tertiary structure by disrupting the weak bonds that maintain shape. The primary structure (amino acid sequence, held by peptide bonds) is NOT broken. Denatured proteins lose function — like cooked egg white turning solid."
  },
  {
    "id": "ch2-q-021", "section": "ch2-s4", "difficulty": "easy",
    "question": "Hemoglobin (the oxygen-carrying protein in red blood cells) is made of 4 polypeptide subunits. This represents which level of protein structure?",
    "choices": [
      "Primary",
      "Secondary",
      "Tertiary",
      "Quaternary"
    ],
    "answerIndex": 3,
    "explanation": "Quaternary structure describes proteins built from multiple polypeptide chains (subunits). Hemoglobin has 4 subunits (2 alpha + 2 beta). Not all proteins have quaternary structure — myoglobin is single-chain (no quaternary)."
  },
  {
    "id": "ch2-q-022", "section": "ch2-s5", "difficulty": "easy",
    "question": "Which nitrogenous base is found in RNA but NOT in DNA?",
    "choices": [
      "Adenine",
      "Cytosine",
      "Uracil",
      "Guanine"
    ],
    "answerIndex": 2,
    "explanation": "RNA uses uracil (U) instead of thymine (T). Uracil pairs with adenine just as thymine does. Thymine has a methyl group that uracil lacks. This difference is one of several structural distinctions between DNA and RNA."
  },
  {
    "id": "ch2-q-023", "section": "ch2-s5", "difficulty": "medium",
    "question": "In DNA, the two strands of the double helix are held together by:",
    "choices": [
      "Covalent bonds between complementary bases",
      "Hydrogen bonds between complementary base pairs (A–T and G–C)",
      "Ionic bonds between the phosphate backbones",
      "Peptide bonds between nucleotides"
    ],
    "answerIndex": 1,
    "explanation": "The double helix is held together by hydrogen bonds between complementary bases: A–T (2 H-bonds) and G–C (3 H-bonds). The sugar-phosphate backbone is held by covalent bonds. Because H-bonds are weak, the two strands can be separated (unzipped) during replication and transcription."
  },
  {
    "id": "ch2-q-024", "section": "ch2-s1", "difficulty": "medium",
    "question": "Why does oil not dissolve in water ('like dissolves like')?",
    "choices": [
      "Oil molecules are too large to enter water",
      "Polar water molecules interact strongly with each other and with other polar/ionic solutes but cannot interact with nonpolar oil molecules, which have no partial charges",
      "Oil is denser than water",
      "Water's hydrogen bonds repel all hydrocarbons"
    ],
    "answerIndex": 1,
    "explanation": "Water dissolves polar and ionic substances because its partial charges attract and surround them. Nonpolar molecules (oils, fats) have no partial charges, so water cannot interact with them. Instead, water molecules form a cage around them (hydrophobic effect), pushing oil droplets together."
  },
  {
    "id": "ch2-q-025", "section": "ch2-s3", "difficulty": "easy",
    "question": "Which pair correctly matches the monomer to its polymer?",
    "choices": [
      "Amino acid → nucleic acid",
      "Fatty acid → polysaccharide",
      "Monosaccharide → polysaccharide",
      "Nucleotide → polypeptide"
    ],
    "answerIndex": 2,
    "explanation": "Monosaccharides (like glucose) are the monomers of polysaccharides (like starch, glycogen, cellulose). Amino acids → proteins/polypeptides; nucleotides → nucleic acids (DNA/RNA); fatty acids + glycerol → triglycerides."
  },
]

# ── Chapter 3 — extra questions ────────────────────────────────────────────────
ch3_extra = [
  {
    "id": "ch3-q-015", "section": "ch3-s2", "difficulty": "easy",
    "question": "What is the nucleolus and what does it do?",
    "choices": [
      "A membrane-bound organelle that stores DNA separately from the chromosomes",
      "A region within the nucleus where ribosomal RNA (rRNA) is synthesized and ribosomal subunits are assembled before export to the cytoplasm",
      "The outer boundary of the nucleus that regulates what enters and exits",
      "A type of lysosome found in the nucleus"
    ],
    "answerIndex": 1,
    "explanation": "The nucleolus (inside the nucleus but NOT membrane-bound) is a site of rRNA transcription and ribosome assembly. Cells with high protein synthesis demands — like secretory cells — have especially large, prominent nucleoli."
  },
  {
    "id": "ch3-q-016", "section": "ch3-s2", "difficulty": "easy",
    "question": "The nuclear envelope is a _____ membrane with nuclear pores that:",
    "choices": [
      "Single-layered membrane; prevent all large molecules from leaving the nucleus",
      "Double-layered membrane; control the passage of mRNA, proteins, and ribosomal subunits between the nucleus and cytoplasm",
      "Triple-layered membrane; produce energy for nuclear functions",
      "Single-layered membrane; replicate DNA before cell division"
    ],
    "answerIndex": 1,
    "explanation": "The nuclear envelope consists of two lipid bilayers. Nuclear pores are protein complexes that regulate traffic: mRNA and ribosomal subunits exit; transcription factors and DNA-repair proteins enter. This separates transcription (nucleus) from translation (cytoplasm)."
  },
  {
    "id": "ch3-q-017", "section": "ch3-s3", "difficulty": "medium",
    "question": "Cristae are inner membrane folds of mitochondria. Their function is to:",
    "choices": [
      "Store mitochondrial DNA and ribosomes",
      "Increase the inner membrane surface area, packing in more electron transport chain complexes and ATP synthase to maximize ATP production",
      "Produce ribosomal RNA for mitochondrial protein synthesis",
      "Store calcium ions for cell signaling"
    ],
    "answerIndex": 1,
    "explanation": "Cristae amplify the inner membrane surface area dramatically. The more surface area, the more ETC complexes and ATP synthase can fit, boosting ATP output. Cells with high energy demands (muscle, liver) have denser cristae. The fluid inside (matrix) is where the Krebs cycle occurs."
  },
  {
    "id": "ch3-q-018", "section": "ch3-s3", "difficulty": "medium",
    "question": "What is the PRIMARY difference between cilia and flagella?",
    "choices": [
      "Cilia are made of actin filaments; flagella are made of microtubules",
      "Cilia are short and numerous (move fluid past the cell); flagella are long and few (propel the cell through fluid)",
      "Cilia are found only in prokaryotes; flagella are only in eukaryotes",
      "They are structurally completely different but perform identical functions"
    ],
    "answerIndex": 1,
    "explanation": "Both have a '9+2' microtubule axoneme. The difference is scale and number: cilia (short, many — respiratory tract moving mucus; Paramecium swimming) vs. flagella (long, 1–2 — sperm motility, Euglena). Some eukaryotic cilia are non-motile (primary cilia for signaling)."
  },
  {
    "id": "ch3-q-019", "section": "ch3-s3", "difficulty": "medium",
    "question": "Peroxisomes neutralize hydrogen peroxide (H₂O₂) produced during certain reactions. Why is H₂O₂ dangerous to cells?",
    "choices": [
      "It is needed for photosynthesis and must be kept away from mitochondria",
      "H₂O₂ is a reactive oxygen species that oxidizes and damages DNA, proteins, and lipids — so peroxisomal catalase converts it to harmless water and O₂",
      "H₂O₂ inhibits enzyme activity by raising the pH",
      "H₂O₂ is too large to exit the cell, causing osmotic problems"
    ],
    "answerIndex": 1,
    "explanation": "Hydrogen peroxide is a reactive oxygen species (ROS) that can oxidize and damage biomolecules. Catalase in peroxisomes rapidly breaks it down: 2 H₂O₂ → 2 H₂O + O₂. Peroxisomes also oxidize fatty acids and detoxify alcohol in the liver."
  },
  {
    "id": "ch3-q-020", "section": "ch3-s2", "difficulty": "medium",
    "question": "Match the cell wall material to the correct organism group: Bacteria — Plants — Fungi",
    "choices": [
      "Cellulose — Peptidoglycan — Chitin",
      "Peptidoglycan — Cellulose — Chitin",
      "Chitin — Cellulose — Peptidoglycan",
      "Peptidoglycan — Chitin — Cellulose"
    ],
    "answerIndex": 1,
    "explanation": "Bacteria: peptidoglycan (penicillin targets its synthesis). Plants: cellulose (structural carbohydrate). Fungi: chitin (also in arthropod exoskeletons). These compositional differences are exploited by antibiotics and antifungals."
  },
  {
    "id": "ch3-q-021", "section": "ch3-s4", "difficulty": "medium",
    "question": "Both gap junctions (animals) and plasmodesmata (plants) allow:",
    "choices": [
      "Cells to prevent any communication with their neighbors for independence",
      "Direct cytoplasmic connections so ions, small molecules, and signals can pass between adjacent cells without crossing plasma membranes",
      "Large proteins to move freely between any cell in the body",
      "Cell walls to form at the midpoint between daughter cells"
    ],
    "answerIndex": 1,
    "explanation": "Gap junctions (animals) and plasmodesmata (plants) are intercellular channels that link adjacent cells' cytoplasm. This enables coordinated responses — e.g., cardiac muscle cells contract synchronously via gap junctions; plants propagate signals through plasmodesmata."
  },
  {
    "id": "ch3-q-022", "section": "ch3-s3", "difficulty": "hard",
    "question": "A drug destroys all microtubules in a dividing cell. Which process would be MOST directly and severely disrupted?",
    "choices": [
      "Protein synthesis on ribosomes",
      "ATP production in mitochondria",
      "Chromosome separation during mitosis (spindle fibers are microtubules)",
      "Lipid synthesis in the smooth ER"
    ],
    "answerIndex": 2,
    "explanation": "The mitotic spindle is built from microtubules that attach to and pull chromosomes apart. No spindle = chromosomes cannot separate = cell division fails. This is how taxol (paclitaxel) stops cancer cells — it stabilizes (hyperstabilizes) microtubules so the spindle cannot disassemble."
  },
  {
    "id": "ch3-q-023", "section": "ch3-s3", "difficulty": "easy",
    "question": "Rough ER is called 'rough' because:",
    "choices": [
      "Its membrane is irregularly shaped and jagged",
      "Ribosomes are studded on its cytoplasmic surface, giving it a bumpy appearance under electron microscopy",
      "It produces unfinished (rough) proteins that need polishing in the Golgi",
      "Its lipid bilayer is thicker and rougher than that of smooth ER"
    ],
    "answerIndex": 1,
    "explanation": "Ribosomes on the rough ER's cytoplasmic face synthesize proteins co-translationally into the ER lumen (secretory or membrane proteins). The ribosome-studded surface appears rough/bumpy under the electron microscope, in contrast to the smooth ER (no ribosomes)."
  },
  {
    "id": "ch3-q-024", "section": "ch3-s4", "difficulty": "medium",
    "question": "In the secretory pathway, what is the correct order from protein synthesis to secretion?",
    "choices": [
      "Golgi → rough ER → vesicle → plasma membrane",
      "Rough ER → transport vesicle → Golgi → secretory vesicle → plasma membrane (exocytosis)",
      "Smooth ER → rough ER → Golgi → lysosome",
      "Nucleus → Golgi → rough ER → plasma membrane"
    ],
    "answerIndex": 1,
    "explanation": "The endomembrane secretory pathway: rough ER (synthesis & initial folding) → transport vesicle → Golgi apparatus (processing, sorting, packaging) → secretory vesicle → plasma membrane fusion (exocytosis). The Golgi is the 'cellular post office,' directing cargo to the right destinations."
  },
  {
    "id": "ch3-q-025", "section": "ch3-s2", "difficulty": "medium",
    "question": "Eukaryotic cells can be much larger than prokaryotic cells mainly because:",
    "choices": [
      "They have a rigid cell wall that supports their larger size",
      "Their membrane-bound organelles divide metabolic labor, allowing efficient function at larger scales without depending entirely on diffusion across the whole cytoplasm",
      "They have more DNA and therefore need more space",
      "They evolved later and the environment allowed larger sizes"
    ],
    "answerIndex": 1,
    "explanation": "Organelle compartmentalization is key: mitochondria handle ATP, rough ER handles protein processing, lysosomes handle digestion, etc. This internal division of labor lets eukaryotes function efficiently at sizes where diffusion alone (as in prokaryotes) would be too slow."
  },
]

# ── Chapter 4 — extra questions ────────────────────────────────────────────────
ch4_extra = [
  {
    "id": "ch4-q-016", "section": "ch4-s1", "difficulty": "easy",
    "question": "The Second Law of Thermodynamics states that:",
    "choices": [
      "Energy cannot be created or destroyed, only converted",
      "Energy tends to disperse and entropy (disorder) tends to increase in any energy conversion",
      "All reactions require a catalyst to proceed",
      "Living things are exempt from the laws of thermodynamics"
    ],
    "answerIndex": 1,
    "explanation": "The Second Law: every energy conversion produces some heat (waste energy), increasing entropy. This is why no process is 100% efficient. Living organisms must continuously import energy just to maintain their organized, low-entropy state — defying local disorder by increasing entropy elsewhere."
  },
  {
    "id": "ch4-q-017", "section": "ch4-s1", "difficulty": "medium",
    "question": "In metabolism, coupled reactions refer to:",
    "choices": [
      "Two reactions that occur in the same organelle simultaneously",
      "Using the free energy released by an exergonic (energy-releasing) reaction to drive an endergonic (energy-requiring) reaction",
      "Two enzymes binding the same substrate at the same time",
      "Reactions that both require oxygen to proceed"
    ],
    "answerIndex": 1,
    "explanation": "ATP couples reactions: its hydrolysis (exergonic, −7.3 kcal/mol) releases energy used to drive otherwise unfavorable endergonic reactions (like active transport, biosynthesis). Without coupling, endergonic reactions would not proceed spontaneously."
  },
  {
    "id": "ch4-q-018", "section": "ch4-s2", "difficulty": "medium",
    "question": "A cofactor differs from a coenzyme in that a cofactor is typically:",
    "choices": [
      "An organic molecule derived from a vitamin that loosely associates with the enzyme",
      "An inorganic ion (like Mg²⁺, Zn²⁺, Fe²⁺) required for enzyme activity; coenzymes are organic helper molecules",
      "Permanently covalently bound to the enzyme and never released",
      "Always larger than the enzyme active site it assists"
    ],
    "answerIndex": 1,
    "explanation": "Cofactors are inorganic ions (Mg²⁺ in kinases, Zn²⁺ in carbonic anhydrase, Fe²⁺ in cytochromes). Coenzymes are organic molecules, often vitamin derivatives (NAD⁺ from niacin, FAD from riboflavin, Coenzyme A from pantothenic acid). Both are required for enzyme activity."
  },
  {
    "id": "ch4-q-019", "section": "ch4-s2", "difficulty": "medium",
    "question": "Feedback inhibition in a metabolic pathway means the end product:",
    "choices": [
      "Speeds up the first enzyme in the pathway to produce more end product",
      "Allosterically inhibits an enzyme early in the pathway, shutting down production when sufficient product has accumulated",
      "Competitively blocks the active site of the final enzyme in the pathway",
      "Causes all enzymes in the pathway to denature"
    ],
    "answerIndex": 1,
    "explanation": "Feedback inhibition is a regulatory mechanism where the end product binds an allosteric site on an early enzyme, changing its shape and reducing its activity. Example: isoleucine (end product) inhibits threonine deaminase (first enzyme in its synthesis pathway) when enough isoleucine exists."
  },
  {
    "id": "ch4-q-020", "section": "ch4-s3", "difficulty": "medium",
    "question": "A plant cell placed in a hypotonic solution will:",
    "choices": [
      "Lose water and undergo plasmolysis (membrane pulls away from cell wall)",
      "Gain water by osmosis; the cell wall resists bursting, resulting in turgor pressure that gives the cell rigidity",
      "Remain unchanged because plant cells are isotonic to all environments",
      "Lose its chloroplasts through exocytosis"
    ],
    "answerIndex": 1,
    "explanation": "In a hypotonic solution, water moves in by osmosis. Unlike animal cells (which lyse), plant cell walls provide pressure resistance. The resulting turgor pressure keeps plants rigid — loss of turgor (in isotonic or hypertonic solutions) causes wilting."
  },
  {
    "id": "ch4-q-021", "section": "ch4-s3", "difficulty": "easy",
    "question": "Which of these crosses the plasma membrane by SIMPLE diffusion, requiring no transport proteins?",
    "choices": [
      "Glucose (large, polar molecule)",
      "Sodium ions (Na⁺, charged)",
      "CO₂ (small, nonpolar molecule)",
      "Large proteins"
    ],
    "answerIndex": 2,
    "explanation": "Simple diffusion requires a small, nonpolar or very small polar molecule. CO₂ and O₂ pass directly through the lipid bilayer. Large polar molecules (glucose) need channel/carrier proteins (facilitated diffusion); ions need channel or pump proteins; proteins cannot diffuse through membranes."
  },
  {
    "id": "ch4-q-022", "section": "ch4-s3", "difficulty": "medium",
    "question": "Receptor-mediated endocytosis differs from phagocytosis because:",
    "choices": [
      "Receptor-mediated endocytosis uses ATP; phagocytosis is passive",
      "Receptor-mediated endocytosis specifically binds target molecules via surface receptors before engulfing them; phagocytosis nonspecifically engulfs large particles",
      "Receptor-mediated endocytosis is found only in plant cells",
      "Phagocytosis requires a nucleus; receptor-mediated endocytosis does not"
    ],
    "answerIndex": 1,
    "explanation": "Receptor-mediated endocytosis uses membrane receptors to selectively bind specific target molecules (like LDL cholesterol or viruses), then draws them in via a coated pit and vesicle. Phagocytosis ('cell eating') is a non-specific engulfment of large particles — like macrophages engulfing bacteria or debris."
  },
  {
    "id": "ch4-q-023", "section": "ch4-s1", "difficulty": "hard",
    "question": "Why must organisms continuously consume food and energy?",
    "choices": [
      "To maintain their body temperature regardless of environment",
      "Because every energy conversion produces heat (entropy increases), so organisms must continuously import free energy to maintain the low-entropy, ordered state that characterizes life",
      "Because ATP molecules can each only be used once before they are excreted",
      "To produce oxygen for cellular respiration reactions"
    ],
    "answerIndex": 1,
    "explanation": "The Second Law dictates that every metabolic reaction produces some heat (entropy). To maintain organized, ordered structures (proteins, membranes, DNA) against the tendency toward disorder, organisms must constantly import energy. Starve a cell and it quickly loses its organized state."
  },
  {
    "id": "ch4-q-024", "section": "ch4-s3", "difficulty": "medium",
    "question": "The Na⁺/K⁺ pump moves 3 Na⁺ OUT and 2 K⁺ IN per ATP hydrolyzed. This is an example of:",
    "choices": [
      "Facilitated diffusion — moving ions down concentration gradients",
      "Simple diffusion — no energy or proteins required",
      "Primary active transport — directly using ATP to move ions against their concentration gradients",
      "Secondary active transport — coupling ion movement to a pre-existing gradient"
    ],
    "answerIndex": 2,
    "explanation": "Primary active transport uses ATP directly to move solutes against their concentration gradient. The Na⁺/K⁺ pump is the classic example. It maintains resting membrane potential and is essential for nerve/muscle function. Secondary active transport (e.g., glucose cotransport) piggybacks on the Na⁺ gradient the pump creates."
  },
  {
    "id": "ch4-q-025", "section": "ch4-s2", "difficulty": "medium",
    "question": "An enzyme's active site binds its substrate. After the reaction, the enzyme is:",
    "choices": [
      "Destroyed and cannot catalyze another reaction",
      "Released unchanged and can catalyze the same reaction many times (it is a catalyst)",
      "Permanently bound to the product",
      "Only able to catalyze 1–2 more reactions before wearing out"
    ],
    "answerIndex": 1,
    "explanation": "Enzymes are catalysts — they lower activation energy and are released unchanged after each reaction, allowing them to catalyze thousands to millions of reactions per second. Enzyme activity is not consumed by the reaction; it is regulated by temperature, pH, inhibitors, and substrate concentration."
  },
]

# ── Chapter 5 — extra questions ────────────────────────────────────────────────
ch5_extra = [
  {
    "id": "ch5-q-015", "section": "ch5-s2", "difficulty": "medium",
    "question": "After electrons are energized in PSII, they pass through an electron transport chain in the thylakoid membrane. What does this electron flow accomplish?",
    "choices": [
      "It directly synthesizes glucose",
      "It pumps H⁺ ions from the stroma into the thylakoid lumen, creating a proton gradient that drives ATP synthase to produce ATP (photophosphorylation)",
      "It converts NADP⁺ to NADPH without any intermediate steps",
      "It splits water molecules to release O₂"
    ],
    "answerIndex": 1,
    "explanation": "As electrons flow through the ETC from PSII toward PSI, the energy released pumps H⁺ into the thylakoid lumen. The gradient drives ATP synthase (in the thylakoid membrane) to synthesize ATP — the same chemiosmosis principle used in mitochondria, but powered by light instead of food."
  },
  {
    "id": "ch5-q-016", "section": "ch5-s2", "difficulty": "easy",
    "question": "What provides the electrons that ultimately reduce NADP⁺ to NADPH in the light reactions?",
    "choices": [
      "CO₂ absorbed from the atmosphere",
      "Water molecules split at PSII — releasing electrons, H⁺, and O₂ as a byproduct",
      "G3P molecules from the Calvin cycle",
      "Glucose stored in the chloroplast"
    ],
    "answerIndex": 1,
    "explanation": "Water splitting (photolysis) at PSII is the source of electrons: H₂O → 2H⁺ + ½O₂ + 2e⁻. These electrons enter PSII, travel the ETC to PSI, and are ultimately used to reduce NADP⁺ to NADPH. This is also why photosynthesis releases oxygen."
  },
  {
    "id": "ch5-q-017", "section": "ch5-s3", "difficulty": "medium",
    "question": "How many CO₂ molecules must enter the Calvin cycle to produce ONE net G3P molecule?",
    "choices": [
      "1",
      "2",
      "3",
      "6"
    ],
    "answerIndex": 2,
    "explanation": "Three CO₂ are fixed per Calvin cycle 'turn' → 6 G3P are produced → 5 G3P are used to regenerate 3 RuBP → only 1 G3P exits as net product. To make one glucose (6C), 6 turns are needed (6 CO₂, 18 ATP, 12 NADPH)."
  },
  {
    "id": "ch5-q-018", "section": "ch5-s3", "difficulty": "easy",
    "question": "Which molecule in the Calvin cycle directly accepts CO₂ during carbon fixation?",
    "choices": [
      "G3P (glyceraldehyde-3-phosphate)",
      "ATP",
      "NADPH",
      "RuBP (ribulose-1,5-bisphosphate)"
    ],
    "answerIndex": 3,
    "explanation": "RuBisCO catalyzes the attachment of CO₂ to RuBP (5C) → two 3-PGA (3C) molecules. RuBP is then regenerated using ATP and NADPH (the regeneration phase). RuBisCO is the most abundant enzyme on Earth — and the entry point for nearly all carbon entering the biosphere."
  },
  {
    "id": "ch5-q-019", "section": "ch5-s4", "difficulty": "medium",
    "question": "What is photorespiration, and why is it a problem for C₃ plants?",
    "choices": [
      "Photosynthesis that occurs at night using stored ATP — a problem in cold climates",
      "When stomata close in hot, dry conditions, CO₂ drops and RuBisCO fixes O₂ instead of CO₂, producing a 2C compound that must be processed (wasting ATP and releasing CO₂) — reducing photosynthesis efficiency",
      "The use of light energy to break down glucose — the reverse of photosynthesis",
      "Excess light absorption that causes chlorophyll to degrade"
    ],
    "answerIndex": 1,
    "explanation": "RuBisCO has low specificity and accepts O₂ as an alternative substrate when CO₂ levels are low (e.g., stomata closed). This photorespiration wastes energy and carbon. C₄ and CAM plants evolved mechanisms to concentrate CO₂ around RuBisCO, minimizing this problem."
  },
  {
    "id": "ch5-q-020", "section": "ch5-s4", "difficulty": "medium",
    "question": "C₄ plants like corn and sugarcane fix CO₂ into a 4-carbon compound (oxaloacetate) in mesophyll cells and transfer it to bundle sheath cells. The ADVANTAGE of this is:",
    "choices": [
      "C₄ plants produce twice the ATP per CO₂ fixed",
      "This concentrates CO₂ around RuBisCO in bundle sheath cells, suppressing photorespiration and allowing efficient photosynthesis in hot, sunny environments",
      "C₄ plants do not need light for the Calvin cycle",
      "C₄ plants never close their stomata, allowing constant CO₂ entry"
    ],
    "answerIndex": 1,
    "explanation": "By pre-fixing CO₂ in mesophyll cells and releasing it in bundle sheath cells where RuBisCO operates, C₄ plants maintain high CO₂ concentrations around RuBisCO even when stomata are partially closed. This minimizes photorespiration and makes C₄ plants highly productive in tropical/subtropical conditions."
  },
  {
    "id": "ch5-q-021", "section": "ch5-s2", "difficulty": "hard",
    "question": "Cyclic photophosphorylation produces _____ but NOT _____.",
    "choices": [
      "NADPH but not ATP",
      "ATP but not NADPH or O₂",
      "O₂ but not ATP",
      "G3P but not NADPH"
    ],
    "answerIndex": 1,
    "explanation": "In cyclic photophosphorylation, electrons from PSI are recycled back through the ETC rather than going to NADP⁺. This pumps more H⁺ to make more ATP — but without producing NADPH or splitting water (no O₂). Useful when the cell needs more ATP relative to NADPH."
  },
  {
    "id": "ch5-q-022", "section": "ch5-s1", "difficulty": "easy",
    "question": "Why do plant leaves appear green?",
    "choices": [
      "Chlorophyll absorbs green light most efficiently and converts it to energy",
      "Chlorophyll absorbs red and blue wavelengths for photosynthesis and REFLECTS green light — the reflected green reaches our eyes",
      "Green pigments in the vacuole color the leaf without contributing to photosynthesis",
      "Leaves contain no pigment and appear green due to refraction of light"
    ],
    "answerIndex": 1,
    "explanation": "Chlorophyll's absorption spectrum peaks in red (~680 nm) and blue (~430 nm). Green wavelengths (~550 nm) are poorly absorbed and mostly reflected. The reflected green light is what we see. In autumn, chlorophyll breaks down revealing yellow/orange carotenoids (always present, just masked by green)."
  },
  {
    "id": "ch5-q-023", "section": "ch5-s4", "difficulty": "medium",
    "question": "CAM plants (like cacti and pineapple) fix CO₂ at NIGHT and store it as organic acids. During the day, stomata close and stored CO₂ is released for the Calvin cycle. The PRIMARY advantage is:",
    "choices": [
      "Photosynthesis occurs faster at night than during the day",
      "Opening stomata only at night minimizes water loss in arid environments while still obtaining CO₂ for daytime photosynthesis",
      "CAM plants do not need sunlight and can photosynthesize in total darkness",
      "The Calvin cycle runs faster when CO₂ is stored as organic acids"
    ],
    "answerIndex": 1,
    "explanation": "CAM (Crassulacean Acid Metabolism) temporally separates CO₂ capture (night, stomata open) from carbon fixation in the Calvin cycle (day, stomata closed). This allows desert plants to photosynthesize during the day without the water loss that open daytime stomata would cause."
  },
  {
    "id": "ch5-q-024", "section": "ch5-s3", "difficulty": "medium",
    "question": "If a researcher adds radioactively labeled ¹⁴CO₂ to a plant, which molecule would FIRST become radioactively labeled during the Calvin cycle?",
    "choices": [
      "ATP",
      "NADPH",
      "3-PGA (3-phosphoglycerate), then G3P",
      "O₂ released from water"
    ],
    "answerIndex": 2,
    "explanation": "RuBisCO fixes ¹⁴CO₂ onto RuBP → two molecules of 3-PGA (one carries the radioactive carbon). 3-PGA is then reduced to G3P. This Calvin-Benson-Bassham cycle was worked out by Melvin Calvin using radioactive ¹⁴C tracers in the early 1950s."
  },
  {
    "id": "ch5-q-025", "section": "ch5-s2", "difficulty": "medium",
    "question": "The absorption spectrum and action spectrum of chlorophyll closely match. What does this demonstrate?",
    "choices": [
      "All wavelengths of visible light are equally effective at driving photosynthesis",
      "The wavelengths absorbed by chlorophyll are the wavelengths that actually power photosynthesis — not just absorbed harmlessly",
      "Green light is the most effective wavelength for photosynthesis",
      "Photosynthesis works better at higher temperatures because more wavelengths are absorbed"
    ],
    "answerIndex": 1,
    "explanation": "The absorption spectrum shows which wavelengths chlorophyll absorbs; the action spectrum shows which wavelengths drive photosynthesis most effectively. Their close match proves that absorbed wavelengths are the ones doing useful work. Both peak at red and blue; both show low activity for green light."
  },
]

# ── Chapter 6 — extra questions ────────────────────────────────────────────────
ch6_extra = [
  {
    "id": "ch6-q-016", "section": "ch6-s1", "difficulty": "easy",
    "question": "Which stage of cellular respiration can occur in the ABSENCE of oxygen?",
    "choices": [
      "Pyruvate oxidation",
      "Krebs cycle",
      "Electron transport chain",
      "Glycolysis"
    ],
    "answerIndex": 3,
    "explanation": "Glycolysis occurs in the cytoplasm and has no requirement for oxygen — it evolved in ancient anaerobic environments. The other three stages (pyruvate oxidation, Krebs cycle, ETC) all require or depend on oxygen to function. Glycolysis is also the first step in fermentation."
  },
  {
    "id": "ch6-q-017", "section": "ch6-s2", "difficulty": "easy",
    "question": "What molecule directly enters the Krebs cycle, and how is it produced?",
    "choices": [
      "Glucose, directly from glycolysis",
      "Pyruvate, directly from the cytoplasm",
      "Acetyl-CoA (2-carbon), produced when pyruvate is oxidized and decarboxylated in the mitochondrial matrix",
      "NADH, produced in glycolysis"
    ],
    "answerIndex": 2,
    "explanation": "Pyruvate from glycolysis enters the mitochondrion, where pyruvate dehydrogenase removes one CO₂ and attaches the remaining 2-carbon fragment to coenzyme A → acetyl-CoA. This is pyruvate oxidation (pyruvate decarboxylation). One NADH is also produced per pyruvate."
  },
  {
    "id": "ch6-q-018", "section": "ch6-s2", "difficulty": "medium",
    "question": "How are electrons removed from organic molecules during cellular respiration and delivered to the electron transport chain?",
    "choices": [
      "As free electrons floating in the cytoplasm",
      "Carried by NADH and FADH₂ (electron carriers produced in glycolysis and the Krebs cycle)",
      "Packaged into ATP molecules for transport to the mitochondria",
      "Dissolved in the mitochondrial matrix as hydronium ions"
    ],
    "answerIndex": 1,
    "explanation": "NAD⁺ and FAD are electron carriers (oxidizing agents). When they accept electrons and H⁺ from oxidized substrates, they become NADH and FADH₂. These deliver electrons to the ETC, where energy is extracted to pump H⁺ and ultimately make ATP via chemiosmosis."
  },
  {
    "id": "ch6-q-019", "section": "ch6-s3", "difficulty": "medium",
    "question": "The inner mitochondrial membrane is impermeable to H⁺. Why is this critical for ATP synthesis?",
    "choices": [
      "It forces the matrix pH to drop, activating ATP synthase",
      "This impermeability allows H⁺ pumped by the ETC to accumulate in the intermembrane space, creating a proton gradient. H⁺ can only re-enter the matrix through ATP synthase — powering ATP production",
      "It prevents NADH from leaving the matrix before it donates electrons",
      "It allows oxygen to diffuse in but blocks CO₂, concentrating it for the Krebs cycle"
    ],
    "answerIndex": 1,
    "explanation": "If the inner membrane were leaky to H⁺, the proton gradient would dissipate without making ATP (proton leak generates heat but not ATP). This is why the cristae's impermeability is essential. Some organisms (and brown fat tissue in mammals) do uncouple H⁺ flow from ATP synthase on purpose — generating heat instead."
  },
  {
    "id": "ch6-q-020", "section": "ch6-s4", "difficulty": "medium",
    "question": "Why does alcoholic fermentation release CO₂ but lactic acid fermentation does not?",
    "choices": [
      "Yeast have a modified Krebs cycle that produces CO₂",
      "In alcoholic fermentation, pyruvate is first decarboxylated to acetaldehyde (releasing CO₂) before being reduced to ethanol. In lactic acid fermentation, pyruvate is directly reduced to lactate without any carbon being released",
      "Lactic acid fermentation uses CO₂ as a substrate rather than releasing it",
      "CO₂ is released during glycolysis, which precedes alcoholic but not lactic acid fermentation"
    ],
    "answerIndex": 1,
    "explanation": "Alcoholic: pyruvate → acetaldehyde + CO₂ (decarboxylation) → ethanol (NADH oxidized). Lactic acid: pyruvate → lactate (NADH oxidized, no carbon lost). Both regenerate NAD⁺ so glycolysis can continue. Bread rises because yeast CO₂ forms bubbles in dough."
  },
  {
    "id": "ch6-q-021", "section": "ch6-s1", "difficulty": "medium",
    "question": "Substrate-level phosphorylation differs from oxidative phosphorylation in that substrate-level phosphorylation:",
    "choices": [
      "Uses the proton gradient and ATP synthase to make ATP",
      "Directly transfers a phosphate group from a high-energy substrate molecule to ADP, making ATP without requiring the ETC or proton gradient",
      "Requires oxygen as the final electron acceptor",
      "Occurs only in the mitochondrial inner membrane"
    ],
    "answerIndex": 1,
    "explanation": "Substrate-level phosphorylation: a phosphate is directly transferred from a metabolic intermediate to ADP (example: PEP → pyruvate in glycolysis; succinyl-CoA → succinate in Krebs). Oxidative phosphorylation: the ETC + proton gradient + ATP synthase. Most ATP (~32–34 of ~36 total) comes from oxidative phosphorylation."
  },
  {
    "id": "ch6-q-022", "section": "ch6-s3", "difficulty": "medium",
    "question": "Aerobic respiration of glucose produces the same TOTAL energy as burning glucose in a flame. What makes cellular respiration more valuable?",
    "choices": [
      "Aerobic respiration releases more total energy than combustion",
      "Both release the same total free energy (~686 kcal/mol), but cellular respiration captures ~40% as ATP in small controlled steps, while combustion releases everything as heat at once",
      "Combustion is actually more efficient at capturing ATP energy",
      "Aerobic respiration requires much less oxygen than combustion"
    ],
    "answerIndex": 1,
    "explanation": "Both fully oxidize glucose to CO₂ and H₂O releasing ~686 kcal/mol. But cellular respiration releases energy gradually in small steps — each step able to power ATP synthesis — capturing ~40% as usable ATP. Burning releases it all at once as heat (entropy), useless for biological work."
  },
  {
    "id": "ch6-q-023", "section": "ch6-s2", "difficulty": "easy",
    "question": "After all 6 carbons of one glucose molecule pass completely through aerobic respiration, where do ALL the carbon atoms end up?",
    "choices": [
      "Stored in ATP molecules as chemical energy",
      "Released as 6 CO₂ molecules (2 from pyruvate oxidation + 4 from the Krebs cycle)",
      "Incorporated into NADH for transport to the ETC",
      "Built into the inner mitochondrial membrane"
    ],
    "answerIndex": 1,
    "explanation": "Glucose (6C) is fully oxidized: glycolysis → 2 pyruvate (3C each). Each pyruvate oxidation releases 1 CO₂ (2 total). Each Krebs cycle turn releases 2 CO₂ (4 total from 2 acetyl-CoA). Total: 6 CO₂. This is why you exhale CO₂ — it's the oxidized carbon from your food."
  },
  {
    "id": "ch6-q-024", "section": "ch6-s4", "difficulty": "medium",
    "question": "During intense exercise, muscle cells switch to lactic acid fermentation even though some oxygen is still present. Why?",
    "choices": [
      "The muscles run out of glucose and must use an alternative fuel",
      "Oxygen delivery to muscle mitochondria cannot keep up with ATP demand, so muscles supplement aerobic respiration with fermentation to maintain the glycolytic ATP supply",
      "Fermentation is actually more efficient than aerobic respiration at high intensity",
      "The mitochondria become too hot during intense exercise and shut down"
    ],
    "answerIndex": 1,
    "explanation": "High-intensity exercise demands ATP faster than mitochondria can supply it. Fermentation regenerates NAD⁺ so glycolysis can keep running, providing a rapid (if inefficient) ATP supply. Lactate accumulation contributes to the 'burning' sensation and muscle fatigue during intense exercise."
  },
  {
    "id": "ch6-q-025", "section": "ch6-s1", "difficulty": "medium",
    "question": "The overall reaction of cellular respiration (C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O) is essentially the reverse of photosynthesis. What does this relationship illustrate?",
    "choices": [
      "They share no enzymes or pathways and evolved independently",
      "The products of photosynthesis are the reactants of respiration and vice versa, linking energy storage (photosynthesis) and energy release (respiration) in a cycle that connects autotrophs and heterotrophs",
      "They both occur in chloroplasts using the same proteins",
      "Photosynthesis and respiration produce identical amounts of energy per reaction"
    ],
    "answerIndex": 1,
    "explanation": "Photosynthesis stores light energy as chemical energy (glucose + O₂); respiration releases that chemical energy for cellular work (releasing CO₂ + H₂O). Together they cycle carbon, oxygen, and energy between autotrophs (producers) and heterotrophs (consumers), forming the basis of nearly all life on Earth."
  },
]

# ── Apply all extras ────────────────────────────────────────────────────────────
print("Adding questions...")
extend_quiz("ch1", ch1_extra)
extend_quiz("ch2", ch2_extra)
extend_quiz("ch3", ch3_extra)
extend_quiz("ch4", ch4_extra)
extend_quiz("ch5", ch5_extra)
extend_quiz("ch6", ch6_extra)

out = json.dumps(data, indent=2, ensure_ascii=False)
SRC.write_text(out, encoding="utf-8")
ROOT.write_text(out, encoding="utf-8")
print(f"\nWrote {SRC} and {ROOT}")
print("\nFinal counts:")
for ch in data["chapters"]:
    print(f"  {ch['id']}: {len(ch['flashcards'])} flashcards, {len(ch['quiz'])} quiz questions")
