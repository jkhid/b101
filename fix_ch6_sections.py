"""
Audit fix for Chapter 6 (Respiration and Fermentation):
1. Relabel sections to match the textbook's real 6.1-6.9 structure.
   Our content only had 6 sections grouped by biochemical stage
   (glycolysis/pyruvate-ox/Krebs/ETC/fermentation); the textbook has
   9 numbered sections, two of which were entirely missing from our
   content: 6.3 (mitochondrion structure) and 6.7 (other food
   molecules entering the pathways).
2. Add flashcards + quiz questions for gaps found versus the textbook:
   - 6.2 Three Main Processes: respiration framed as redox; why energy
     is released stepwise instead of all at once.
   - 6.3 Mitochondria (entirely missing): cristae, matrix, intermembrane
     compartment, prokaryote vs eukaryote enzyme locations, mtDNA/disease.
   - 6.6 ATP yield: the NADH shuttle cost (38->36 theoretical), why
     actual yield is lower (~30), and respiration poisons (arsenic,
     cyanide, CO, DNP, oligomycin) and where each acts.
   - 6.7 Other Food Molecules (entirely missing): how carbs/protein/fat
     enter the pathways, why fat has more Calories/gram.
   - 6.8 Anaerobic respiration as distinct from fermentation (we only
     had fermentation); the muscle-soreness myth.
   - 6.9 Endosymbiosis evidence and the ancient-pathway argument for
     glycolysis (we only had one question on this whole topic).
"""

import json, pathlib

SRC = pathlib.Path("src/data/content.json")
ROOT = pathlib.Path("content.json")

data = json.loads(SRC.read_text(encoding="utf-8"))
ch6 = next(c for c in data["chapters"] if c["id"] == "ch6")

# ── 1. Fix sections array to match the textbook ─────────────────────────────

ch6["sections"] = [
    {"id": "6.1", "title": "Cells Use Energy in Food to Make ATP"},
    {"id": "6.2", "title": "Cellular Respiration Includes Three Main Processes"},
    {"id": "6.3", "title": "In Eukaryotic Cells, Mitochondria Produce Most ATP"},
    {"id": "6.4", "title": "Glycolysis Breaks Down Glucose to Pyruvate"},
    {"id": "6.5", "title": "Aerobic Respiration Yields Abundant ATP"},
    {"id": "6.6", "title": "How Many ATPs Can One Glucose Molecule Yield?"},
    {"id": "6.7", "title": "Other Food Molecules Enter the Energy-Extracting Pathways"},
    {"id": "6.8", "title": "Some Energy Pathways Do Not Require Oxygen"},
    {"id": "6.9", "title": "Photosynthesis and Respiration Are Ancient Pathways"},
]

# ── 2. Remap existing flashcards by ID (old groupings don't nest cleanly) ───

FC_SECTION_REMAP = {
    "ch6-fc-001": "6.1",  # Overall equation for aerobic cellular respiration
    "ch6-fc-002": "6.1",  # Cellular respiration is catabolic and exergonic
    "ch6-fc-003": "6.4",  # Glycolysis - location and overview
    "ch6-fc-004": "6.4",  # Net products of glycolysis per glucose
    "ch6-fc-005": "6.5",  # Pyruvate oxidation (pyruvate decarboxylation)
    "ch6-fc-006": "6.5",  # Krebs cycle - location and overview
    "ch6-fc-007": "6.5",  # Krebs cycle products per glucose (2 turns)
    "ch6-fc-008": "6.5",  # Electron transport chain (ETC) - location
    "ch6-fc-009": "6.5",  # Chemiosmosis and ATP synthase
    "ch6-fc-010": "6.5",  # Why is oxygen the final electron acceptor?
    "ch6-fc-011": "6.6",  # Total ATP yield from aerobic respiration
    "ch6-fc-012": "6.5",  # Where is CO2 released during aerobic respiration?
    "ch6-fc-013": "6.8",  # Fermentation - purpose and key feature
    "ch6-fc-014": "6.8",  # Lactic acid fermentation
    "ch6-fc-015": "6.8",  # Alcoholic (ethanol) fermentation
    "ch6-fc-016": "6.8",  # Aerobic respiration vs. fermentation - ATP comparison
    "ch6-fc-017": "6.5",  # Role of NADH and FADH2 in aerobic respiration
    "ch6-fc-018": "6.2",  # Stages of aerobic respiration and their locations (roadmap/overview)
    "ch6-fc-019": "6.4",  # Why glycolysis is universal
    "ch6-fc-020": "6.9",  # Comparing inner mito membrane to thylakoid membrane
}
for f in ch6["flashcards"]:
    f["section"] = FC_SECTION_REMAP[f["id"]]

# ── 3. Remap existing quiz questions by ID ───────────────────────────────────

QUIZ_SECTION_REMAP = {
    "ch6-q-001": "6.4",  # In which part of the cell does glycolysis occur?
    "ch6-q-002": "6.4",  # Net ATP gain from glycolysis
    "ch6-q-003": "6.4",  # Which statement about glycolysis is correct?
    "ch6-q-004": "6.5",  # Final electron acceptor of the ETC
    "ch6-q-005": "6.5",  # Where does the Krebs cycle occur?
    "ch6-q-006": "6.5",  # Per-turn Krebs cycle products
    "ch6-q-007": "6.5",  # What drives ATP synthase?
    "ch6-q-008": "6.8",  # Primary purpose of fermentation
    "ch6-q-009": "6.8",  # Lactic acid fermentation products
    "ch6-q-010": "6.8",  # Bread rising / alcoholic fermentation gas
    "ch6-q-011": "6.6",  # Aerobic respiration vs fermentation ATP comparison (yield accounting)
    "ch6-q-012": "6.5",  # O2 removed -> ETC stops
    "ch6-q-013": "6.5",  # Total CO2 released per glucose
    "ch6-q-014": "6.8",  # Sprint / muscle cells / fermentation burning feeling
    "ch6-q-015": "6.3",  # Which location produces the MOST ATP (mitochondrion)
    "ch6-q-016": "6.4",  # Which stage occurs in absence of O2 (glycolysis)
    "ch6-q-017": "6.5",  # What enters the Krebs cycle (acetyl-CoA)
    "ch6-q-018": "6.2",  # How electrons are removed and delivered to ETC (redox framing)
    "ch6-q-019": "6.5",  # Inner membrane impermeability to H+ / chemiosmosis
    "ch6-q-020": "6.8",  # Alcoholic vs lactic acid fermentation CO2
    "ch6-q-021": "6.4",  # Substrate-level vs oxidative phosphorylation
    "ch6-q-022": "6.6",  # Respiration vs combustion efficiency
    "ch6-q-023": "6.5",  # Where do all 6 carbons end up (CO2)
    "ch6-q-024": "6.8",  # Intense exercise / lactic acid fermentation despite O2 present
    "ch6-q-025": "6.9",  # Respiration as reverse of photosynthesis
}
for q in ch6["quiz"]:
    q["section"] = QUIZ_SECTION_REMAP[q["id"]]

# ── 4. New flashcards ────────────────────────────────────────────────────────

new_flashcards = [
    # 6.2 — Three Main Processes (overview / redox framing)
    {
        "id": "ch6-fc-021", "section": "6.2", "difficulty": "medium",
        "front": "Cellular respiration as a redox process",
        "back": "Respiration oxidizes glucose (removes electrons) and reduces O2 (adds electrons to it). Because O2 has a strong attraction for electrons, this electron transfer is energetically 'downhill' (like coasting on a bike) and releases energy that the cell captures as ATP.",
    },
    {
        "id": "ch6-fc-022", "section": "6.2", "difficulty": "easy",
        "front": "Why respiration releases energy in many small steps",
        "back": "If a cell released all of glucose's potential energy in one uncontrolled step, the sudden heat would destroy the cell (like a tiny bomb). Instead, enzymes rearrange glucose's bonds one step at a time across glycolysis, the Krebs cycle, and the electron transport chain — releasing a small amount of energy with each transformation.",
    },
    # 6.3 — Mitochondria (entirely new section)
    {
        "id": "ch6-fc-023", "section": "6.3", "difficulty": "medium",
        "front": "Mitochondrion structure",
        "back": "Bounded by two membranes: a smooth OUTER membrane and a highly folded INNER membrane. Cristae = folds of the inner membrane (huge surface area for the ETC). Intermembrane compartment = space between the two membranes. Matrix = fluid inside the inner membrane, where the Krebs cycle occurs.",
    },
    {
        "id": "ch6-fc-024", "section": "6.3", "difficulty": "hard",
        "front": "Where respiration enzymes are located: prokaryotes vs. eukaryotes",
        "back": "Bacteria and archaea lack mitochondria: their Krebs cycle enzymes are in the cytosol, and their electron transport proteins are embedded in the cell membrane. Eukaryotic cells (protists, plants, fungi, animals) have mitochondria that house the Krebs cycle (matrix) and ETC (inner membrane/cristae).",
    },
    {
        "id": "ch6-fc-025", "section": "6.3", "difficulty": "medium",
        "front": "Mitochondrial DNA and disease",
        "back": "Mitochondria contain their own DNA and ribosomes, which encode ATP synthase and most ETC proteins. Mitochondrial diseases especially harm energy-hungry muscle and nerve cells — each may contain up to 10,000 mitochondria, so defective mitochondrial genes can be devastating.",
    },
    # 6.6 — ATP yield accounting + poisons
    {
        "id": "ch6-fc-026", "section": "6.6", "difficulty": "hard",
        "front": "Theoretical (38) vs. commonly cited (36) ATP yield: the NADH shuttle cost",
        "back": "Adding up all ATP from substrate-level phosphorylation + oxidative phosphorylation gives a theoretical max of 38 ATP/glucose. But NADH made in glycolysis (cytosol) must be shuttled into the mitochondrion, often costing ~1 ATP per NADH — dropping the commonly cited theoretical yield to 36. Actual yield (~30) is lower still due to H+ leak and the cost of transporting pyruvate/ADP into the matrix.",
    },
    {
        "id": "ch6-fc-027", "section": "6.6", "difficulty": "hard",
        "front": "Respiration poisons and where they act",
        "back": "Arsenic: blocks acetyl-CoA formation (Krebs cycle entry). Mercury, cyanide, carbon monoxide: block the electron transport chain (cyanide & CO block the same step — final electron transfer to O2). DNP: makes the inner membrane leaky to H+, collapsing the proton gradient. Oligomycin: directly blocks ATP synthase's proton channel.",
    },
    {
        "id": "ch6-fc-028", "section": "6.6", "difficulty": "medium",
        "front": "Respiration efficiency vs. combustion",
        "back": "Burning glucose in a flame and aerobic respiration release the same total energy (~686 kcal/mol). Respiration releases it gradually in small enzyme-controlled steps, capturing roughly 32% as usable ATP. Combustion releases it all at once as heat — useless for doing cellular work.",
    },
    # 6.7 — Other Food Molecules (entirely new section)
    {
        "id": "ch6-fc-029", "section": "6.7", "difficulty": "medium",
        "front": "How carbohydrates, proteins, and fats enter respiration",
        "back": "Starch/glycogen: digested to glucose -> glycolysis. Proteins: digested to amino acids; nitrogen is stripped and excreted (e.g., as urea), and the remaining carbon skeleton enters as pyruvate, acetyl-CoA, or a Krebs cycle intermediate (depends on the amino acid). Fats: split into glycerol (-> converted to pyruvate) and fatty acids (cut into 2-carbon pieces -> acetyl-CoA).",
    },
    {
        "id": "ch6-fc-030", "section": "6.7", "difficulty": "easy",
        "front": "Why fat has more Calories per gram",
        "back": "A single fat molecule's fatty acid chains can be cut into dozens of 2-carbon acetyl-CoA groups for the Krebs cycle — far more than other food molecules yield per gram. The body can also store excess Calories from carbs OR fat by diverting acetyl-CoA away from the Krebs cycle to build new fat molecules for storage.",
    },
    # 6.8 — Anaerobic respiration distinct from fermentation
    {
        "id": "ch6-fc-031", "section": "6.8", "difficulty": "hard",
        "front": "Anaerobic respiration (distinct from fermentation)",
        "back": "Like aerobic respiration, but the final electron acceptor at the end of the ETC is something OTHER than O2 (e.g., nitrate NO3-, sulfate SO4(2-), or CO2). Still uses an electron transport chain, so it yields more ATP than fermentation — but less than aerobic respiration. Performed by bacteria/archaea: denitrifiers -> N2 gas, sulfate reducers -> H2S, methanogens -> CH4.",
    },
    {
        "id": "ch6-fc-032", "section": "6.8", "difficulty": "medium",
        "front": "Fermentation vs. anaerobic respiration — the key distinction",
        "back": "Fermentation: NADH donates its electrons directly to pyruvate (NO electron transport chain involved at all); ATP comes only from glycolysis. Anaerobic respiration: NADH still donates electrons to an ETC — just with a non-O2 final acceptor — so it generates extra ATP via chemiosmosis beyond glycolysis's 2 ATP.",
    },
    {
        "id": "ch6-fc-033", "section": "6.8", "difficulty": "easy",
        "front": "Muscle soreness myth",
        "back": "The immediate burning feeling during intense exercise is associated with fermentation. But the DELAYED soreness felt a day or two later is NOT caused by lactic acid — lactate doesn't significantly drop muscle pH, and it's cleared from cells within hours of the workout. Delayed soreness is now attributed to microscopic tears in muscle tissue.",
    },
    # 6.9 — Endosymbiosis / ancient pathways
    {
        "id": "ch6-fc-034", "section": "6.9", "difficulty": "medium",
        "front": "Endosymbiosis explains mitochondrial structure",
        "back": "The double membrane of mitochondria (and chloroplasts) reflects their origin: an ancestral host cell engulfed a free-living bacterium. The bacterium's own cell membrane became the organelle's INNER membrane; the host's engulfing vesicle membrane became the OUTER membrane. This is why ETC proteins sit in the mitochondrion's inner membrane — homologous to a free-living bacterium's single cell membrane.",
    },
    {
        "id": "ch6-fc-035", "section": "6.9", "difficulty": "easy",
        "front": "Evidence for endosymbiosis",
        "back": "Both mitochondria and chloroplasts have their own DNA and ribosomes (separate from the nucleus) and are bounded by a double membrane — strong evidence they were once free-living bacteria engulfed by an ancestral host cell.",
    },
    {
        "id": "ch6-fc-036", "section": "6.9", "difficulty": "medium",
        "front": "Glycolysis is the most ancient energy pathway",
        "back": "Glycolysis occurs in virtually all living cells (even those lacking mitochondria) and requires no O2 — consistent with evolving when Earth's atmosphere lacked oxygen. Photosynthesis may have evolved partly from glycolysis (Calvin cycle reactions partly mirror reversed glycolysis steps). Oxygen-generating photosynthesis (cyanobacteria) arose ~3.5 billion years ago, eventually making aerobic respiration possible.",
    },
]
ch6["flashcards"].extend(new_flashcards)

# ── 5. New quiz questions ────────────────────────────────────────────────────

new_quiz = [
    # 6.2
    {
        "id": "ch6-q-026", "section": "6.2", "difficulty": "easy",
        "question": "Why does cellular respiration release energy from glucose in many small steps rather than all at once?",
        "choices": [
            "A single uncontrolled release of glucose's potential energy would generate a destructive burst of heat; gradual release lets the cell capture energy as ATP",
            "Enzymes can only process one carbon atom at a time, so the six carbons of glucose must be handled sequentially",
            "Glycolysis, the Krebs cycle, and the ETC physically cannot occur in the same organelle simultaneously",
            "Releasing energy all at once would produce only CO2 and no ATP at all",
        ],
        "answerIndex": 0,
        "explanation": "If a cell released all of glucose's potential energy in one step, the heat released would destroy the cell — like a tiny bomb. Breaking the process into many small enzyme-catalyzed steps lets the cell capture much of that energy as ATP instead of losing it all as heat at once.",
    },
    {
        "id": "ch6-q-027", "section": "6.2", "difficulty": "medium",
        "question": "Why is the electron transfer from glucose to O2 during aerobic respiration energetically favorable ('downhill')?",
        "choices": [
            "Glucose has a stronger attraction for electrons than oxygen does, pulling electrons away from the ETC",
            "Oxygen has a strong attraction for electrons, so transferring electrons to it releases energy, similar to coasting downhill",
            "ATP synthase actively pulls electrons toward oxygen, using energy from ATP hydrolysis",
            "Electrons move toward O2 only because of a concentration gradient, not because of any difference in electron affinity",
        ],
        "answerIndex": 1,
        "explanation": "Oxygen's strong electron affinity makes it an excellent final electron acceptor. Moving electrons from glucose (which holds them loosely) to O2 (which holds them tightly) is exergonic — releasing energy the cell traps in ATP, much like riding a bike downhill.",
    },
    # 6.3
    {
        "id": "ch6-q-028", "section": "6.3", "difficulty": "easy",
        "question": "Which mitochondrial structure provides the large surface area needed for the electron transport chain?",
        "choices": ["The matrix", "Cristae (folds of the inner membrane)", "The outer membrane", "The intermembrane compartment"],
        "answerIndex": 1,
        "explanation": "Cristae are folds of the inner mitochondrial membrane that dramatically increase its surface area, providing room for the many electron transport chain proteins and ATP synthase complexes embedded there.",
    },
    {
        "id": "ch6-q-029", "section": "6.3", "difficulty": "hard",
        "question": "How do bacteria and archaea (which lack mitochondria) carry out the Krebs cycle and electron transport?",
        "choices": [
            "They cannot perform these processes at all and rely entirely on fermentation",
            "Krebs cycle enzymes are in the cytosol, and electron transport proteins are embedded in the cell membrane",
            "They use specialized vesicles called proto-mitochondria that mimic eukaryotic organelles",
            "Both processes occur exclusively in the cell wall, outside the plasma membrane",
        ],
        "answerIndex": 1,
        "explanation": "Without mitochondria, prokaryotes house the Krebs cycle enzymes in the cytosol and embed electron transport proteins directly in the cell (plasma) membrane — the same membrane that mitochondria's inner membrane is thought to be derived from via endosymbiosis.",
    },
    {
        "id": "ch6-q-030", "section": "6.3", "difficulty": "medium",
        "question": "Why are muscle and nerve cells especially vulnerable to mitochondrial diseases?",
        "choices": [
            "They contain no mitochondria of their own and rely entirely on neighboring cells for ATP",
            "They are highly energy-demanding and may contain as many as 10,000 mitochondria each",
            "Their mitochondria lack DNA, making them unable to repair genetic damage",
            "They exclusively use anaerobic respiration, which is more sensitive to mitochondrial defects",
        ],
        "answerIndex": 1,
        "explanation": "Muscle and nerve cells have enormous energy demands and may contain up to 10,000 mitochondria each. When mitochondrial genes (which encode ATP synthase and most ETC proteins) are defective, these energy-hungry cells are hit hardest.",
    },
    {
        "id": "ch6-q-031", "section": "6.3", "difficulty": "medium", "type": "selectAll",
        "question": "Which of the following are true of mitochondria? (Select all that apply.)",
        "choices": [
            "They contain their own DNA",
            "They contain ribosomes",
            "They are bounded by two membranes",
            "The matrix is the site of the Krebs cycle",
            "Electron transport chain proteins are located in the outer membrane",
        ],
        "answerIndices": [0, 1, 2, 3],
        "explanation": "Mitochondria have their own DNA and ribosomes (evidence of endosymbiotic origin), a double membrane (outer + inner), and the Krebs cycle occurs in the matrix. The ETC is embedded in the INNER membrane (specifically the cristae), not the outer membrane.",
    },
    # 6.6
    {
        "id": "ch6-q-032", "section": "6.6", "difficulty": "hard",
        "question": "Why is the theoretical maximum ATP yield (38) higher than the commonly cited theoretical yield of 36 ATP per glucose?",
        "choices": [
            "Two ATP are always lost to heat during the transition step, regardless of conditions",
            "Shuttling NADH made during glycolysis (in the cytosol) into the mitochondrion typically costs about 1 ATP per NADH",
            "Oxygen consumption during the ETC directly consumes 2 ATP per glucose molecule",
            "The Krebs cycle only runs once per glucose instead of twice in most human cells",
        ],
        "answerIndex": 1,
        "explanation": "Adding up all ATP from substrate-level and oxidative phosphorylation gives 38 ATP/glucose theoretically. But NADH produced in the cytosol during glycolysis must be shuttled into the mitochondrion, which often costs about 1 ATP per NADH — bringing the commonly cited theoretical max down to 36.",
    },
    {
        "id": "ch6-q-033", "section": "6.6", "difficulty": "medium", "type": "selectAll",
        "question": "Which of the following help explain why the ACTUAL ATP yield of aerobic respiration (~30) is lower than the theoretical yield (~36)? (Select all that apply.)",
        "choices": [
            "Some protons leak across the inner mitochondrial membrane without passing through ATP synthase",
            "The cell spends energy transporting pyruvate and ADP into the mitochondrial matrix",
            "Oxygen must be present as the final electron acceptor",
            "CO2 must be released as a waste product at multiple steps",
        ],
        "answerIndices": [0, 1],
        "explanation": "Proton leak across the inner membrane wastes some of the gradient without generating ATP, and transporting pyruvate/ADP into the matrix costs energy — both lower the actual yield below the theoretical maximum. Needing O2 and releasing CO2 are normal, necessary parts of the pathway, not energy losses.",
    },
    {
        "id": "ch6-q-034", "section": "6.6", "difficulty": "medium",
        "question": "Cyanide and carbon monoxide are both deadly poisons because they:",
        "choices": [
            "Block the same step of the electron transport chain — the final transfer of electrons to O2",
            "Both directly inhibit ATP synthase's proton channel, identical to oligomycin's mechanism",
            "Compete with glucose for the active site of hexokinase, blocking glycolysis entirely",
            "Bind to oxaloacetate, preventing the Krebs cycle from regenerating its starting molecule",
        ],
        "answerIndex": 0,
        "explanation": "Cyanide and carbon monoxide both block the final transfer of electrons to O2 at the end of the electron transport chain. With nowhere to 'dump' their electrons, the ETC grinds to a halt and ATP production via chemiosmosis ceases.",
    },
    {
        "id": "ch6-q-035", "section": "6.6", "difficulty": "medium",
        "question": "Arsenic is toxic to cellular respiration primarily because it:",
        "choices": [
            "Blocks formation of acetyl-CoA, preventing pyruvate from entering the Krebs cycle",
            "Directly competes with O2 for binding to the final ETC protein complex",
            "Makes the inner mitochondrial membrane permeable to protons",
            "Prevents glucose from being phosphorylated during the first step of glycolysis",
        ],
        "answerIndex": 0,
        "explanation": "Arsenic binds to a molecule needed to form acetyl-CoA, blocking the transition step that feeds pyruvate's carbon skeleton into the Krebs cycle — stopping that stage of respiration.",
    },
    {
        "id": "ch6-q-036", "section": "6.6", "difficulty": "hard",
        "question": "The poison 2,4-dinitrophenol (DNP) disrupts ATP production by:",
        "choices": [
            "Directly blocking the proton channel within ATP synthase",
            "Making the inner mitochondrial membrane permeable to H+, so the proton gradient never builds up",
            "Binding to NADH so it cannot deliver electrons to the first ETC protein",
            "Preventing pyruvate from crossing into the mitochondrial matrix",
        ],
        "answerIndex": 1,
        "explanation": "DNP makes the inner mitochondrial membrane leaky to protons. H+ ions leak back into the matrix without passing through ATP synthase, destroying the gradient needed to drive ATP production — unlike oligomycin, which blocks ATP synthase's channel directly.",
    },
    # 6.7
    {
        "id": "ch6-q-037", "section": "6.7", "difficulty": "easy",
        "question": "A digested fatty acid most directly enters the energy-extracting pathways as:",
        "choices": ["Glucose", "Pyruvate", "Acetyl-CoA", "Lactate"],
        "answerIndex": 2,
        "explanation": "Fatty acids are cut into many two-carbon pieces inside the mitochondria, and each piece becomes acetyl-CoA, which then proceeds through the Krebs cycle exactly as it would if it had come from glucose.",
    },
    {
        "id": "ch6-q-038", "section": "6.7", "difficulty": "medium",
        "question": "When a cell breaks down amino acids to generate ATP, what happens to the nitrogen atoms?",
        "choices": [
            "They are incorporated directly into ATP's adenine base",
            "They are stripped from the amino acid and excreted, often as urea, while the remaining carbon skeleton enters the energy pathways",
            "They combine with CO2 to form additional acetyl-CoA molecules",
            "They are stored permanently in the mitochondrial matrix as a nitrogen reserve",
        ],
        "answerIndex": 1,
        "explanation": "Before an amino acid's carbon skeleton can enter the energy pathways (as pyruvate, acetyl-CoA, or a Krebs cycle intermediate, depending on the amino acid), nitrogen must first be stripped off and excreted — typically as urea.",
    },
    {
        "id": "ch6-q-039", "section": "6.7", "difficulty": "medium", "type": "selectAll",
        "question": "Which of the following correctly pair a digested food molecule with its entry point into the energy-extracting pathways? (Select all that apply.)",
        "choices": [
            "Glycerol (from fat) enters as pyruvate",
            "Fatty acids enter as acetyl-CoA",
            "Glucose (from starch/glycogen) enters glycolysis",
            "Every amino acid enters exclusively as glucose, regardless of its structure",
        ],
        "answerIndices": [0, 1, 2],
        "explanation": "Glycerol is converted to pyruvate; fatty acids are cut into acetyl-CoA units; glucose from digested starch/glycogen enters glycolysis directly. Amino acids do NOT all enter as glucose — depending on which amino acid, they enter as pyruvate, acetyl-CoA, or a Krebs cycle intermediate.",
    },
    {
        "id": "ch6-q-040", "section": "6.7", "difficulty": "easy",
        "question": "Why do fats contain more Calories per gram than carbohydrates?",
        "choices": [
            "A single fat molecule's fatty acid chains can be cut into dozens of acetyl-CoA units, far more than a comparable carbohydrate yields",
            "Fat molecules contain nitrogen atoms that carbohydrates lack, adding extra potential energy",
            "Fats are digested directly into ATP without passing through the Krebs cycle",
            "Carbohydrates must be converted to fat before they can release any energy at all",
        ],
        "answerIndex": 0,
        "explanation": "A fat molecule's long fatty acid chains can be broken into many two-carbon acetyl-CoA units — far more energy-yielding fragments per gram than carbohydrates provide, which is why fat is calorically denser.",
    },
    # 6.8
    {
        "id": "ch6-q-041", "section": "6.8", "difficulty": "medium",
        "question": "How does anaerobic respiration differ from fermentation?",
        "choices": [
            "Anaerobic respiration still uses an electron transport chain (with a non-O2 final acceptor); fermentation uses no ETC at all",
            "Fermentation requires mitochondria, while anaerobic respiration occurs only in the cytosol",
            "Anaerobic respiration produces less ATP than fermentation because it skips glycolysis entirely",
            "There is no meaningful difference — the two terms describe the same biochemical process",
        ],
        "answerIndex": 0,
        "explanation": "Anaerobic respiration still routes electrons through an electron transport chain — just with an acceptor other than O2 (like nitrate or sulfate) — so it still generates some ATP via chemiosmosis. Fermentation skips the ETC entirely: NADH donates its electrons directly to pyruvate.",
    },
    {
        "id": "ch6-q-042", "section": "6.8", "difficulty": "easy",
        "question": "Which of these can serve as an alternative electron acceptor in anaerobic respiration?",
        "choices": ["Glucose", "Nitrate (NO3-)", "ATP", "Pyruvate"],
        "answerIndex": 1,
        "explanation": "In anaerobic respiration, inorganic molecules such as nitrate (NO3-), sulfate (SO4^2-), or CO2 substitute for O2 as the final electron acceptor at the end of the electron transport chain.",
    },
    {
        "id": "ch6-q-043", "section": "6.8", "difficulty": "hard",
        "question": "Why does anaerobic respiration generally yield more ATP per glucose than fermentation, even though both occur without O2?",
        "choices": [
            "Anaerobic respiration runs glycolysis twice per glucose molecule, doubling the initial ATP yield",
            "Anaerobic respiration still uses an electron transport chain and chemiosmosis to generate additional ATP beyond glycolysis",
            "Fermentation does not produce any pyruvate, so it cannot proceed past the first step of glycolysis",
            "Anaerobic respiration uses oxygen stored within the cell instead of the environment",
        ],
        "answerIndex": 1,
        "explanation": "Because anaerobic respiration still routes electrons through an ETC (just to a non-O2 acceptor), it produces additional ATP via chemiosmosis on top of glycolysis's 2 ATP. Fermentation skips the ETC, so it is limited to whatever ATP glycolysis alone produces.",
    },
    {
        "id": "ch6-q-044", "section": "6.8", "difficulty": "medium",
        "question": "The delayed muscle soreness felt a day or two after intense exercise is now believed to be caused mainly by:",
        "choices": [
            "A sustained drop in muscle pH from accumulated lactic acid",
            "Microscopic tears in muscle tissue, not a drop in pH from lactate",
            "Leftover ethanol produced during muscle fermentation",
            "Excess CO2 trapped in muscle fibers from the Krebs cycle",
        ],
        "answerIndex": 1,
        "explanation": "Muscle cells produce lactate (not lactic acid), which doesn't substantially change cytoplasmic pH, and lactate is cleared from cells within hours of a workout — too quickly to explain soreness a day or two later. That delayed soreness is now attributed to microscopic tears in muscle tissue.",
    },
    # 6.9
    {
        "id": "ch6-q-045", "section": "6.9", "difficulty": "medium",
        "question": "What evidence supports the theory that mitochondria evolved from free-living bacteria engulfed by a host cell (endosymbiosis)?",
        "choices": [
            "Mitochondria have their own DNA and ribosomes and are bounded by a double membrane",
            "Mitochondria can be observed dividing independently outside of any cell in laboratory cultures",
            "Mitochondrial proteins are identical in sequence to human nuclear genome proteins",
            "Mitochondria lack any genetic material, proving they were never independent organisms",
        ],
        "answerIndex": 0,
        "explanation": "Mitochondria having their own DNA and ribosomes, separate from the cell's nucleus, plus a double membrane (consistent with one membrane from the original bacterium and one from the host's engulfing vesicle), are the key lines of evidence for endosymbiosis.",
    },
    {
        "id": "ch6-q-046", "section": "6.9", "difficulty": "hard",
        "question": "According to endosymbiosis theory, the mitochondrion's INNER membrane is thought to be derived from:",
        "choices": [
            "The host cell's plasma membrane, which wrapped around the engulfed bacterium",
            "The plasma membrane of the engulfed bacterium itself",
            "The nuclear envelope of the ancestral host cell",
            "A newly synthesized membrane formed after the engulfment event, unrelated to either original cell",
        ],
        "answerIndex": 1,
        "explanation": "The engulfed bacterium's own plasma membrane is thought to have become the mitochondrion's inner membrane, while the host cell's engulfing vesicle membrane became the outer membrane. This explains why ETC proteins sit in the inner membrane — homologous to a free-living bacterium's single cell membrane.",
    },
    {
        "id": "ch6-q-047", "section": "6.9", "difficulty": "medium",
        "question": "Why is glycolysis considered the most ancient of the energy-extracting pathways?",
        "choices": [
            "It occurs in virtually all living cells and requires no O2, consistent with evolving before Earth's atmosphere contained oxygen",
            "It is the only pathway that can be performed inside a mitochondrion",
            "Fossil evidence shows glycolysis enzymes predate the origin of DNA itself",
            "It produces the most ATP per glucose of any energy pathway, making it evolutionarily favored",
        ],
        "answerIndex": 0,
        "explanation": "Glycolysis occurs in virtually all cells, including those without mitochondria, and needs no oxygen — fitting with an origin before Earth's atmosphere accumulated O2. Photosynthesis (and aerobic respiration) likely arose later.",
    },
    {
        "id": "ch6-q-048", "section": "6.9", "difficulty": "medium", "type": "selectAll",
        "question": "Which of the following support the endosymbiotic origin of mitochondria? (Select all that apply.)",
        "choices": [
            "Mitochondria contain their own circular DNA",
            "Mitochondria contain ribosomes",
            "Mitochondria are bounded by two membranes",
            "Mitochondria can survive and replicate indefinitely outside of any host cell",
        ],
        "answerIndices": [0, 1, 2],
        "explanation": "Mitochondria having their own DNA, ribosomes, and a double membrane are the classic lines of evidence for endosymbiosis. Mitochondria cannot survive indefinitely outside a host cell — they remain dependent organelles, not free-living organisms.",
    },
]
ch6["quiz"].extend(new_quiz)

# ── Save ──────────────────────────────────────────────────────────────────────

out = json.dumps(data, indent=2, ensure_ascii=False)
SRC.write_text(out, encoding="utf-8")
ROOT.write_text(out, encoding="utf-8")

print(f"ch6 flashcards: {len(ch6['flashcards'])} (+{len(new_flashcards)})")
print(f"ch6 quiz: {len(ch6['quiz'])} (+{len(new_quiz)})")
sa_count = sum(1 for q in ch6['quiz'] if q.get('type') == 'selectAll')
print(f"ch6 selectAll questions: {sa_count}")
