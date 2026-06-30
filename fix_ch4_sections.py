"""
Audit fix for Chapter 4 (The Energy of Life):
1. Relabel sections to match the textbook's real 4.1-4.5 structure
   (our content only had 4.1-4.4, with 4.2/4.3/4.4 mislabeled, and three
   questions stuck under junk IDs ch4-s1/ch4-s2/ch4-s3).
2. Add flashcards + quiz questions for gaps found versus the textbook:
   - 4.2 Networks of Chemical Reactions (metabolism, redox, electron
     transport chains) was entirely missing as a section.
   - 4.3 ATP: phosphorylation mechanism, why ATP can't be stockpiled.
   - 4.4 Enzymes: positive feedback (we only had negative feedback).
   - 4.5 Membrane Transport: aquaporins, ATP synthase/chemiosmosis,
     turgor pressure as its own term, concentration gradient/selective
     permeability as explicit terms.
"""

import json, pathlib

SRC = pathlib.Path("src/data/content.json")
ROOT = pathlib.Path("content.json")

data = json.loads(SRC.read_text(encoding="utf-8"))
ch4 = next(c for c in data["chapters"] if c["id"] == "ch4")

# ── 1. Fix sections array to match the textbook ─────────────────────────────

ch4["sections"] = [
    {"id": "4.1", "title": "All Cells Capture and Use Energy"},
    {"id": "4.2", "title": "Networks of Chemical Reactions Sustain Life"},
    {"id": "4.3", "title": "ATP Is Cellular Energy Currency"},
    {"id": "4.4", "title": "Enzymes Speed Biochemical Reactions"},
    {"id": "4.5", "title": "Membrane Transport"},
]

# ── 2. Remap existing flashcard sections (shift ATP/Enzymes/Transport down) ──

FC_SECTION_REMAP = {
    "4.1": "4.1",
    "4.2": "4.3",   # was ATP
    "4.3": "4.4",   # was Enzymes
    "4.4": "4.5",   # was Membrane Transport
}
for f in ch4["flashcards"]:
    f["section"] = FC_SECTION_REMAP[f["section"]]

# ── 3. Remap existing quiz sections, including per-question junk-ID fixes ───

QUIZ_SECTION_REMAP = {
    "4.1": "4.1",
    "4.2": "4.3",
    "4.3": "4.4",
    "4.4": "4.5",
}
# Per-question overrides for the junk ch4-s1/s2/s3 section IDs
QUESTION_SECTION_OVERRIDE = {
    "The Second Law of Thermodynamics states that:": "4.1",
    "In metabolism, coupled reactions refer to:": "4.3",
    "Why must organisms continuously consume food and energy?": "4.1",
    "A cofactor differs from a coenzyme in that a cofactor is typically:": "4.4",
    "Feedback inhibition in a metabolic pathway means the end product:": "4.4",
    "An enzyme's active site binds its substrate. After the reaction, the enzyme is:": "4.4",
    "A plant cell placed in a hypotonic solution will:": "4.5",
    "Which of these crosses the plasma membrane by SIMPLE diffusion, requiring no transport proteins?": "4.5",
    "Receptor-mediated endocytosis differs from phagocytosis because:": "4.5",
    "The Na⁺/K⁺ pump moves 3 Na⁺ OUT and 2 K⁺ IN per ATP hydrolyzed. This is an example of:": "4.5",
}
for q in ch4["quiz"]:
    if q["question"] in QUESTION_SECTION_OVERRIDE:
        q["section"] = QUESTION_SECTION_OVERRIDE[q["question"]]
    elif q["section"] in QUIZ_SECTION_REMAP:
        q["section"] = QUIZ_SECTION_REMAP[q["section"]]
    else:
        raise ValueError(f"Unhandled section/question: {q['section']} | {q['question']}")

# ── 4. New flashcards ────────────────────────────────────────────────────────

new_flashcards = [
    {
        "id": "ch4-fc-021", "section": "4.2", "difficulty": "easy",
        "front": "Metabolism",
        "back": "The sum of all chemical reactions occurring in a cell. Includes anabolic reactions (build complex molecules from simple ones, require energy) and catabolic reactions (break down complex molecules, release energy).",
    },
    {
        "id": "ch4-fc-022", "section": "4.2", "difficulty": "medium",
        "front": "Oxidation vs. reduction (redox reactions)",
        "back": "Oxidation = LOSS of electrons (and energy) from a molecule. Reduction = GAIN of electrons (and energy). The two always occur together: one molecule's oxidation requires another's reduction. Most energy transformations in cells happen via these redox reactions.",
    },
    {
        "id": "ch4-fc-023", "section": "4.2", "difficulty": "medium",
        "front": "Electron transport chain (ETC)",
        "back": "A series of membrane proteins that pass electrons from one to the next, like a relay. Each protein is reduced (gains the electron) then oxidized (passes it on). Small amounts of energy are released at each step and harvested by the cell. Central to both photosynthesis (ch. 5) and cellular respiration (ch. 6).",
    },
    {
        "id": "ch4-fc-024", "section": "4.3", "difficulty": "medium",
        "front": "Phosphorylation",
        "back": "Transfer of a phosphate group from one molecule (often ATP) to another. Has two possible effects: (1) energizes the target molecule, making it more likely to react further, or (2) changes the target protein's shape, which can power transport or other work.",
    },
    {
        "id": "ch4-fc-025", "section": "4.3", "difficulty": "easy",
        "front": "Why cells can't stockpile ATP",
        "back": "ATP's high-energy phosphate bonds make it too unstable for long-term storage. A typical cell uses ~2 billion ATP molecules/minute and recycles its entire ATP pool roughly every minute. Cells store energy instead as fats, starch, and glycogen, converting them to ATP via cellular respiration as needed.",
    },
    {
        "id": "ch4-fc-026", "section": "4.4", "difficulty": "medium",
        "front": "Positive feedback (vs. negative feedback)",
        "back": "A process that reinforces/amplifies an existing change rather than reversing it (opposite of negative feedback/feedback inhibition). Much rarer in biology. Example: blood clotting — each clotting reaction stimulates the next, accelerating clot formation until the pathway shuts off (negative feedback) once bleeding stops.",
    },
    {
        "id": "ch4-fc-027", "section": "4.5", "difficulty": "easy",
        "front": "Selective permeability & concentration gradient",
        "back": "Selective permeability: a membrane allows some substances through freely but blocks others. Concentration gradient: a difference in solute concentration between two neighboring regions. Gradients store potential energy and dissipate (disappear) over time unless energy is spent to maintain them.",
    },
    {
        "id": "ch4-fc-028", "section": "4.5", "difficulty": "medium",
        "front": "Aquaporins",
        "back": "Channel proteins that increase the rate of water movement across a membrane (speed up osmosis). Found in bacteria, plants, and animals. Example: kidney cells control how much water is reabsorbed into the body by changing the number of aquaporins in their membranes.",
    },
    {
        "id": "ch4-fc-029", "section": "4.5", "difficulty": "hard",
        "front": "ATP synthase & chemiosmosis",
        "back": "A membrane channel protein that lets H+ ions flow down their concentration gradient (a form of facilitated diffusion) and uses the released energy to synthesize ATP from ADP + Pi. This process — chemiosmosis — powers ATP production in both photosynthesis and cellular respiration.",
    },
    {
        "id": "ch4-fc-030", "section": "4.5", "difficulty": "easy",
        "front": "Turgor pressure",
        "back": "The force of water pressing the plasma membrane against the cell wall in a plant cell that has taken up water by osmosis. Keeps plants rigid and upright. Lost turgor (e.g., in a hypertonic or dry environment) causes wilting.",
    },
]
ch4["flashcards"].extend(new_flashcards)

# ── 5. New quiz questions ────────────────────────────────────────────────────

new_quiz = [
    # 4.2 — Networks of Chemical Reactions
    {
        "id": "ch4-q-026", "section": "4.2", "difficulty": "easy",
        "question": "In a redox reaction, the molecule that LOSES electrons is said to be:",
        "choices": ["Reduced", "Oxidized", "Hydrolyzed", "Phosphorylated"],
        "answerIndex": 1,
        "explanation": "Oxidation = loss of electrons (and their energy). The molecule that loses electrons is oxidized; the molecule that gains those electrons is reduced. The two always happen together in a redox reaction.",
    },
    {
        "id": "ch4-q-027", "section": "4.2", "difficulty": "medium",
        "question": "Why must oxidation and reduction always occur together in a redox reaction?",
        "choices": [
            "Enzymes require both processes to remain catalytically active during the reaction",
            "Electrons removed from one molecule during oxidation must be accepted by another molecule, reducing it",
            "ATP can only be synthesized when oxidation and reduction cancel out each other's energy change",
            "Cells evolved redox reactions specifically to balance pH on both sides of the membrane",
        ],
        "answerIndex": 1,
        "explanation": "Electrons don't simply disappear — when one molecule loses electrons (is oxidized), another molecule must accept them (is reduced). This pairing is why the two halves of a redox reaction always occur simultaneously.",
    },
    {
        "id": "ch4-q-028", "section": "4.2", "difficulty": "medium",
        "question": "In an electron transport chain, as an electron passes from one membrane protein to the next:",
        "choices": [
            "A large burst of energy is released all at once at the final step only",
            "Small amounts of energy are released at each step, which the cell harvests for other reactions",
            "The electron gains additional energy at each protein, building toward a maximum at the chain's end",
            "The chain consumes ATP at each step to keep the electron moving forward",
        ],
        "answerIndex": 1,
        "explanation": "Electron transport chains release energy gradually, in small steps, as electrons pass from protein to protein — like a ball rolling down a staircase rather than off a cliff. The cell captures this stepwise energy release to do useful work, such as pumping H+ ions.",
    },
    {
        "id": "ch4-q-029", "section": "4.2", "difficulty": "hard", "type": "selectAll",
        "question": "Which of the following are true of metabolism? (Select all that apply.)",
        "choices": [
            "It includes anabolic reactions that build complex molecules from simpler ones",
            "It includes catabolic reactions that break down complex molecules",
            "It refers only to reactions that occur inside mitochondria",
            "Photosynthesis and cellular respiration are both part of an organism's metabolism",
            "Every metabolic reaction either absorbs or releases energy",
        ],
        "answerIndices": [0, 1, 3, 4],
        "explanation": "Metabolism is the sum of ALL chemical reactions in a cell — anabolic (building) and catabolic (breaking down) — not limited to any one organelle. Photosynthesis and respiration are major metabolic pathways, and every reaction either requires energy input (endergonic) or releases energy (exergonic).",
    },
    {
        "id": "ch4-q-030", "section": "4.2", "difficulty": "easy",
        "question": "Electron transport chains are used in which of the following processes?",
        "choices": [
            "Only cellular respiration",
            "Only photosynthesis",
            "Both photosynthesis and cellular respiration",
            "Neither — ETCs are unique to anaerobic fermentation",
        ],
        "answerIndex": 2,
        "explanation": "Both photosynthesis (chapter 5) and cellular respiration (chapter 6) rely on electron transport chains embedded in membranes to harvest energy released as electrons move from protein to protein.",
    },
    # 4.3 — ATP
    {
        "id": "ch4-q-031", "section": "4.3", "difficulty": "medium", "type": "selectAll",
        "question": "Phosphorylation — the transfer of a phosphate group from ATP to a target molecule — can have which of the following effects? (Select all that apply.)",
        "choices": [
            "Energize the target molecule, making it more likely to bond with other molecules",
            "Change the shape of a target protein",
            "Permanently destroy the target molecule's chemical structure",
            "Convert the target molecule directly into a new strand of DNA",
        ],
        "answerIndices": [0, 1],
        "explanation": "Phosphorylation has two possible effects: energizing a target molecule (e.g., activating glucose so it bonds into a polysaccharide) or changing a protein's shape (which can power transport or other mechanical work). It does not destroy the molecule or create DNA.",
    },
    {
        "id": "ch4-q-032", "section": "4.3", "difficulty": "medium",
        "question": "Why don't cells store large reserves of ATP for later use?",
        "choices": [
            "ATP's high-energy phosphate bonds are too unstable for long-term storage, so cells store fats and carbohydrates instead",
            "Cells lack the enzymes needed to synthesize ATP in advance of when it's needed",
            "ATP is too large a molecule to be stored in the cytoplasm without forming toxic aggregates",
            "Storing ATP would interfere with the cell's ability to maintain osmotic balance",
        ],
        "answerIndex": 0,
        "explanation": "ATP's unstable phosphate bonds make it a poor long-term energy-storage molecule. Cells instead store energy in fats, starch, and glycogen, and convert these to ATP via cellular respiration as it's needed — recycling the entire ATP pool roughly once a minute.",
    },
    {
        "id": "ch4-q-033", "section": "4.3", "difficulty": "easy",
        "question": "A cell uses ATP to attach a phosphate group to glucose, making it more reactive and able to bond into a polysaccharide chain. This is an example of:",
        "choices": ["Hydrolysis", "Phosphorylation", "Oxidative decarboxylation", "Allosteric inhibition"],
        "answerIndex": 1,
        "explanation": "This is phosphorylation — ATP transfers a phosphate group to glucose, energizing it ('activating' it) so it is more likely to react and bond with other molecules to build a polysaccharide.",
    },
    # 4.4 — Enzymes
    {
        "id": "ch4-q-034", "section": "4.4", "difficulty": "medium",
        "question": "Which scenario best describes POSITIVE feedback?",
        "choices": [
            "An amino acid accumulates and inhibits the first enzyme in its own synthesis pathway",
            "Blood clotting reactions accelerate each other once a clot begins forming, speeding up further clotting",
            "A noncompetitive inhibitor binds an allosteric site, reducing enzyme activity as product builds up",
            "Rising body temperature triggers sweating, which cools the body back toward normal",
        ],
        "answerIndex": 1,
        "explanation": "Positive feedback reinforces an existing change rather than reversing it. In blood clotting, each step of the clotting cascade stimulates the next, accelerating the process — the opposite of negative feedback (options 0, 2, and 3, which all reverse a change).",
    },
    {
        "id": "ch4-q-035", "section": "4.4", "difficulty": "easy",
        "question": "How does positive feedback differ from negative feedback (feedback inhibition) in biological systems?",
        "choices": [
            "Positive feedback reinforces an existing change; negative feedback reverses a change. Positive feedback is much rarer in organisms",
            "Positive feedback always requires ATP; negative feedback never does",
            "Positive feedback only regulates enzyme pathways; negative feedback only regulates membrane transport",
            "Positive feedback occurs in plants; negative feedback occurs in animals",
        ],
        "answerIndex": 0,
        "explanation": "Negative feedback (feedback inhibition) is the common regulatory strategy in cells — it reverses changes to maintain stability, like an end product shutting down its own synthesis pathway. Positive feedback amplifies a change instead and is much rarer; blood clotting is a classic example.",
    },
    # 4.5 — Membrane Transport
    {
        "id": "ch4-q-036", "section": "4.5", "difficulty": "easy",
        "question": "Aquaporins are membrane proteins that:",
        "choices": [
            "Pump hydrogen ions against their concentration gradient using ATP",
            "Increase the rate of water movement across a membrane during osmosis",
            "Actively transport glucose into the cell against its concentration gradient",
            "Detect extracellular signals and trigger receptor-mediated endocytosis",
        ],
        "answerIndex": 1,
        "explanation": "Aquaporins are channel proteins that speed up osmosis by increasing how quickly water crosses a membrane. Kidney cells, for example, control water reabsorption by adjusting how many aquaporins are in their membranes.",
    },
    {
        "id": "ch4-q-037", "section": "4.5", "difficulty": "medium",
        "question": "ATP synthase is best described as a membrane protein that:",
        "choices": [
            "Actively pumps ATP out of the mitochondrion using energy from glucose",
            "Allows H+ ions to flow down their concentration gradient and uses that energy to synthesize ATP",
            "Hydrolyzes ATP to power the sodium-potassium pump directly",
            "Catalyzes the breakdown of glucose into pyruvate during glycolysis",
        ],
        "answerIndex": 1,
        "explanation": "ATP synthase is a channel that lets H+ ions move down their concentration gradient (facilitated diffusion) — and harnesses the energy released to attach a phosphate to ADP, generating ATP. This process, called chemiosmosis, powers ATP production in both photosynthesis and respiration.",
    },
    {
        "id": "ch4-q-038", "section": "4.5", "difficulty": "hard",
        "question": "Which transport category does ATP synthase's H+ channel belong to?",
        "choices": [
            "Active transport, because it produces ATP",
            "Facilitated diffusion, because H+ moves down its gradient through a channel protein without direct ATP cost",
            "Simple diffusion, because no protein is involved",
            "Exocytosis, because it releases a substance from the cell",
        ],
        "answerIndex": 1,
        "explanation": "Even though ATP synthase produces ATP, the H+ ions themselves move passively DOWN their concentration gradient through the channel — that's facilitated diffusion. The energy released by this passive flow is what the enzyme uses to build ATP.",
    },
    {
        "id": "ch4-q-039", "section": "4.5", "difficulty": "easy",
        "question": "A wilted houseplant perks back up after watering. This is best explained by:",
        "choices": [
            "Increased turgor pressure as water enters plant cells by osmosis and pushes against the cell wall",
            "Active transport pumping water molecules directly into the central vacuole",
            "Exocytosis of stored water from vesicles into the extracellular space",
            "A drop in turgor pressure as solutes diffuse out of the cell wall",
        ],
        "answerIndex": 0,
        "explanation": "Watering increases the soil's water concentration relative to the plant cells, so water enters by osmosis. The rigid cell wall resists the resulting pressure, creating turgor pressure that makes the plant rigid again. Loss of turgor pressure (not a gain) is what causes wilting.",
    },
    {
        "id": "ch4-q-040", "section": "4.5", "difficulty": "medium",
        "question": "A concentration gradient across a membrane represents:",
        "choices": [
            "A form of potential energy that dissipates over time unless energy is spent maintaining it",
            "A type of covalent bond between two adjacent phospholipids",
            "Kinetic energy that is immediately lost as heat upon formation",
            "An enzyme-catalyzed reaction occurring at the membrane surface",
        ],
        "answerIndex": 0,
        "explanation": "A concentration gradient is potential energy — the difference in solute concentration between two regions. Without continued energy input, random molecular motion causes the gradient to dissipate (equalize) over time, just as any other form of potential energy is eventually released.",
    },
    {
        "id": "ch4-q-041", "section": "4.5", "difficulty": "hard", "type": "selectAll",
        "question": "Which of the following are examples of facilitated diffusion? (Select all that apply.)",
        "choices": [
            "Glucose entering a cell through a GLUT transporter protein",
            "H+ ions flowing through ATP synthase down their concentration gradient",
            "The sodium-potassium pump moving Na+ out and K+ into a cell",
            "Water moving through an aquaporin channel",
            "A white blood cell engulfing a bacterium by phagocytosis",
        ],
        "answerIndices": [0, 1],
        "explanation": "Facilitated diffusion is PASSIVE movement (down a concentration gradient) through a channel or carrier protein, with no ATP required — like glucose through GLUT transporters or H+ through ATP synthase. The Na+/K+ pump is active transport (uses ATP, moves against gradients). Water through aquaporins is classified separately as osmosis. Phagocytosis is endocytosis.",
    },
]
ch4["quiz"].extend(new_quiz)

# ── Save ──────────────────────────────────────────────────────────────────────

out = json.dumps(data, indent=2, ensure_ascii=False)
SRC.write_text(out, encoding="utf-8")
ROOT.write_text(out, encoding="utf-8")

print(f"ch4 flashcards: {len(ch4['flashcards'])} (+{len(new_flashcards)})")
print(f"ch4 quiz: {len(ch4['quiz'])} (+{len(new_quiz)})")
sa_count = sum(1 for q in ch4['quiz'] if q.get('type') == 'selectAll')
print(f"ch4 selectAll questions: {sa_count}")
