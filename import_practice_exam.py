"""
Import practice_exam_ch1-3.json into content.json.

Decisions:
  - SKIP  selectAll questions (UI doesn't support multi-select)
  - SKIP  near-identical duplicates already in content.json
  - CONVERT trueFalse → proper 4-choice MC
  - ADD    everything else (different scenarios = more exam practice)
"""

import json, pathlib

SRC  = pathlib.Path("src/data/content.json")
ROOT = pathlib.Path("content.json")

data = json.loads(SRC.read_text(encoding="utf-8"))

# ── helpers ───────────────────────────────────────────────────────────────────

def ch(cid):
    return next(c for c in data["chapters"] if c["id"] == cid)

def existing_ids(cid):
    return {q["id"] for q in ch(cid)["quiz"]}

def add(cid, questions):
    ids = existing_ids(cid)
    added = 0
    for q in questions:
        if q["id"] not in ids:
            ch(cid)["quiz"].append(q)
            added += 1
    return added

# ══════════════════════════════════════════════════════════════════════════════
# CH 1  — new IDs start at ch1-q-028
# ══════════════════════════════════════════════════════════════════════════════

ch1_new = [
  {
    "id": "ch1-q-028", "section": "1.1", "difficulty": "easy",
    "question": "A robot can move, draw power from a battery, and respond to its environment. Biologists would still NOT classify it as alive because it cannot:",
    "choices": [
      "use energy from a chemical source to power internal reactions",
      "respond to stimuli such as light, sound, or temperature changes",
      "reproduce, grow and develop, or evolve over generations",
      "maintain an internal structure that is more organized than its surroundings",
    ],
    "answerIndex": 2,
    "explanation": "Life requires ALL five characteristics. The robot fails reproduction, growth/development, and evolution — it is not alive even though it shows a few traits.",
  },
  {
    "id": "ch1-q-029", "section": "1.1", "difficulty": "medium",
    "question": "A single ant cannot regulate a colony's temperature, but a whole colony can. This best illustrates:",
    "choices": [
      "homeostasis failure at the organismal level",
      "an emergent property arising from interactions among components",
      "natural selection acting on individual insects",
      "asexual reproduction producing genetically identical workers",
    ],
    "answerIndex": 1,
    "explanation": "Emergent properties arise from interactions among components and do not exist in any single component alone — a hallmark of complex biological systems.",
  },
  {
    "id": "ch1-q-030", "section": "1.1", "difficulty": "medium",
    "question": "A plant captures sunlight and builds sugars. With respect to energy, the plant is best described as:",
    "choices": [
      "a heterotroph that produces energy from photons",
      "an autotroph that converts light energy into chemical energy",
      "a decomposer that absorbs energy from decaying organic matter",
      "a consumer that stores light in its chlorophyll pigments",
    ],
    "answerIndex": 1,
    "explanation": "Autotrophs convert energy from a nonliving source (sunlight) into chemical energy in food. Nothing 'produces' energy from nothing — that would violate thermodynamics.",
  },
  # ch1-pe-005 converted from trueFalse
  {
    "id": "ch1-q-031", "section": "1.1", "difficulty": "easy",
    "question": "Which statement about decomposers is correct?",
    "choices": [
      "Decomposers are autotrophs that produce organic molecules from inorganic compounds using sunlight or chemical energy",
      "Decomposers are heterotrophs that absorb nutrients from dead organic matter, recycling compounds back into the ecosystem",
      "Decomposers are chemotrophs that oxidize inorganic minerals to obtain energy for building organic molecules",
      "Decomposers are both autotrophs and heterotrophs, alternating strategies based on whether light is available",
    ],
    "answerIndex": 1,
    "explanation": "Decomposers (mostly fungi and some bacteria) are heterotrophs that absorb nutrients from dead matter and recycle nutrients, not autotrophs that make their own food.",
  },
  {
    "id": "ch1-q-032", "section": "1.1", "difficulty": "easy",
    "question": "When you exercise, you sweat and blood vessels widen to release heat, keeping body temperature near 37°C. This maintenance of a stable internal environment despite external change is:",
    "choices": [
      "evolution — gradual genetic adaptation of the body to temperature stress",
      "metabolism — the total of all chemical reactions occurring inside cells",
      "homeostasis — regulated maintenance of stable internal conditions",
      "development — programmed changes in body structure that occur with age",
    ],
    "answerIndex": 2,
    "explanation": "Homeostasis is the maintenance of stable internal conditions via sense-and-counteract feedback loops. Sweating and vasodilation are classic homeostatic responses.",
  },
  {
    "id": "ch1-q-033", "section": "1.1", "difficulty": "easy",
    "question": "Offspring produced by sexual reproduction differ genetically from their parents primarily because:",
    "choices": [
      "one parent copies its DNA exactly and the copy accumulates random errors over time",
      "two parents combine their genetic information, generating new combinations of traits",
      "mutations always occur at a higher rate during sexual reproduction than asexual reproduction",
      "development introduces entirely new genes not present in either parent",
    ],
    "answerIndex": 1,
    "explanation": "Sexual reproduction combines DNA from two parents, producing genetic variation that helps populations adapt through natural selection.",
  },
  {
    "id": "ch1-q-034", "section": "1.2", "difficulty": "medium",
    "question": "Two organisms are both single-celled and lack a nucleus, but their DNA sequences and membrane chemistry differ fundamentally. They most likely belong to:",
    "choices": [
      "the same domain, since their shared prokaryotic cell plan places them in a single evolutionary lineage",
      "two different domains — Bacteria and Archaea — which diverged early despite their similar appearance",
      "the same kingdom within domain Eukarya, grouped by their unicellular prokaryotic body plan",
      "domain Eukarya, because multicellular organisms cannot arise from organisms with such primitive cell plans",
    ],
    "answerIndex": 1,
    "explanation": "Bacteria and Archaea are both prokaryotic (no nucleus) but are placed in separate domains based on molecular and membrane-chemistry differences that reveal deep evolutionary divergence.",
  },
  {
    "id": "ch1-q-035", "section": "1.2", "difficulty": "medium",
    "question": "A eukaryotic organism is multicellular and obtains nutrients by secreting enzymes onto its food and absorbing the products. It belongs to kingdom:",
    "choices": [
      "Plantae — plants produce food via photosynthesis and absorb water and minerals through roots",
      "Animalia — animals rely on external digestion using secreted enzymes before ingesting dissolved nutrients",
      "Fungi — fungi digest food externally and absorb nutrients, unlike animals that ingest and digest internally",
      "Protista — all unicellular absorptive eukaryotes are classified here regardless of body complexity",
    ],
    "answerIndex": 2,
    "explanation": "Fungi digest food externally by secreting enzymes, then absorb the products. Animals ingest food and digest it internally.",
  },
  {
    "id": "ch1-q-036", "section": "1.2", "difficulty": "medium",
    "question": "Which statement about kingdom Protista is most accurate?",
    "choices": [
      "It is a tightly unified group of closely related eukaryotes that share a common ancestor not shared by plants, animals, or fungi",
      "It is an artificial 'leftover' grouping of diverse eukaryotic lineages that do not fit Plantae, Fungi, or Animalia",
      "It contains only prokaryotes whose complexity puts them above bacteria but below true eukaryotes",
      "It represents a fourth domain of life independent of Bacteria, Archaea, and Eukarya",
    ],
    "answerIndex": 1,
    "explanation": "Protista is not a true kingdom — it is an artificial grouping of several distinct eukaryotic lineages. Biologists continue to revise its classification using molecular data.",
  },
  {
    "id": "ch1-q-037", "section": "1.3", "difficulty": "medium",
    "question": "'Drinking green tea lowers blood pressure' is best classified as a:",
    "choices": [
      "prediction — a specific if-then outcome that can be tested in one experiment",
      "hypothesis — a tentative, testable explanation for an observed pattern",
      "theory — a broad explanation supported by extensive experimental evidence",
      "control — a baseline condition used to isolate the effect of the independent variable",
    ],
    "answerIndex": 1,
    "explanation": "A hypothesis is a tentative, testable explanation. A prediction is the specific if-then outcome that follows FROM the hypothesis.",
  },
  {
    "id": "ch1-q-038", "section": "1.3", "difficulty": "medium",
    "question": "A lawn mower has stopped running. A mechanic hypothesizes 'the mower stopped because it is out of gas.' Which is the matching prediction?",
    "choices": [
      "The mower's carburetor is blocked with debris and must be cleaned before the engine will start",
      "Gasoline provides chemical energy that the engine converts into mechanical motion",
      "If I add gasoline to the tank, then the mower will start",
      "The mower stopped because the spark plugs failed to ignite the fuel-air mixture",
    ],
    "answerIndex": 2,
    "explanation": "A prediction is a specific, testable if-then statement derived from the hypothesis. 'If I add gas, then the mower will start' directly tests the out-of-gas hypothesis.",
  },
  {
    "id": "ch1-q-039", "section": "1.3", "difficulty": "easy",
    "question": "In a vaccine study, one group receives the vaccine and another receives a saline injection with no active ingredient. The saline group is the:",
    "choices": [
      "independent variable — the factor the researcher deliberately changes",
      "dependent variable — the measurable outcome that changes in response to the treatment",
      "control group — the untreated baseline that allows comparison with the experimental group",
      "standardized variable — a condition kept constant to prevent it from affecting results",
    ],
    "answerIndex": 2,
    "explanation": "The control group receives no active treatment (here, a placebo injection), providing a baseline to determine whether any observed changes are actually caused by the vaccine.",
  },
  {
    "id": "ch1-q-040", "section": "1.3", "difficulty": "easy",
    "question": "A researcher tests three doses of a new drug and measures tumor size in each group. Tumor size is the:",
    "choices": [
      "independent variable — what the researcher manipulates to cause a change",
      "dependent variable — what is measured to detect the effect of the treatment",
      "control — the condition without treatment used for comparison",
      "placebo — the inactive substitute given to the control group",
    ],
    "answerIndex": 1,
    "explanation": "The dependent variable is what is measured as the outcome — here tumor size. The drug dose is the independent variable manipulated by the researcher.",
  },
  {
    "id": "ch1-q-041", "section": "1.3", "difficulty": "medium",
    "question": "Volunteers count and identify bird species at the same locations every winter for 30 years, without changing or manipulating anything. This project is an example of:",
    "choices": [
      "experimental science — a controlled manipulation of variables to establish cause-and-effect",
      "discovery science — systematic observation and data collection without manipulating variables",
      "a double-blind study — observers and coordinators are unaware of the hypotheses being tested",
      "hypothesis-driven research — each observation tests a specific prediction about population change",
    ],
    "answerIndex": 1,
    "explanation": "Discovery science collects data through systematic observation without manipulating variables. Experimental science deliberately manipulates an independent variable.",
  },
  # ch1-pe-020 converted from trueFalse
  {
    "id": "ch1-q-042", "section": "1.3", "difficulty": "easy",
    "question": "Which question is OUTSIDE the scope of science to answer?",
    "choices": [
      "Does increasing atmospheric CO2 raise average global temperatures?",
      "Which genetic mutations are associated with elevated risk of type 2 diabetes?",
      "Is the Mona Lisa a more beautiful painting than Starry Night?",
      "How do capsaicin molecules in jalapenos activate pain receptors in the mouth?",
    ],
    "answerIndex": 2,
    "explanation": "Science only addresses testable questions about the natural world. Aesthetic judgments (beauty), ethical questions, and the supernatural fall outside science's scope.",
  },
]

# ══════════════════════════════════════════════════════════════════════════════
# CH 2  — new IDs start at ch2-q-039
# ══════════════════════════════════════════════════════════════════════════════

ch2_new = [
  {
    "id": "ch2-q-039", "section": "2.1", "difficulty": "easy",
    "question": "Which four elements make up approximately 96% of the human body by mass?",
    "choices": [
      "Carbon, hydrogen, oxygen, calcium",
      "Carbon, hydrogen, oxygen, nitrogen",
      "Carbon, oxygen, iron, sodium",
      "Hydrogen, oxygen, sulfur, calcium",
    ],
    "answerIndex": 1,
    "explanation": "CHON: carbon, hydrogen, oxygen, and nitrogen are the bulk elements used to build the carbohydrates, proteins, lipids, and nucleic acids that make up most of the body.",
  },
  {
    "id": "ch2-q-040", "section": "2.1", "difficulty": "easy",
    "question": "The atomic number of an element is defined as the number of:",
    "choices": [
      "neutrons in the nucleus, which determines the isotope",
      "protons in the nucleus, which defines the element's identity",
      "electrons in the outermost valence shell, which determines bonding behavior",
      "protons plus neutrons, which gives the element its atomic mass",
    ],
    "answerIndex": 1,
    "explanation": "Atomic number = number of protons. It uniquely identifies the element. Protons + neutrons = mass number.",
  },
  {
    "id": "ch2-q-041", "section": "2.1", "difficulty": "medium",
    "question": "Two atoms both have 6 protons, but one has 6 neutrons and the other has 8. They are:",
    "choices": [
      "different elements, because the number of neutrons determines the element's chemical identity",
      "ions of each other — the extra neutrons create a charge difference that makes one atom positive",
      "isotopes of carbon — same element, same chemical behavior, but different atomic masses",
      "molecules — two atoms that share the same number of protons naturally bond to form a compound",
    ],
    "answerIndex": 2,
    "explanation": "Same number of protons but different neutrons = isotopes of the same element. Here, carbon-12 (6 neutrons) and carbon-14 (8 neutrons) are both carbon.",
  },
  {
    "id": "ch2-q-042", "section": "2.1", "difficulty": "easy",
    "question": "Iron and iodine are needed in tiny amounts but their absence causes diseases such as anemia and goiter. They are classified as:",
    "choices": [
      "bulk elements — the four main elements (C, H, O, N) that make up most biological molecules",
      "trace elements — required in small amounts but essential for health",
      "isotopes — radioactive forms of common elements that serve specialized biological roles",
      "ions only — these elements function exclusively as charged particles, never as neutral atoms",
    ],
    "answerIndex": 1,
    "explanation": "Trace elements are required in very small (trace) amounts but are nonetheless essential. Deficiency causes specific, predictable diseases.",
  },
  {
    "id": "ch2-q-043", "section": "2.1", "difficulty": "easy",
    "question": "A hydrogen atom donates its single electron to another atom. The hydrogen is now:",
    "choices": [
      "a neutron — losing its electron converts a proton-electron pair into a neutral neutron",
      "an isotope — gaining or losing electrons changes the mass of the atom",
      "an ion (H+) — with no electron, the remaining proton carries a positive charge",
      "a covalent bond — the donated electron creates a shared pair between the two atoms",
    ],
    "answerIndex": 2,
    "explanation": "An atom that gains or loses electrons becomes a charged ion. H that loses its electron leaves behind just a proton — the ion H+.",
  },
  {
    "id": "ch2-q-044", "section": "2.2", "difficulty": "medium",
    "question": "Sodium has an electronegativity of 0.9 and chlorine has 3.0. Based on this large difference, what type of bond forms?",
    "choices": [
      "A nonpolar covalent bond — large electronegativity differences produce equal electron sharing",
      "A polar covalent bond — partial charges develop but both atoms still share the electrons",
      "An ionic bond — chlorine strips sodium's electron completely, forming Na+ and Cl-",
      "A hydrogen bond — atoms with extreme electronegativity differences always form hydrogen bonds",
    ],
    "answerIndex": 2,
    "explanation": "A difference greater than ~1.7 leads to electron TRANSFER rather than sharing: Na loses its electron to Cl, producing Na+ and Cl- ions held together by electrostatic attraction.",
  },
  {
    "id": "ch2-q-045", "section": "2.2", "difficulty": "medium",
    "question": "In a water molecule, the oxygen carries a partial negative charge (δ-) and each hydrogen carries a partial positive charge (δ+). This is because:",
    "choices": [
      "oxygen has more protons than hydrogen, so the nucleus attracts the bonding electrons more strongly",
      "oxygen is more electronegative and pulls the shared electrons closer, creating an unequal charge distribution",
      "oxygen completely strips the electrons from hydrogen, forming ionic bonds within the water molecule",
      "hydrogen bonds between water molecules donate extra electron density to the oxygen atom",
    ],
    "answerIndex": 1,
    "explanation": "Oxygen is more electronegative than hydrogen, pulling shared electrons toward itself. This creates a polar covalent bond with partial charges — the basis for water's remarkable properties.",
  },
  # ch2-pe-009 converted from trueFalse
  {
    "id": "ch2-q-046", "section": "2.2", "difficulty": "medium",
    "question": "Which correctly compares a single hydrogen bond to a covalent bond in terms of bond strength?",
    "choices": [
      "Hydrogen bonds are stronger than covalent bonds, which is why water's hydrogen bonds hold the molecule together so tightly",
      "Hydrogen bonds and covalent bonds are approximately equal in strength — their difference lies only in the atoms involved",
      "A single hydrogen bond is much weaker than a covalent bond, but many hydrogen bonds acting together provide significant stabilizing force in water, DNA, and proteins",
      "Hydrogen bonds are as strong as covalent bonds but are reversible, breaking and reforming without requiring or releasing energy",
    ],
    "answerIndex": 2,
    "explanation": "Individual hydrogen bonds are weak (~5 vs ~350 kJ/mol for C-C), but their collective effect stabilizes ice, keeps DNA's two strands together, and holds protein 3D shape.",
  },
  {
    "id": "ch2-q-047", "section": "2.2", "difficulty": "medium",
    "question": "H2 (hydrogen gas) is a molecule but NOT a compound, whereas H2O is both a molecule and a compound. Which statement explains this?",
    "choices": [
      "A compound must contain atoms of two or more different elements; H2 has only one element",
      "A molecule must contain only one element; H2O contains two, making it a compound rather than a molecule",
      "They are identical terms — all molecules are compounds and all compounds are molecules",
      "A compound cannot also be a molecule; only ionic substances like NaCl are truly compounds",
    ],
    "answerIndex": 0,
    "explanation": "A compound contains two or more DIFFERENT elements. H2 is a molecule (two bonded atoms) but not a compound (only one element). H2O is both a molecule and a compound.",
  },
  {
    "id": "ch2-q-048", "section": "2.3", "difficulty": "medium",
    "question": "Water climbs upward through a thin paper towel even against gravity. This is primarily due to water's:",
    "choices": [
      "cohesion — water molecules sticking to each other via hydrogen bonds",
      "adhesion — water molecules forming hydrogen bonds with polar fibers in the paper",
      "high specific heat — stored thermal energy drives water molecules upward through capillary action",
      "surface tension — the skin of water at the paper surface pulls more water upward from below",
    ],
    "answerIndex": 1,
    "explanation": "Adhesion is the tendency of water molecules to form hydrogen bonds with other polar surfaces, such as cellulose fibers in paper, pulling water upward through capillary action.",
  },
  {
    "id": "ch2-q-049", "section": "2.4", "difficulty": "medium",
    "question": "A solution at pH 4 is how many times more acidic than a solution at pH 7?",
    "choices": [
      "3 times more acidic — the difference of 3 pH units equals a 3-fold increase in H+ concentration",
      "30 times more acidic — each pH unit represents a 10-fold change, so 3 units = 30-fold",
      "300 times more acidic — the logarithmic scale multiplies the concentration by 100 per unit",
      "1000 times more acidic — the pH scale is base-10 logarithmic, so 3 units = 10 x 10 x 10",
    ],
    "answerIndex": 3,
    "explanation": "The pH scale is base-10 logarithmic: each 1-unit decrease = 10x more H+. A drop of 3 units (pH 7 to 4) = 10 × 10 × 10 = 1000 times more acidic.",
  },
  {
    "id": "ch2-q-050", "section": "2.4", "difficulty": "medium",
    "question": "Blood pH must stay near 7.4 to prevent cellular damage. Buffers keep it stable by:",
    "choices": [
      "continuously producing H+ ions that neutralize any base added to the blood",
      "raising blood temperature when pH drops, which chemically drives H+ ions out of solution",
      "absorbing excess H+ when acid is added and releasing H+ when base is added, resisting large pH changes",
      "removing all H+ ions from the blood before they can alter pH, maintaining a pure neutral solution",
    ],
    "answerIndex": 2,
    "explanation": "A buffer resists pH change by acting as both an acid and a base — absorbing excess H+ when acids are added and donating H+ when bases are added.",
  },
  {
    "id": "ch2-q-051", "section": "2.5", "difficulty": "easy",
    "question": "Digestive enzymes in your small intestine break starch into glucose units by adding a water molecule across each glycosidic bond. This reaction is called:",
    "choices": [
      "dehydration synthesis — water is removed to build a covalent bond between two monomers",
      "hydrolysis — water is added to break a covalent bond, separating the polymer into monomers",
      "denaturation — the starch loses its 3D shape due to pH and enzyme activity in the gut",
      "evaporation — dissolved sugars are driven into the bloodstream by the water vapor released",
    ],
    "answerIndex": 1,
    "explanation": "Hydrolysis ('water-splitting') adds a water molecule to break polymer bonds into monomers. Dehydration synthesis is the reverse: removing water to build polymers from monomers.",
  },
  {
    "id": "ch2-q-052", "section": "2.5", "difficulty": "medium",
    "question": "Glucose and fructose share the molecular formula C6H12O6 but taste and react differently. This is because they differ in:",
    "choices": [
      "the total number of atoms — glucose has more carbons while fructose has more oxygens",
      "the arrangement of their atoms — same formula, different structural arrangement gives different properties",
      "molecular weight — fructose is heavier, making it sweeter and harder for enzymes to break down",
      "the elements they contain — fructose contains phosphorus while glucose does not",
    ],
    "answerIndex": 1,
    "explanation": "Glucose and fructose are structural isomers — same atoms, different arrangement. The structural difference changes how they interact with enzymes, receptors, and taste buds.",
  },
  {
    "id": "ch2-q-053", "section": "2.5", "difficulty": "easy",
    "question": "The covalent bond that links two amino acids together during protein synthesis is called a:",
    "choices": [
      "hydrogen bond — the weak attraction between an N-H group of one amino acid and the C=O of another",
      "ionic bond — the electrostatic attraction between oppositely charged R groups on adjacent amino acids",
      "peptide bond — formed by dehydration synthesis between the carboxyl group of one amino acid and the amino group of the next",
      "glycosidic bond — the bond that links monosaccharides in carbohydrate polymers",
    ],
    "answerIndex": 2,
    "explanation": "A peptide bond is a covalent bond formed between the -COOH of one amino acid and the -NH2 of the next, releasing water (dehydration synthesis).",
  },
  {
    "id": "ch2-q-054", "section": "2.5", "difficulty": "easy",
    "question": "Which level of protein structure is simply the linear order of amino acids in the polypeptide chain?",
    "choices": [
      "Primary structure — the sequence of amino acids linked by peptide bonds",
      "Secondary structure — the local folding patterns (alpha helices, beta sheets) stabilized by backbone hydrogen bonds",
      "Tertiary structure — the overall 3D shape from interactions among R groups (side chains)",
      "Quaternary structure — the association of two or more polypeptide subunits into one functional protein",
    ],
    "answerIndex": 0,
    "explanation": "Primary structure is the unique amino acid sequence. It determines all higher levels of structure because the R groups dictate how the chain will fold.",
  },
  {
    "id": "ch2-q-055", "section": "2.5", "difficulty": "medium",
    "question": "A single strand of DNA reads 5'-A-T-C-G-3'. Its complementary strand reads:",
    "choices": [
      "5'-A-T-C-G-3' — the template and complementary strands are always identical in sequence",
      "5'-T-A-G-C-3' — complementary base pairing: A pairs with T, and C pairs with G",
      "5'-U-A-G-C-3' — RNA complementary to the DNA template incorporates uracil opposite adenine",
      "5'-G-C-T-A-3' — the complementary strand reads in the same direction with swapped bases",
    ],
    "answerIndex": 1,
    "explanation": "DNA base pairing: A pairs with T, and C pairs with G. The complementary strand of 5'-ATCG-3' is 5'-CGAT-3', which written antiparallel (3' to 5' aligned with 5' to 3') reads 5'-TAGC-3'.",
  },
  # ch2-pe-024 converted from trueFalse
  {
    "id": "ch2-q-056", "section": "2.5", "difficulty": "easy",
    "question": "Which correctly describes how RNA differs from DNA?",
    "choices": [
      "RNA is double-stranded and contains deoxyribose sugar, while DNA is single-stranded and contains ribose sugar",
      "RNA uses thymine (T) where DNA uses uracil (U), and both are usually double-stranded",
      "RNA contains uracil (U) instead of thymine (T) and is usually single-stranded",
      "RNA and DNA have identical nucleotide bases; they differ only in whether they are found in the nucleus or cytoplasm",
    ],
    "answerIndex": 2,
    "explanation": "DNA uses A, C, G, T and is double-stranded; RNA uses A, C, G, U (uracil replaces thymine) and is usually single-stranded. RNA also uses ribose sugar rather than deoxyribose.",
  },
  # ch2-pe-026 converted from trueFalse
  {
    "id": "ch2-q-057", "section": "2.5", "difficulty": "medium",
    "question": "Which correctly explains how lipids differ from carbohydrates, proteins, and nucleic acids?",
    "choices": [
      "Lipids are the only organic class that contains nitrogen; the other three are built only from C, H, and O",
      "Unlike carbohydrates, proteins, and nucleic acids (true polymers assembled from repeating monomers), lipids are NOT true polymers — they are a diverse hydrophobic group with varied structures",
      "Lipids are assembled by ribosomes from an mRNA template, just as proteins are — the ribosome reads a lipid code to add fatty acids in sequence",
      "Lipids form the largest macromolecules in living cells — a single lipid molecule is larger than most protein polymers",
    ],
    "answerIndex": 1,
    "explanation": "Lipids are NOT true polymers; they are a chemically diverse group unified by hydrophobicity, not by a repeating monomer subunit. The other three classes (carbs, proteins, nucleic acids) are all built from monomers.",
  },
]

# ══════════════════════════════════════════════════════════════════════════════
# CH 3  — new IDs start at ch3-q-037
# ══════════════════════════════════════════════════════════════════════════════

ch3_new = [
  {
    "id": "ch3-q-037", "section": "3.1", "difficulty": "medium",
    "question": "Which is one of the THREE original statements of the cell theory as proposed by Schleiden, Schwann, and Virchow?",
    "choices": [
      "All cells have the same chemical composition and perform identical metabolic reactions",
      "All cells use oxygen to produce ATP through cellular respiration",
      "All cells come from preexisting cells — spontaneous generation of cells does not occur",
      "All cells contain mitochondria that generate the ATP required for growth and division",
    ],
    "answerIndex": 2,
    "explanation": "The three original tenets: (1) all living things are made of cells; (2) the cell is the basic unit of life; (3) all cells come from preexisting cells (Virchow). The others are modern additions.",
  },
  {
    "id": "ch3-q-038", "section": "3.1", "difficulty": "medium",
    "question": "A scientist wants to view the 3D external surface texture of a pollen grain in detail. The most appropriate tool is a:",
    "choices": [
      "light microscope — its visible-light beam reveals fine surface texture at high magnification",
      "transmission electron microscope (TEM) — electrons passing through thin sections reveal 3D surface contours",
      "scanning electron microscope (SEM) — a focused electron beam scans the surface to build a 3D image of the exterior",
      "confocal microscope — fluorescent tags on the surface proteins map 3D structure using laser light",
    ],
    "answerIndex": 2,
    "explanation": "SEM scans the surface with electrons, creating a detailed 3D image of external texture. TEM passes electrons through a thin slice, revealing internal 2D ultrastructure.",
  },
  {
    "id": "ch3-q-039", "section": "3.1", "difficulty": "easy",
    "question": "The ability to distinguish two closely spaced points as separate objects rather than blurring them together is a microscope's:",
    "choices": [
      "magnification — how many times larger the image appears compared to the actual object",
      "resolution — the minimum distance at which two points can still be seen as distinct",
      "contrast — the difference in brightness between stained structures and the background",
      "wavelength — the size of the photons or electrons used to illuminate the specimen",
    ],
    "answerIndex": 1,
    "explanation": "Resolution is the ability to distinguish two close points; magnification is how much larger the image appears. High magnification without high resolution just produces a bigger blur.",
  },
  {
    "id": "ch3-q-040", "section": "3.1", "difficulty": "medium",
    "question": "Why do most cells remain very small (10–100 µm) rather than growing larger?",
    "choices": [
      "Small cells contain more DNA relative to their size, enabling faster gene expression and faster growth",
      "As a cell grows larger, its volume increases faster than its surface area, reducing the cell's ability to exchange materials quickly enough",
      "Large cells cannot physically fit the organelles needed for metabolism into their cytoplasm",
      "Surface area increases faster than volume as a cell grows, creating excess membrane that the cell cannot maintain",
    ],
    "answerIndex": 1,
    "explanation": "Volume grows as the cube of radius; surface area grows as the square. As cells enlarge, there is less membrane surface per unit of cytoplasm, slowing material exchange.",
  },
  {
    "id": "ch3-q-041", "section": "3.1", "difficulty": "hard",
    "question": "A cube measuring 3 cm on each side has a surface-area-to-volume ratio of:",
    "choices": [
      "1.0 — SA = 6(3)^2 = 54, V = 3^3 = 27, ratio = 2.0... let me recalculate: 54/27 = 2.0",
      "2.0 — SA = 6 × 9 = 54 cm², V = 27 cm³, ratio = 54 ÷ 27 = 2.0",
      "3.0 — SA = 3 × 9 = 27 cm², V = 3^3 = 27 cm³, ratio = 27 ÷ 27 = 1.0",
      "6.0 — SA = 6 × 3 = 18 cm², V = 3^3 = 27 cm³, ratio = 18 ÷ 27 = 0.67",
    ],
    "answerIndex": 1,
    "explanation": "SA = 6 faces × (3 cm)² = 54 cm². V = (3 cm)³ = 27 cm³. SA:V = 54/27 = 2.0. As cells grow larger, this ratio decreases — each unit of volume has less surface area for exchange.",
  },
  {
    "id": "ch3-q-042", "section": "3.2", "difficulty": "easy",
    "question": "The single most fundamental structural difference between a prokaryotic cell and a eukaryotic cell is that eukaryotes have:",
    "choices": [
      "ribosomes that synthesize proteins — prokaryotes use a different mechanism for translation",
      "a cell membrane that separates the cell's interior from its environment",
      "a membrane-bound nucleus enclosing the DNA — prokaryotes have no such membrane around their genetic material",
      "DNA that encodes genetic information — prokaryotic cells store information in RNA instead",
    ],
    "answerIndex": 2,
    "explanation": "The defining feature of eukaryotes is the membrane-bound nucleus. Prokaryotes have a nucleoid region — DNA without a surrounding membrane — plus they lack other membrane-bound organelles.",
  },
  {
    "id": "ch3-q-043", "section": "3.2", "difficulty": "medium",
    "question": "A bacterial cell's DNA is contained in a region called the nucleoid. How does this differ from a eukaryotic nucleus?",
    "choices": [
      "The nucleoid contains no genetic information — it stores only ribosomes and transfer RNA molecules",
      "The nucleoid is not surrounded by a membrane — the eukaryotic nucleus encloses DNA in a double membrane",
      "The nucleoid is larger than the eukaryotic nucleus because bacteria have more total DNA than eukaryotes",
      "The nucleoid contains only ribosomes and RNA; DNA in bacteria floats freely throughout the entire cytoplasm",
    ],
    "answerIndex": 1,
    "explanation": "The nucleoid is a region where DNA is concentrated in bacteria, but it has NO surrounding membrane. A eukaryotic nucleus has a double membrane (nuclear envelope) with pores.",
  },
  {
    "id": "ch3-q-044", "section": "3.3", "difficulty": "medium",
    "question": "A phospholipid differs from a triglyceride (neutral fat) in that a phospholipid has:",
    "choices": [
      "three fatty acid tails and a glycerol backbone, making it larger than a triglyceride",
      "two fatty acids and a phosphate group replacing the third fatty acid, making it amphipathic",
      "no glycerol backbone — phospholipids link fatty acids directly to the phosphate group",
      "only a phosphate group with no fatty acid tails, making it completely hydrophilic",
    ],
    "answerIndex": 1,
    "explanation": "A phospholipid = glycerol + 2 fatty acids + phosphate group (+ small head group). The phosphate makes it amphipathic (one polar head, two nonpolar tails) — perfect for membrane bilayer formation.",
  },
  {
    "id": "ch3-q-045", "section": "3.3", "difficulty": "medium",
    "question": "When phospholipids are placed in water, they spontaneously form a bilayer. The driving force is that:",
    "choices": [
      "all parts of the phospholipid are hydrophobic and naturally exclude water from the interior",
      "all parts of the phospholipid are hydrophilic and attracted to the surrounding water molecules",
      "the hydrophilic heads face the water while the hydrophobic tails turn inward — the lowest-energy arrangement",
      "phospholipids are pumped into a bilayer arrangement using energy from membrane-bound ATP synthase",
    ],
    "answerIndex": 2,
    "explanation": "Phospholipids self-assemble because burying the hydrophobic tails away from water while exposing the hydrophilic heads to water is the thermodynamically most favorable (lowest free energy) arrangement.",
  },
  {
    "id": "ch3-q-046", "section": "3.3", "difficulty": "medium",
    "question": "A transplant recipient's immune system attacks a donor organ because it detects unfamiliar molecules on the organ's cell surfaces. Which membrane protein type is responsible?",
    "choices": [
      "Transport proteins — they carry foreign molecules into the cell, triggering an intracellular immune response",
      "Recognition proteins — cell-surface glycoproteins that act as 'self' ID tags; mismatched markers trigger immune attack",
      "Enzyme proteins — donor cell enzymes catalyze reactions that produce antigens recognized as foreign",
      "Receptor proteins — they bind donor cytokines that signal the recipient's immune system to destroy the organ",
    ],
    "answerIndex": 1,
    "explanation": "Recognition proteins (glycoproteins) act as 'self' name tags. If a donor's markers don't match the recipient's, the immune system recognizes them as foreign and mounts an attack.",
  },
  {
    "id": "ch3-q-047", "section": "3.4", "difficulty": "medium",
    "question": "A liver cell must break down a toxic drug circulating in the blood. Which organelle is primarily responsible for this detoxification?",
    "choices": [
      "Rough ER — its ribosomes synthesize the detoxifying enzymes and immediately degrade drug molecules",
      "Smooth ER — it contains enzymes that oxidize and detoxify drugs, poisons, and other lipid-soluble compounds",
      "Nucleolus — it produces the ribosomal RNA required for synthesizing detoxifying enzymes faster than other organelles",
      "Lysosome — its acidic pH and hydrolytic enzymes break down any foreign molecule entering the cell",
    ],
    "answerIndex": 1,
    "explanation": "Smooth ER contains cytochrome P450 enzymes that oxidize lipid-soluble drugs and toxins, making them water-soluble for excretion. Liver cells are especially rich in smooth ER.",
  },
  {
    "id": "ch3-q-048", "section": "3.4", "difficulty": "medium",
    "question": "Heart muscle cells contain an unusually high number of mitochondria compared to other cell types. This tells you that heart cells:",
    "choices": [
      "store large amounts of fat droplets that the mitochondria slowly oxidize over many days",
      "have very high continuous energy (ATP) demands that require constant aerobic respiration",
      "perform photosynthesis using mitochondria as a substitute for chloroplasts",
      "rarely divide — extra mitochondria compensate for the lack of cell division by providing extra DNA",
    ],
    "answerIndex": 1,
    "explanation": "Mitochondria produce ATP via aerobic respiration. Cells with the highest and most continuous energy demands — like constantly contracting heart muscle — have the most mitochondria.",
  },
  # ch3-pe-020 converted from trueFalse
  {
    "id": "ch3-q-049", "section": "3.4", "difficulty": "medium",
    "question": "Which evidence best supports the endosymbiont theory — the idea that mitochondria and chloroplasts originated as free-living bacteria that were engulfed by a host cell?",
    "choices": [
      "Both organelles are found in all eukaryotic cells, including fungi and protozoa that never perform photosynthesis",
      "Both mitochondria and chloroplasts contain their own circular DNA and ribosomes, suggesting they were once independent prokaryotic cells",
      "Both organelles are bounded by a single phospholipid membrane, consistent with their origin as secretory vesicles",
      "Both organelles grow by budding off from the Golgi apparatus, just like lysosomes and secretory vesicles",
    ],
    "answerIndex": 1,
    "explanation": "Circular DNA and prokaryote-like ribosomes inside mitochondria and chloroplasts are the strongest structural evidence for endosymbiosis. Both organelles also divide by binary fission.",
  },
  {
    "id": "ch3-q-050", "section": "3.4", "difficulty": "medium",
    "question": "Which pair of processes are essentially the reverse of each other in terms of reactants and products?",
    "choices": [
      "Hydrolysis and digestion — both break polymers into monomers using water",
      "Cellular respiration and photosynthesis — one uses glucose + O2 to yield CO2 + H2O + energy; the other uses CO2 + H2O + energy to yield glucose + O2",
      "Diffusion and osmosis — both move molecules from high to low concentration across a membrane",
      "Translation and transcription — one reads DNA to make mRNA; the other reads mRNA to make protein",
    ],
    "answerIndex": 1,
    "explanation": "Respiration (glucose + O2 → CO2 + H2O + ATP) and photosynthesis (CO2 + H2O + light → glucose + O2) are metabolic opposites, linking energy release and energy storage.",
  },
  {
    "id": "ch3-q-051", "section": "3.5", "difficulty": "medium",
    "question": "Microfilaments are the thinnest cytoskeletal fibers. They are composed of:",
    "choices": [
      "tubulin dimers — the same protein that polymerizes to form microtubules and the mitotic spindle",
      "actin — a globular protein that polymerizes into long filaments involved in cell shape and movement",
      "myosin — the motor protein that works with the filaments during muscle contraction",
      "keratin — the intermediate filament protein that provides tensile strength in epithelial cells",
    ],
    "answerIndex": 1,
    "explanation": "Microfilaments are made of actin (F-actin). Myosin is a motor protein that walks along actin filaments — it forms the filament itself only in thick filaments, not actin-based microfilaments.",
  },
  {
    "id": "ch3-q-052", "section": "3.5", "difficulty": "medium",
    "question": "A chemotherapy drug disrupts microtubule polymerization. Why does this stop cancer cells from multiplying?",
    "choices": [
      "Disrupting microtubules prevents the cell wall from forming, trapping the cell in a permanently enlarged state",
      "Microtubules form the mitotic spindle that pulls duplicated chromosomes to opposite poles — without spindle fibers, chromosomes cannot separate and cell division halts",
      "Without microtubules, mitochondria cannot produce ATP, starving cancer cells of the energy needed to replicate DNA",
      "Microtubules carry genetic information to daughter cells — disrupting them prevents DNA from being distributed to new cells",
    ],
    "answerIndex": 1,
    "explanation": "The mitotic spindle is made of microtubules. If they cannot assemble, sister chromatids cannot be separated to opposite poles, so cell division arrests — the principle behind drugs like taxol and colchicine.",
  },
  {
    "id": "ch3-q-053", "section": "3.5", "difficulty": "hard",
    "question": "In animal cells, the microtubule-organizing center (MTOC) that contains two centrioles is the:",
    "choices": [
      "ribosome — the complex that organizes mRNA translation and anchors the cytoskeleton to the rough ER",
      "centrosome — the MTOC that nucleates microtubule growth and contains a pair of centrioles",
      "lysosome — the organelle that degrades old microtubule proteins and recycles the tubulin dimers",
      "basal body — a centriole-derived structure at the base of cilia; it is identical to a centrosome",
    ],
    "answerIndex": 1,
    "explanation": "Centrosomes organize microtubules in animal cells and contain two centrioles. Plant cells typically lack centrosomes yet still form a functional mitotic spindle. Centrioles template basal bodies.",
  },
  {
    "id": "ch3-q-054", "section": "3.5", "difficulty": "medium",
    "question": "The lining of the human respiratory tract is covered by short, numerous extensions that beat in coordinated waves to sweep mucus and trapped particles up and out. These extensions are:",
    "choices": [
      "flagella — long, few, whip-like structures that propel cells such as sperm through fluid",
      "cilia — short, numerous projections made of microtubules that move in rhythmic waves to sweep surfaces",
      "microvilli — short projections that increase surface area for absorption but do not move",
      "pili — bacterial surface projections used for adhesion and DNA transfer",
    ],
    "answerIndex": 1,
    "explanation": "Cilia are short (~2–20 µm), numerous, and beat in coordinated waves. Flagella are longer and fewer. Microvilli increase absorptive surface but do not beat.",
  },
  {
    "id": "ch3-q-055", "section": "3.6", "difficulty": "medium",
    "question": "The blood-brain barrier prevents most substances in the blood from entering the brain. It is formed by which type of cell junction?",
    "choices": [
      "Gap junctions — channels that allow ions and small molecules to pass directly between adjacent cells",
      "Anchoring junctions (desmosomes) — protein-link structures that mechanically attach neighboring cells together",
      "Tight junctions — protein strands that seal the space between adjacent endothelial cells, blocking paracellular flow",
      "Plasmodesmata — cytoplasmic channels through the cell wall that connect adjacent plant cells",
    ],
    "answerIndex": 2,
    "explanation": "Tight junctions fuse adjacent endothelial cell membranes, preventing substances from leaking between cells. This forces everything crossing the blood-brain barrier to pass through cells, enabling selective control.",
  },
  {
    "id": "ch3-q-056", "section": "3.6", "difficulty": "medium",
    "question": "Heart muscle cells must contract in a precisely coordinated rhythm. Which cell junction allows the electrical signal to spread rapidly from cell to cell?",
    "choices": [
      "Tight junctions — they seal cells together so the electrical signal cannot escape the cardiac muscle layer",
      "Anchoring junctions (desmosomes) — they physically connect the cytoskeletons of adjacent cells, transmitting the contraction force",
      "Gap junctions — protein channels that directly connect the cytoplasm of adjacent cells, allowing ions and electrical signals to pass",
      "Cell walls — the carbohydrate matrix between plant cells conducts electrical signals that synchronize tissue contraction",
    ],
    "answerIndex": 2,
    "explanation": "Gap junctions form protein channels (connexons) that directly connect adjacent cytoplasm, allowing ions (the electrical signal) to flow between cells and synchronize cardiac contraction.",
  },
  {
    "id": "ch3-q-057", "section": "3.6", "difficulty": "medium",
    "question": "Plasmodesmata in plant cells are functionally most similar to which junction in animal cells?",
    "choices": [
      "Tight junctions — both seal off the extracellular space to prevent unwanted molecular movement between cells",
      "Anchoring junctions — both provide mechanical links between adjacent cell membranes and cytoskeletons",
      "Gap junctions — both are channels that allow direct cytoplasmic communication between adjacent cells",
      "Desmosomes — both attach the cytoskeleton of one cell to the extracellular matrix of the neighboring cell",
    ],
    "answerIndex": 2,
    "explanation": "Plasmodesmata are channels through plant cell walls that allow cytoplasm, ions, and small molecules to pass between cells — functionally equivalent to the gap junction channels in animal cells.",
  },
  # ch3-pe-030 converted from trueFalse
  {
    "id": "ch3-q-058", "section": "3.6", "difficulty": "medium",
    "question": "Tight junctions between endothelial cells form the blood-brain barrier. Which type of molecule would still cross it quickly despite these tight junctions?",
    "choices": [
      "Water-soluble vitamins like vitamin C — tight junctions specifically transport polar vitamins into the brain",
      "Large protein antibodies — tight junctions block only small ions while allowing proteins to pass through size-selective pores",
      "Lipid-soluble molecules such as certain anesthetics, which dissolve through the cells' own lipid bilayer membranes",
      "Glucose and other polar sugars — aquaporin channels in the barrier cells bypass the tight junctions entirely for sugar transport",
    ],
    "answerIndex": 2,
    "explanation": "Although tight junctions block paracellular (between-cell) flow, lipid-soluble molecules can still cross by dissolving through the phospholipid bilayer of the endothelial cells themselves — that's why lipid-soluble anesthetics reach the brain rapidly.",
  },
]

# ══════════════════════════════════════════════════════════════════════════════
# Apply
# ══════════════════════════════════════════════════════════════════════════════

a1 = add("ch1", ch1_new)
a2 = add("ch2", ch2_new)
a3 = add("ch3", ch3_new)

print(f"ch1: +{a1} -> {len(ch('ch1')['quiz'])} questions")
print(f"ch2: +{a2} -> {len(ch('ch2')['quiz'])} questions")
print(f"ch3: +{a3} -> {len(ch('ch3')['quiz'])} questions")
print(f"Total added: {a1+a2+a3}")

out = json.dumps(data, indent=2, ensure_ascii=False)
SRC.write_text(out, encoding="utf-8")
ROOT.write_text(out, encoding="utf-8")
print("Saved.")
