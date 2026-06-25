"""Add 5 selectAll questions from practice_exam_ch1-3.json and fix ch3-q-041 choice 0."""

import json, pathlib

SRC  = pathlib.Path("src/data/content.json")
ROOT = pathlib.Path("content.json")

data = json.loads(SRC.read_text(encoding="utf-8"))

def ch(cid):
    return next(c for c in data["chapters"] if c["id"] == cid)

# ── Fix ch3-q-041 (SA:V ratio) — choice 0 had garbled text ──────────────────

ch3 = ch("ch3")
for q in ch3["quiz"]:
    if q["id"] == "ch3-q-041":
        q["choices"][0] = (
            "1.0 — SA = 3 × (3²) = 27 cm² (counting only 3 faces instead of all 6), "
            "V = 3³ = 27 cm³, ratio = 27/27 = 1.0"
        )
        print("Fixed ch3-q-041 choice 0")
        break

# ── Add selectAll questions ───────────────────────────────────────────────────

def existing_ids(cid):
    return {q["id"] for q in ch(cid)["quiz"]}

new_questions = {
    "ch1": [
        {
            "id": "ch1-q-043", "type": "selectAll",
            "section": "1.3", "difficulty": "hard",
            "question": "Which features improve the reliability of an experiment? (Select all that apply.)",
            "choices": [
                "Larger sample size",
                "A placebo control group",
                "Double-blind design",
                "Changing several variables at once",
                "Peer review before publication",
            ],
            "answerIndices": [0, 1, 2, 4],
            "explanation": (
                "Large samples, placebo controls, double-blind design, and peer review all reduce bias and increase reliability. "
                "Changing several variables at once makes it impossible to determine which variable caused any observed change."
            ),
        },
    ],
    "ch2": [
        {
            "id": "ch2-q-058", "type": "selectAll",
            "section": "2.5", "difficulty": "easy",
            "question": "Which are the four classes of organic (carbon-based) macromolecules found in all living organisms? (Select all that apply.)",
            "choices": [
                "Carbohydrates",
                "Lipids",
                "Proteins",
                "Nucleic acids",
                "Minerals",
            ],
            "answerIndices": [0, 1, 2, 3],
            "explanation": (
                "The four classes of organic macromolecules are carbohydrates, lipids, proteins, and nucleic acids. "
                "Minerals (such as calcium, iron, and sodium) are inorganic — they are not carbon-based macromolecules."
            ),
        },
    ],
    "ch3": [
        {
            "id": "ch3-q-059", "type": "selectAll",
            "section": "3.1", "difficulty": "hard",
            "question": "Which features are found in ALL cells — both prokaryotic and eukaryotic? (Select all that apply.)",
            "choices": [
                "DNA",
                "Ribosomes",
                "Nucleus",
                "Cell (plasma) membrane",
                "Cytoplasm",
                "Chloroplasts",
            ],
            "answerIndices": [0, 1, 3, 4],
            "explanation": (
                "ALL cells have DNA (genetic material), ribosomes (for protein synthesis), a plasma membrane, and cytoplasm. "
                "A membrane-bound nucleus is eukaryotic only. Chloroplasts are found only in plant and algal cells."
            ),
        },
        {
            "id": "ch3-q-060", "type": "selectAll",
            "section": "3.2", "difficulty": "medium",
            "question": "Which structures are found in plant cells but NOT in animal cells? (Select all that apply.)",
            "choices": [
                "Cell wall (made of cellulose)",
                "Chloroplast",
                "Mitochondrion",
                "Large central vacuole",
                "Ribosome",
            ],
            "answerIndices": [0, 1, 3],
            "explanation": (
                "Plant cells have a cell wall (cellulose), chloroplasts (for photosynthesis), and a large central vacuole (for turgor pressure and storage). "
                "Mitochondria and ribosomes are found in both plant and animal cells."
            ),
        },
        {
            "id": "ch3-q-061", "type": "selectAll",
            "section": "3.3", "difficulty": "hard",
            "question": "Which are recognized types of membrane proteins? (Select all that apply.)",
            "choices": [
                "Transport proteins",
                "Enzyme proteins",
                "Recognition proteins",
                "Adhesion proteins",
                "Receptor proteins",
                "Storage proteins",
            ],
            "answerIndices": [0, 1, 2, 3, 4],
            "explanation": (
                "The five types of membrane proteins are: transport (channels/carriers), enzymes (catalyze reactions at the membrane), "
                "recognition (glycoproteins as 'self' ID tags), adhesion (attach cells to each other or the matrix), and receptor (bind signals). "
                "'Storage proteins' is not one of the five — storage occurs in the cytoplasm, not embedded in membranes."
            ),
        },
    ],
}

added_total = 0
for cid, questions in new_questions.items():
    ids = existing_ids(cid)
    for q in questions:
        if q["id"] not in ids:
            ch(cid)["quiz"].append(q)
            added_total += 1
            print(f"Added {q['id']} to {cid}")

print(f"\nTotal added: {added_total}")
for cid in ["ch1", "ch2", "ch3"]:
    print(f"  {cid}: {len(ch(cid)['quiz'])} questions total")

out = json.dumps(data, indent=2, ensure_ascii=False)
SRC.write_text(out, encoding="utf-8")
ROOT.write_text(out, encoding="utf-8")
print("Saved.")
