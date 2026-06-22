"""Adds dedicated Ch 3 flashcards for mitochondria, chloroplast, lysosome, and peroxisome."""

import json, pathlib

SRC  = pathlib.Path("src/data/content.json")
ROOT = pathlib.Path("content.json")

data = json.loads(SRC.read_text(encoding="utf-8"))
ch3  = next(c for c in data["chapters"] if c["id"] == "ch3")

existing_fc = {f["id"] for f in ch3["flashcards"]}
existing_q  = {q["id"] for q in ch3["quiz"]}

new_fc = [
  {
    "id": "ch3-fc-023", "section": "3.4", "difficulty": "medium",
    "front": "Mitochondria structure",
    "back": (
      "DOUBLE membrane organelle — site of aerobic respiration. "
      "Outer membrane: smooth, permeable to small molecules. "
      "Inner membrane: highly folded into CRISTAE (increases surface area for ETC/ATP synthase). "
      "MATRIX: fluid inside the inner membrane — location of the Krebs cycle, "
      "contains its own circular DNA and ribosomes (evidence of endosymbiosis)."
    )
  },
  {
    "id": "ch3-fc-024", "section": "3.4", "difficulty": "medium",
    "front": "Chloroplast structure",
    "back": (
      "DOUBLE membrane organelle — site of photosynthesis. Found only in plant/algal cells. "
      "THYLAKOIDS: flattened membrane sacs stacked into GRANA; contain chlorophyll and the light-reaction machinery. "
      "STROMA: fluid surrounding the thylakoids — location of the Calvin cycle. "
      "Contains its own circular DNA and ribosomes (evidence of endosymbiosis)."
    )
  },
  {
    "id": "ch3-fc-025", "section": "3.4", "difficulty": "easy",
    "front": "Lysosomes — structure and function",
    "back": (
      "Membrane-bound vesicles containing ~50 hydrolytic enzymes (proteases, lipases, nucleases) "
      "that work best at pH ~5 (acidic). Functions: "
      "(1) Digest food particles and bacteria after phagocytosis. "
      "(2) Autophagy — break down old/damaged organelles for recycling. "
      "(3) Programmed cell death (apoptosis). "
      "Found mainly in ANIMAL cells. The membrane protects the rest of the cell from the enzymes inside."
    )
  },
  {
    "id": "ch3-fc-026", "section": "3.4", "difficulty": "easy",
    "front": "Peroxisomes — structure and function",
    "back": (
      "Small, single-membrane vesicles containing oxidative enzymes. Key functions: "
      "(1) Detoxify hydrogen peroxide: 2 H2O2 -> 2 H2O + O2 (using catalase). "
      "(2) Oxidize fatty acids (beta-oxidation) — products fed to mitochondria. "
      "(3) Detoxify alcohol and other harmful compounds (especially in liver cells). "
      "Unlike lysosomes, peroxisomes are found in BOTH plant and animal cells."
    )
  },
]

new_q = [
  {
    "id": "ch3-q-033", "section": "3.4", "difficulty": "medium",
    "question": "The inner mitochondrial membrane is highly folded into cristae. What is the purpose of this folding?",
    "choices": [
      "To store DNA and ribosomes used for mitochondrial protein synthesis",
      "To greatly increase surface area, fitting more electron transport chain complexes and ATP synthase to maximize ATP production",
      "To separate the Krebs cycle enzymes from the cytoplasm of the cell",
      "To allow the mitochondria to divide by binary fission"
    ],
    "answerIndex": 1,
    "explanation": "Cristae dramatically amplify the inner membrane surface area. More membrane = more ETC protein complexes and ATP synthase molecules = more ATP per mitochondrion. Cells with high energy demands (heart muscle, liver) have denser, more elaborate cristae."
  },
  {
    "id": "ch3-q-034", "section": "3.4", "difficulty": "medium",
    "question": "In a chloroplast, where do the light reactions occur and where does the Calvin cycle occur?",
    "choices": [
      "Light reactions in the stroma; Calvin cycle in the thylakoid lumen",
      "Both stages occur in the stroma",
      "Light reactions in/on the thylakoid membranes; Calvin cycle in the stroma",
      "Light reactions in the outer membrane; Calvin cycle in the inner membrane"
    ],
    "answerIndex": 2,
    "explanation": "The thylakoid membranes house the photosystems and ETC for the light reactions (capturing light energy to make ATP and NADPH). The stroma surrounds the thylakoids and contains the Calvin cycle enzymes (including RuBisCO) that use that ATP and NADPH to fix CO2 into G3P."
  },
  {
    "id": "ch3-q-035", "section": "3.4", "difficulty": "medium",
    "question": "Lysosomes are sometimes called the cell's 'recycling center.' Which best explains this role?",
    "choices": [
      "They convert ADP back to ATP using hydrolytic enzymes",
      "They contain digestive enzymes that break down damaged organelles (autophagy), food particles, and foreign material, recycling the components for reuse",
      "They store excess glucose as glycogen for later energy use",
      "They repackage misfolded proteins sent back from the Golgi apparatus"
    ],
    "answerIndex": 1,
    "explanation": "Lysosomes fuse with vesicles containing material to be broken down. Their ~50 hydrolytic enzymes (active at pH ~5) digest macromolecules into monomers (amino acids, sugars, nucleotides, fatty acids) that are exported back to the cytoplasm for reuse. Lysosomal storage diseases result from missing enzymes."
  },
  {
    "id": "ch3-q-036", "section": "3.4", "difficulty": "easy",
    "question": "A cell biologist finds that removing peroxisomes from liver cells causes toxic levels of hydrogen peroxide to accumulate. This demonstrates that peroxisomes normally:",
    "choices": [
      "Produce hydrogen peroxide as an energy source",
      "Neutralize hydrogen peroxide using the enzyme catalase (2 H2O2 -> 2 H2O + O2), protecting the cell from oxidative damage",
      "Store hydrogen peroxide for use in the electron transport chain",
      "Transport hydrogen peroxide out of the cell via exocytosis"
    ],
    "answerIndex": 1,
    "explanation": "Catalase in peroxisomes rapidly converts toxic H2O2 (a reactive oxygen species produced by oxidative metabolism) into harmless water and oxygen. Peroxisomes also oxidize fatty acids and detoxify alcohol — that's why liver cells are especially rich in them."
  },
]

added_fc = added_q = 0
for f in new_fc:
    if f["id"] not in existing_fc:
        ch3["flashcards"].append(f); added_fc += 1
for q in new_q:
    if q["id"] not in existing_q:
        ch3["quiz"].append(q); added_q += 1

print(f"ch3: +{added_fc} fc, +{added_q} q -> {len(ch3['flashcards'])} fc / {len(ch3['quiz'])} q total")

out = json.dumps(data, indent=2, ensure_ascii=False)
SRC.write_text(out, encoding="utf-8")
ROOT.write_text(out, encoding="utf-8")
print("Done.")
