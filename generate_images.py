import time
import os
from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyB5IC4zkSEl3ul_RQ1UnAzPiD9aL5vMijM")
MODEL = "gemini-3.1-flash-image"
OUT_DIR = "images"
os.makedirs(OUT_DIR, exist_ok=True)

MECHANISMS = [
    {
        "id": "mechanism_01_variable_ratio",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing how variable ratio reinforcement works in the brain. "
            "Show a sagittal cross-section of the human brain with the striatum highlighted. "
            "On the left side, show a 'PREDICTABLE REWARD' scenario with a flat dopamine line labeled 'No significant DA release'. "
            "On the right side, show a 'VARIABLE/UNPREDICTABLE REWARD' scenario with a large dopamine spike in the striatum labeled 'Significant DA surge'. "
            "Include a small icon of a slot machine and a smartphone side by side at the top to show the parallel. "
            "Draw arrows showing dopamine release patterns. "
            "Style: clean black line art on white background, blue and red marker accents, hand-drawn whiteboard aesthetic, educational medical diagram. Title: 'VARIABLE RATIO REINFORCEMENT — The Slot Machine Effect'"
        ),
    },
    {
        "id": "mechanism_02_wanting_vs_liking",
        "prompt": (
            "Create a whiteboard-style scientific illustration of the mesolimbic dopamine pathway showing 'WANTING vs LIKING'. "
            "Show a sagittal brain cross-section with the pathway from VTA (ventral tegmental area) through nucleus accumbens to prefrontal cortex clearly drawn with blue arrows. "
            "On the left side of the diagram, show a large spike labeled 'WANTING (Dopamine)' with text 'fires BEFORE reward — anticipation'. "
            "On the right side, show a much smaller bump labeled 'LIKING (Opioids/Serotonin)' with text 'fires DURING reward — brief satisfaction'. "
            "Add a small timeline at the bottom showing: CUE → DOPAMINE SPIKE → REWARD → QUICK FADE → NEXT CUE. "
            "Style: clean black line art on white background, blue for wanting pathway, green for liking, hand-drawn whiteboard marker aesthetic. Title: 'WANTING vs LIKING — Berridge's Discovery'"
        ),
    },
    {
        "id": "mechanism_03_d2_downregulation",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing D2 receptor downregulation in the striatum. "
            "Show two side-by-side close-up views of a synapse (presynaptic and postsynaptic neurons): "
            "LEFT side labeled 'HEALTHY BRAIN' — many D2 receptors on the postsynaptic membrane (drawn as Y-shaped receptors), normal dopamine molecules binding, labeled '100% D2 receptor density'. "
            "RIGHT side labeled 'ADDICTED BRAIN' — far fewer D2 receptors on the postsynaptic membrane, some dopamine molecules floating unbound, labeled '~80% D2 receptor density (20% reduction)'. "
            "Below, show a simple bar comparing the two. Add text: 'Same mechanism as cocaine & alcohol addiction — PET scan confirmed (Kim et al. 2011)'. "
            "Style: clean black line art on white background, blue and red marker accents, hand-drawn whiteboard educational diagram. Title: 'D2 RECEPTOR DOWNREGULATION — The Tolerance Spiral'"
        ),
    },
    {
        "id": "mechanism_04_gray_matter_loss",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing structural brain changes from digital overconsumption. "
            "Show a top-down view of the human brain with six regions highlighted and labeled with impact indicators: "
            "1. Anterior Cingulate Cortex (ACC) — marked RED — 'impulse control, error detection' "
            "2. Dorsolateral Prefrontal Cortex (dlPFC) — marked RED — 'working memory, planning' "
            "3. Medial Orbitofrontal Cortex (mOFC) — marked RED — 'decision-making' "
            "4. Insular Cortex — marked ORANGE — 'self-awareness, time perception' "
            "5. Lateral Prefrontal Cortex — marked ORANGE — 'cognitive control' "
            "6. Striatum — marked ORANGE — 'habit formation' "
            "Use arrows pointing inward to indicate shrinkage/volume reduction. Add text: 'VBM meta-analysis: convergent gray matter reductions in heavy digital users'. "
            "Style: clean black line art on white background, red and orange color accents, hand-drawn whiteboard marker aesthetic. Title: 'STRUCTURAL BRAIN CHANGES — Gray Matter Loss Under the Scanner'"
        ),
    },
    {
        "id": "mechanism_05_fragmented_attention",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing how short-form content fragments attention. "
            "Show a sagittal brain cross-section with three areas highlighted: "
            "1. medial PFC (mPFC) with an UP arrow labeled 'OVERACTIVATED — brain works harder for basic tasks' "
            "2. dlPFC with a DOWN arrow labeled 'DECREASED — impaired working memory' "
            "3. vlPFC with a DOWN arrow labeled 'DECREASED — weakened inhibition' "
            "Below the brain, show a timeline diagram: a long continuous bar labeled 'SUSTAINED ATTENTION (healthy)' vs many short fragmented bars labeled 'FRAGMENTED ATTENTION (after scrolling)' with gaps between them labeled 'cognitive residue'. "
            "Include the stat '7.2 seconds — average attention span 2026 (was 12s in 2000)'. "
            "Style: clean black line art on white background, blue and red marker accents, hand-drawn whiteboard educational diagram. Title: 'THE FRAGMENTED MIND — Attention Erosion'"
        ),
    },
    {
        "id": "mechanism_06_deep_reading_circuit",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing the deep reading circuit in the brain (Maryanne Wolf's research). "
            "Show a side view (sagittal) brain with a neural circuit highlighted connecting: "
            "Visual cortex → Angular gyrus → Temporal lobe (language areas: Wernicke's area) → Frontal lobe (Broca's area) → Prefrontal cortex (inference, reflection). "
            "Show this circuit as a connected pathway with blue arrows. "
            "On the left side, label 'DEEP READING CIRCUIT — Active' with functions listed: 'empathy, critical thinking, inference, reflection, perspective-taking'. "
            "On the right side, show the same brain but with the circuit grayed out / dotted lines, labeled 'CIRCUIT ATROPHYING' with text: 'Replaced by scanning/skimming pathways'. "
            "Add Wolf's quote: 'The digital age is reshaping the reading circuits in our brains'. "
            "Style: clean black line art on white background, blue and gray marker accents, hand-drawn whiteboard aesthetic. Title: 'THE DEEP READING CIRCUIT — Use It or Lose It'"
        ),
    },
    {
        "id": "mechanism_07_default_mode_network",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing the Default Mode Network (DMN) of the brain. "
            "Show a medial (inner) view of the brain with four key DMN regions highlighted in blue and connected by curved lines: "
            "1. Medial Prefrontal Cortex (mPFC) — labeled 'self-reflection, future planning' "
            "2. Posterior Cingulate Cortex (PCC) — labeled 'memory integration' "
            "3. Precuneus — labeled 'consciousness, self-awareness' "
            "4. Angular Gyrus — labeled 'creative connections' "
            "Show two states side by side: LEFT: 'DMN ACTIVE — during rest, daydreaming' with the network glowing/active. "
            "RIGHT: 'DMN SUPPRESSED — during constant scrolling' with the network grayed out and a smartphone icon. "
            "Add text: 'Constant stimulation prevents the brain from doing its most important integrative work'. "
            "Style: clean black line art on white background, blue glow for active DMN, gray for suppressed, hand-drawn whiteboard aesthetic. Title: 'DEFAULT MODE NETWORK — What You Lose When You Never Do Nothing'"
        ),
    },
    {
        "id": "mechanism_08_addiction_comparison",
        "prompt": (
            "Create a whiteboard-style scientific illustration comparing substance addiction and digital addiction pathways in the brain. "
            "Show one sagittal brain cross-section in the center with the reward circuit highlighted (VTA → Nucleus Accumbens → PFC). "
            "On the LEFT side, list substance addiction triggers (alcohol, cocaine, gambling icons) with an arrow pointing to the pathway. "
            "On the RIGHT side, list digital addiction triggers (smartphone, TikTok scroll, notifications icons) with an arrow pointing to the SAME pathway. "
            "In the center, label the shared features: 'Same VTA→NAc→PFC pathway', 'Same ~20% D2 reduction', 'Same gray matter changes in ACC, OFC, PFC', 'Same ventral→dorsal habit shift'. "
            "Add text at bottom: 'The neurological parallel is not metaphorical — neuroimaging confirms identical circuits'. "
            "Style: clean black line art on white background, blue and red marker accents, hand-drawn whiteboard educational diagram. Title: 'SAME BRAIN CIRCUIT — Substance vs Digital Addiction'"
        ),
    },
    {
        "id": "mechanism_09_anhedonia_threshold",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing Hart's anhedonia threshold model. "
            "Show three horizontal panels stacked vertically, each showing a brain's pleasure center with a threshold barrier: "
            "TOP panel: 'HEALTHY BRAIN' — low threshold barrier (drawn as a short wall), small everyday pleasures (sunset, conversation, meal icons) easily cross over the barrier to reach the pleasure center. Many things bring joy. "
            "MIDDLE panel: 'MODERATE USE' — medium threshold barrier, only medium-intensity experiences cross the barrier. Some everyday pleasures fall short. "
            "BOTTOM panel: 'HEAVY USE' — very high threshold barrier, only extreme stimulation crosses the barrier. Almost all everyday pleasures bounce off the wall. "
            "Use a gradient from green (healthy) to yellow (moderate) to red (heavy use). "
            "Add text: 'Dopamine flooding raises the barrier that enjoyment must cross — Digital Anhedonia (Lakhan et al. 2025)'. "
            "Style: clean black line art on white background, green/yellow/red color progression, hand-drawn whiteboard aesthetic. Title: 'THE RISING PLEASURE THRESHOLD — Thrilled to Death'"
        ),
    },
    {
        "id": "mechanism_10_pleasure_pain_seesaw",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing Lembke's pleasure-pain seesaw (opponent-process theory). "
            "Show three states of a seesaw/balance scale with a brain as the fulcrum: "
            "STATE 1 (top): 'INITIAL USE' — seesaw tipped toward PLEASURE (green side up), PAIN side (red) down. Label: 'Dopamine spike from scrolling'. "
            "STATE 2 (middle): 'COMPENSATORY DIP' — seesaw tips toward PAIN (red side up), PLEASURE side (green) down. Label: 'Brain overcompensates — restlessness, anxiety, boredom'. "
            "STATE 3 (bottom): 'CHRONIC USE' — the entire seesaw has shifted so the resting neutral point is below the original baseline, tilted toward pain. Label: 'Baseline mood settles below neutral — chronic low-grade dysphoria'. "
            "Add Lembke quote: 'The smartphone is the modern-day hypodermic needle'. "
            "Style: clean black line art on white background, green for pleasure, red for pain, hand-drawn whiteboard aesthetic. Title: 'THE PLEASURE-PAIN SEESAW — Lembke's Dopamine Nation'"
        ),
    },
    {
        "id": "mechanism_11_neuroplasticity",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing neuroplasticity working in two directions (Carr's 'The Shallows'). "
            "Show two side-by-side brain views: "
            "LEFT BRAIN — 'DEEP THINKING PATHWAYS': Show thick, strong neural connections (drawn as bold lines) connecting PFC, hippocampus, and language areas. Label: 'Strengthened by: sustained reading, single-tasking, deep focus, deliberate thinking'. "
            "RIGHT BRAIN — 'SHALLOW PROCESSING PATHWAYS': Show different thick connections optimized for rapid switching, with the deep pathways shown as thin/faded. Label: 'Strengthened by: scrolling, skimming, multitasking, context-switching'. "
            "Between them, show a double arrow with text: 'NEUROPLASTICITY — The brain physically rewires based on how you use it. 5 hours of internet use creates new neural pathways'. "
            "At bottom, add: 'The medium is the message — Marshall McLuhan'. "
            "Style: clean black line art on white background, blue for deep pathways, orange for shallow, hand-drawn whiteboard aesthetic. Title: 'NEUROPLASTICITY — Double-Edged Sword'"
        ),
    },
    {
        "id": "mechanism_12_brain_fog_retrieval",
        "prompt": (
            "Create a whiteboard-style scientific illustration showing the brain fog / memory retrieval problem. "
            "Show a sagittal brain cross-section with the memory retrieval circuit highlighted: "
            "1. PREFRONTAL CORTEX sends a 'retrieval cue' arrow down to the HIPPOCAMPUS. "
            "2. HIPPOCAMPUS performs 'pattern completion' and sends the memory trace back up. "
            "3. The memory surfaces into consciousness (shown as a lightbulb). "
            "Show TWO versions: "
            "LEFT: 'HEALTHY RETRIEVAL' — clean, direct arrows between PFC and hippocampus, fast retrieval, lightbulb ON. "
            "RIGHT: 'IMPAIRED RETRIEVAL' — the arrows are broken/congested/dotted, labeled with the causes: 'PFC degradation (-18%)', 'cognitive residue from switching', 'D2 dysregulation', 'atrophied retrieval muscles'. The lightbulb is dim with text 'Tip-of-tongue state'. "
            "Add small text: 'The memory exists — the highway to it is congested'. "
            "Style: clean black line art on white background, blue and red marker accents, hand-drawn whiteboard educational diagram. Title: 'BRAIN FOG — A Retrieval Problem, Not a Storage Problem'"
        ),
    },
]

for i, mech in enumerate(MECHANISMS):
    fname = f"{OUT_DIR}/{mech['id']}.png"
    if os.path.exists(fname) and os.path.getsize(fname) > 10000:
        print(f"[{i+1}/12] SKIP (exists): {mech['id']}")
        continue

    print(f"[{i+1}/12] Generating: {mech['id']}...", flush=True)
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=mech["prompt"],
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )
        saved = False
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                with open(fname, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"  -> Saved {len(part.inline_data.data)} bytes")
                saved = True
                break
        if not saved:
            print(f"  -> WARNING: no image in response")
    except Exception as e:
        print(f"  -> ERROR: {str(e)[:200]}")

    if i < len(MECHANISMS) - 1:
        time.sleep(3)

print("\nDone! All images generated.")
