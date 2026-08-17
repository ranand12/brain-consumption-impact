from ebooklib import epub
import re

book = epub.EpubBook()
book.set_identifier('consumed-mind-2026')
book.set_title('The Consumed Mind — What Short-Form Content Does to Your Brain')
book.set_language('en')
book.add_author('Neuroscience Research Briefing')

STYLE = '''
body {
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.6;
  color: #1a1a1a;
  margin: 0;
  padding: 0;
}
h1 {
  font-size: 2em;
  line-height: 1.15;
  margin-bottom: 0.5em;
  font-weight: 700;
}
h2 {
  font-size: 1.5em;
  line-height: 1.2;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
  font-weight: 700;
  page-break-after: avoid;
}
h3 {
  font-size: 1.2em;
  font-weight: 600;
  margin-top: 1.2em;
  margin-bottom: 0.4em;
}
p {
  margin-bottom: 0.8em;
  text-align: justify;
}
.kicker {
  font-size: 0.75em;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #c0392b;
  font-weight: 600;
  margin-bottom: 0.5em;
}
.subtitle {
  font-size: 1.1em;
  color: #555;
  margin-bottom: 1.5em;
  line-height: 1.5;
}
.section-number {
  font-size: 0.75em;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #2a78d6;
  font-weight: 600;
  margin-bottom: 0.3em;
}
.stat-box {
  border: 1px solid #ddd;
  padding: 0.8em 1em;
  margin-bottom: 0.8em;
  page-break-inside: avoid;
}
.stat-value {
  font-size: 1.8em;
  font-weight: 700;
  line-height: 1.1;
}
.stat-delta {
  font-size: 0.8em;
  font-weight: 600;
  color: #c0392b;
}
.stat-label {
  font-size: 0.8em;
  color: #777;
  margin-top: 0.3em;
}
.callout {
  border-left: 3px solid #2a78d6;
  padding: 0.8em 1em;
  margin: 1em 0;
  background: #f7f7f5;
  page-break-inside: avoid;
}
.callout.warn {
  border-left-color: #c0392b;
}
.callout.insight {
  border-left-color: #1baf7a;
}
.callout-title {
  font-size: 0.8em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.4em;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
  font-size: 0.9em;
  page-break-inside: avoid;
}
th {
  text-align: left;
  padding: 0.5em;
  font-size: 0.8em;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #777;
  border-bottom: 2px solid #999;
  font-weight: 600;
}
td {
  padding: 0.5em;
  border-bottom: 1px solid #ddd;
  vertical-align: top;
}
.bar-chart-text {
  margin: 1em 0;
  font-size: 0.9em;
}
.bar-item {
  margin-bottom: 0.3em;
}
.bar-name {
  font-weight: 500;
}
.bar-visual {
  font-family: monospace;
  font-size: 0.85em;
  color: #555;
}
.cycle-flow {
  text-align: center;
  margin: 1em 0;
  padding: 0.5em;
  border: 1px solid #ddd;
  page-break-inside: avoid;
}
.cycle-step-inline {
  display: inline;
  font-weight: 600;
}
.brain-region-box {
  border: 1px solid #ddd;
  padding: 0.8em 1em;
  margin-bottom: 0.8em;
  page-break-inside: avoid;
}
.severity-high {
  font-size: 0.75em;
  font-weight: 600;
  color: #c0392b;
  text-transform: uppercase;
}
.severity-medium {
  font-size: 0.75em;
  font-weight: 600;
  color: #96660a;
  text-transform: uppercase;
}
.region-name {
  font-weight: 600;
  font-size: 1em;
  margin-top: 0.2em;
}
.region-role {
  font-size: 0.8em;
  color: #777;
  font-style: italic;
}
.book-card {
  border: 1px solid #ddd;
  padding: 1em;
  margin: 1em 0;
  page-break-inside: avoid;
}
.book-title {
  font-size: 1.1em;
  font-weight: 600;
}
.book-author {
  font-size: 0.85em;
  color: #777;
  margin-bottom: 0.5em;
}
.book-thesis {
  font-size: 0.95em;
  font-style: italic;
}
.protocol-card {
  border: 1px solid #ddd;
  padding: 0.8em 1em;
  margin-bottom: 1em;
  page-break-inside: avoid;
}
.proto-num {
  font-weight: 700;
  font-size: 1.1em;
  color: #2a78d6;
}
.proto-title {
  font-weight: 600;
  font-size: 1.05em;
  margin-bottom: 0.3em;
}
.proto-evidence {
  font-size: 0.8em;
  color: #777;
  font-style: italic;
  margin-top: 0.5em;
}
.phase-badge {
  font-weight: 600;
  font-size: 0.85em;
}
.phase-strong { color: #1baf7a; }
.phase-moderate { color: #96660a; }
.phase-weak { color: #c55b8a; }
.phase-mixed { color: #2a78d6; }
ul, ol {
  margin: 0.5em 0 1em 1.5em;
}
li {
  margin-bottom: 0.4em;
}
.source-list {
  list-style: none;
  padding: 0;
  margin: 0.5em 0;
}
.source-list li {
  font-size: 0.85em;
  color: #555;
  padding: 0.3em 0;
  border-bottom: 1px solid #eee;
}
hr {
  border: none;
  border-top: 1px solid #ddd;
  margin: 2em 0;
}
.seesaw-diagram {
  text-align: center;
  margin: 1.5em 0;
  padding: 1em;
  border: 1px solid #ddd;
  page-break-inside: avoid;
}
.threshold-text {
  margin: 0.5em 0;
  font-size: 0.9em;
}
footer {
  font-size: 0.8em;
  color: #777;
  margin-top: 2em;
  border-top: 1px solid #ddd;
  padding-top: 1em;
}
'''

css = epub.EpubItem(uid='style', file_name='style/main.css', media_type='text/css', content=STYLE)
book.add_item(css)

IMAGE_FILES = [
    'mechanism_01_variable_ratio.png',
    'mechanism_02_wanting_vs_liking.png',
    'mechanism_03_d2_downregulation.png',
    'mechanism_04_gray_matter_loss.png',
    'mechanism_05_fragmented_attention.png',
    'mechanism_06_deep_reading_circuit.png',
    'mechanism_07_default_mode_network.png',
    'mechanism_08_addiction_comparison.png',
    'mechanism_09_anhedonia_threshold.png',
    'mechanism_10_pleasure_pain_seesaw.png',
    'mechanism_11_neuroplasticity.png',
    'mechanism_12_brain_fog_retrieval.png',
]

image_items = []
for img_file in IMAGE_FILES:
    img_path = f'images/{img_file}'
    with open(img_path, 'rb') as f:
        img_data = f.read()
    item = epub.EpubItem(
        uid=img_file.replace('.png', ''),
        file_name=f'images/{img_file}',
        media_type='image/png',
        content=img_data,
    )
    book.add_item(item)
    image_items.append(item)

chapters = []

def ch(title, filename, content):
    c = epub.EpubHtml(title=title, file_name=filename, lang='en')
    c.content = content
    c.add_item(css)
    book.add_item(c)
    chapters.append(c)
    return c

def img_tag(filename, alt, caption):
    return f'''
<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/{filename}" alt="{alt}" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">{caption}</p>
</div>
'''


# ── Title page ──
ch('The Consumed Mind', 'title.xhtml', '''
<div style="text-align:center; margin-top:3em;">
  <p class="kicker">Neuroscience Research Briefing</p>
  <h1>The Consumed Mind</h1>
  <p class="subtitle">What happens inside your brain when you scroll through short-form content &mdash;
  the neuroscience of dopamine hijacking, structural brain changes, attention erosion,
  and the quiet death of deep thought.</p>
  <p style="color:#777; font-size:0.85em; margin-top:2em;">This is not opinion. This is what the science says.</p>
  <p style="color:#999; font-size:0.8em; margin-top:3em;">Compiled August 2026</p>
</div>
''')

# ── Key Statistics ──
ch('Key Statistics', 'stats.xhtml', '''
<h2>Key Statistics</h2>
<div class="stat-box">
  <div class="stat-value">7.2s</div>
  <div class="stat-delta">&darr; 40% since 2000</div>
  <div class="stat-label">Average human attention span in 2026 (was 12s)</div>
</div>
<div class="stat-box">
  <div class="stat-value">&minus;12%</div>
  <div class="stat-delta">Gray matter loss</div>
  <div class="stat-label">Reduction in gray matter density in attention-regulating regions among heavy screen users</div>
</div>
<div class="stat-box">
  <div class="stat-value">&minus;18%</div>
  <div class="stat-delta">Prefrontal cortex</div>
  <div class="stat-label">Decrease in prefrontal cortex activity from infinite-scroll dopamine loops</div>
</div>
<div class="stat-box">
  <div class="stat-value">&minus;20%</div>
  <div class="stat-delta">D2 receptors</div>
  <div class="stat-label">Reduction in dopamine D2 receptor availability in the striatum of addicted users</div>
</div>
''')

# ── Section 1: Mechanism ──
ch('1. The Slot Machine in Your Pocket', 'ch01.xhtml', '''
<p class="section-number">Mechanism 01</p>
<h2>The Slot Machine in Your Pocket</h2>
<p>Every time you open TikTok, Instagram Reels, or YouTube Shorts, you are engaging with a system that operates on exactly the same psychological principle as a slot machine: <strong>variable ratio reinforcement</strong>.</p>
<p>B.F. Skinner discovered in the 1950s that the most persistent behaviors are produced not by predictable rewards, but by unpredictable ones. When a rat presses a lever and sometimes gets food, sometimes doesn&rsquo;t &mdash; with no discernible pattern &mdash; it presses the lever obsessively, far more than if it got food every time. The uncertainty is the engine.</p>
<p>This is what your feed does. Sometimes you get a video that makes you laugh. Sometimes it&rsquo;s boring. Sometimes it&rsquo;s infuriating. Sometimes it&rsquo;s transcendent. You never know which one is next. And that uncertainty &mdash; that <em>maybe</em> &mdash; is what makes you keep swiping.</p>

<div class="callout">
  <div class="callout-title">The PET scan evidence</div>
  <p>Zald et al. (2004) used PET imaging to measure dopamine release in the striatum. Rewards delivered on a <strong>variable ratio</strong> sequence produced significant dopamine release in the striatum. The same rewards delivered on a fixed, predictable schedule? <strong>No significant dopamine release detected.</strong> The unpredictability itself is what fires the dopamine system.</p>
</div>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_01_variable_ratio.png" alt="Variable ratio reinforcement: predictable vs unpredictable rewards and dopamine response" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">Variable ratio reinforcement produces far greater dopamine release than predictable rewards (Zald et al., 2004)</p>
</div>

<p>This isn&rsquo;t a metaphor. Platform engineers deliberately build these mechanics. Tristan Harris, former Google design ethicist, has called it &ldquo;persuasive technology&rdquo; &mdash; the systematic application of behavioral psychology to product design.</p>

<div class="cycle-flow">
  <p><strong>The Dopamine Loop</strong></p>
  <p><strong>Step 1: Cue</strong> (notification, boredom, habit trigger)<br/>
  &darr;<br/>
  <strong>Step 2: Anticipation</strong> (dopamine surges <em>before</em> reward)<br/>
  &darr;<br/>
  <strong>Step 3: Reward</strong> (fleeting satisfaction, 15&ndash;60 seconds)<br/>
  &darr;<br/>
  <strong>Step 4: Recalibration</strong> (brain resets, drives next swipe)<br/>
  &darr; <em>repeat</em></p>
</div>
''')

# ── Section 2: Dopamine ──
ch('2. Dopamine Is the Wanting Chemical', 'ch02.xhtml', '''
<p class="section-number">Mechanism 02</p>
<h2>Dopamine Is Not the Pleasure Chemical &mdash; It&rsquo;s the Wanting Chemical</h2>
<p>The popular understanding of dopamine is wrong. Dopamine does not produce pleasure. Neuroscientist Kent Berridge&rsquo;s foundational research demonstrated that dopamine drives <strong>wanting</strong>, not <strong>liking</strong>. The spike comes <em>before</em> the reward, not during it.</p>
<p>This distinction is crucial for understanding what short-form content does to you. When you scroll, your brain isn&rsquo;t experiencing pleasure &mdash; it&rsquo;s experiencing <strong>anticipation</strong>. The satisfaction of each video is fleeting, measured in seconds. Within moments, the brain recalibrates and generates a new pulse of wanting. You are chasing a feeling you never quite reach.</p>

<div class="callout insight">
  <div class="callout-title">Incentive salience theory</div>
  <p>Robinson and Berridge&rsquo;s incentive salience theory describes how repeated exposure to rewarding stimuli increases the brain&rsquo;s drive to <strong>want</strong> without a corresponding increase in <strong>liking</strong>. Over time, you want more but enjoy less. This is the neurological signature of compulsion, and it precisely describes the experience of someone who has been scrolling for an hour and feels worse, not better.</p>
</div>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_02_wanting_vs_liking.png" alt="Wanting versus liking in the dopamine system" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">Berridge's discovery: dopamine drives wanting (anticipation), not liking (pleasure).</p>
</div>

<p>The mesolimbic dopamine pathway &mdash; running from the ventral tegmental area (VTA) through the nucleus accumbens to the prefrontal cortex &mdash; is the circuit being exploited. This is the same pathway activated by gambling, cocaine, and alcohol. The mechanism is identical; only the stimulus differs.</p>
<p>Critically, the reward loops fire with high efficiency, but the <strong>satisfaction system</strong> &mdash; the quieter interplay of serotonin, oxytocin, and endorphins that produces genuine contentment &mdash; barely activates. Short-form content feeds the wanting circuit while starving the fulfillment circuit.</p>
''')

# ── Section 3: Tolerance ──
ch('3. Tolerance and D2 Receptor Downregulation', 'ch03.xhtml', '''
<p class="section-number">Mechanism 03</p>
<h2>Tolerance and D2 Receptor Downregulation</h2>
<p>This is where the neuroscience moves from concerning to alarming. Repeated overstimulation of the dopamine system doesn&rsquo;t just create a habit &mdash; it physically changes the receptor landscape of your brain.</p>
<p>PET scan studies by Kim et al. (2011) directly measured dopamine receptor density in people with internet addiction using radioligand [&sup1;&sup1;C] raclopride. The result: <strong>significantly reduced D2 receptor availability</strong> in the dorsal striatum, including the bilateral dorsal caudate and right putamen.</p>

<div class="callout">
  <div class="callout-title">Dopamine D2 Receptor Reduction in Digital Addiction</div>
  <p>Consistent ~20% reduction across PET imaging studies. Lower D2 = higher tolerance = more stimulation needed.</p>
</div>

<div class="bar-chart-text">
  <div class="bar-item"><span class="bar-name">Healthy controls:</span> <span class="bar-visual">&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;</span> 100%</div>
  <div class="bar-item"><span class="bar-name">Substance addiction:</span> <span class="bar-visual">&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;</span> ~78%</div>
  <div class="bar-item"><span class="bar-name">Internet addiction:</span> <span class="bar-visual">&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;&block;</span> ~80%</div>
</div>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_03_d2_downregulation.png" alt="D2 receptor downregulation: healthy vs addicted synapse" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">D2 receptor downregulation at the synapse — PET scan confirmed (Kim et al., 2011)</p>
</div>

<p>What does reduced D2 receptor availability actually mean? In plain terms: your brain turns down the volume on its own reward receptors. You need <strong>more stimulation to feel the same level of satisfaction</strong>. This is the clinical definition of tolerance, and it is the same mechanism observed in cocaine and alcohol addiction.</p>
<p>Nora Volkow&rsquo;s work at PNAS established that in addicted subjects, drug-induced dopamine increases are &ldquo;markedly blunted compared with controls.&rdquo; The same dampening occurs with digital stimulation. The shift from enjoyment to compulsion &mdash; diminishing pleasure paired with increasing compulsion &mdash; has a precise name: <strong>dopamine tolerance</strong>.</p>

<div class="callout warn">
  <div class="callout-title">The ventral-to-dorsal shift</div>
  <p>Research shows a structural transition in the brain&rsquo;s engagement pattern. Early in addiction, the <strong>ventral striatum</strong> (associated with reward and motivation) drives the behavior. Over time, control shifts to the <strong>dorsal striatum</strong> (associated with habit and automaticity). The behavior transitions from goal-directed to habitual &mdash; you&rsquo;re no longer scrolling because you want to. You&rsquo;re scrolling because the circuit is wired to.</p>
</div>
''')

# ── Section 4: Structural ──
ch('4. Structural Brain Changes', 'ch04.xhtml', '''
<p class="section-number">Mechanism 04</p>
<h2>Structural Brain Changes Under the Scanner</h2>
<p>Neuroimaging studies have moved beyond correlation. Voxel-based morphometry (VBM) meta-analyses now show <strong>consistent, replicable patterns</strong> of gray matter volume reduction in heavy digital consumers.</p>

<div class="brain-region-box">
  <p class="severity-high">High Impact</p>
  <p class="region-name">Anterior Cingulate Cortex (ACC)</p>
  <p class="region-role">Impulse control, error detection, emotional regulation</p>
  <p>Reduced gray matter in bilateral ACC. Loh &amp; Kanai (2014) found reduced GM specifically in frequent media multitaskers. The ACC is the brain&rsquo;s &ldquo;stop and think&rdquo; circuit.</p>
</div>

<div class="brain-region-box">
  <p class="severity-high">High Impact</p>
  <p class="region-name">Dorsolateral Prefrontal Cortex (dlPFC)</p>
  <p class="region-role">Working memory, planning, cognitive flexibility</p>
  <p>Decreased activation during short-form video engagement. The dlPFC governs your ability to hold information, plan ahead, and resist impulses.</p>
</div>

<div class="brain-region-box">
  <p class="severity-high">High Impact</p>
  <p class="region-name">Medial Orbitofrontal Cortex (mOFC)</p>
  <p class="region-role">Decision-making, reward evaluation</p>
  <p>VBM meta-analysis (2026) found consistent GMV reductions in the left mOFC in digital addiction, impairing the ability to weigh long-term consequences against short-term rewards.</p>
</div>

<div class="brain-region-box">
  <p class="severity-medium">Medium Impact</p>
  <p class="region-name">Insular Cortex</p>
  <p class="region-role">Self-awareness, interoception, craving</p>
  <p>Reduced gray matter volume. The insula is involved in conscious awareness of bodily states and cravings &mdash; its impairment may explain why heavy users lose awareness of time passing.</p>
</div>

<div class="brain-region-box">
  <p class="severity-medium">Medium Impact</p>
  <p class="region-name">Lateral Prefrontal Cortex</p>
  <p class="region-role">Cognitive control, executive function</p>
  <p>Longitudinal data shows stronger reduction in cortical thickness over 3 years in high social media users. This is the region responsible for self-regulation.</p>
</div>

<div class="brain-region-box">
  <p class="severity-medium">Medium Impact</p>
  <p class="region-name">Striatum (Caudate &amp; Putamen)</p>
  <p class="region-role">Habit formation, reward processing</p>
  <p>D2 receptor downregulation measured via PET. The striatum&rsquo;s role in habit formation means these changes make the compulsive behavior self-reinforcing.</p>
</div>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_04_gray_matter_loss.png" alt="Brain regions showing gray matter loss in heavy digital consumers" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">Structural brain changes: regions responsible for impulse control, planning, and decision-making are physically shrinking.</p>
</div>

<p>A 2026 meta-analysis in Molecular Psychiatry synthesized VBM data across digital addiction studies and found statistically convergent gray matter reductions in the bilateral ACC, left middle frontal gyrus, and left medial orbitofrontal cortex. These are the same regions implicated in substance addiction.</p>

<div class="callout">
  <div class="callout-title">What this means in plain language</div>
  <p>The brain regions responsible for <strong>stopping yourself</strong>, <strong>thinking ahead</strong>, <strong>staying focused</strong>, and <strong>evaluating consequences</strong> are physically shrinking in heavy users. The regions responsible for <strong>habit</strong> and <strong>compulsion</strong> are becoming dominant. The brain is literally remodeling itself to favor reactive, stimulus-driven behavior over deliberate thought.</p>
</div>
''')

# ── Section 5: Attention ──
ch('5. The Fragmented Mind', 'ch05.xhtml', '''
<p class="section-number">Mechanism 05</p>
<h2>The Fragmented Mind</h2>

<div class="callout">
  <div class="callout-title">Average Human Attention Span (seconds)</div>
  <p>
  2000: 12.0s &nbsp;&nbsp;|&nbsp;&nbsp;
  2015: 8.25s &nbsp;&nbsp;|&nbsp;&nbsp;
  2024: 8.25s &nbsp;&nbsp;|&nbsp;&nbsp;
  2025: 7.97s &nbsp;&nbsp;|&nbsp;&nbsp;
  2026: 7.2s
  </p>
  <p style="font-size:0.85em; color:#777;">Gen Z (18&ndash;24) averages just 5.9 seconds. &mdash; Pew Research Center, January 2026</p>
</div>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_05_fragmented_attention.png" alt="Brain regions affected by attention fragmentation from short-form content" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">The attention trade-off: mPFC overactivated while working memory and inhibition circuits weaken.</p>
</div>

<h3>The Neuroscience of Fragmented Attention</h3>
<p>A 2025 study published in <em>Scientific Reports</em> (Nature) used functional near-infrared spectroscopy (fNIRS) to measure brain activity in college students before and after social media use. The findings were specific:</p>
<ul>
  <li><strong>Reduced accuracy</strong> in executive function tasks (n-back, Go/No-Go paradigms)</li>
  <li><strong>Increased medial prefrontal cortex (mPFC) activation</strong> &mdash; suggesting the brain was working harder just to maintain basic performance</li>
  <li><strong>Decreased dlPFC and vlPFC activation</strong> &mdash; impaired working memory and inhibition</li>
</ul>

<h3>Context Switching Destroys Prospective Memory</h3>
<p>Barton et al. (2025) found that the rapid context-switching inherent in short-form video consumption directly damages <strong>prospective memory</strong> &mdash; your ability to remember to do things in the future. Participants exposed to unlimited context-switching conditions showed &ldquo;significantly deteriorated&rdquo; prospective memory performance.</p>

<h3>Short-Form Video Reduces Analytic Thinking</h3>
<p>Jiang and Ma (2024) demonstrated that even <strong>brief exposure</strong> to TikTok content reduces analytic thinking, promoting intuitive, low-effort cognitive processing. The brain shifts from System 2 (deliberate, analytical) to System 1 (fast, reactive) &mdash; and it stays there even after you close the app.</p>

<div class="callout warn">
  <div class="callout-title">Digital amnesia</div>
  <p>The constant flow of information doesn&rsquo;t allow deep encoding into long-term memory. The brain is forced to repress the rules and objectives of the last task and reload the new one &mdash; a process that is not only resource-consuming but leaves a &ldquo;cognitive residue&rdquo; from the former task that distorts the current one. This is why you can scroll for an hour and remember almost nothing specific afterward.</p>
</div>
''')

# ── Section 6: Deep Reading ──
ch('6. The Death of Deep Reading', 'ch06.xhtml', '''
<p class="section-number">Mechanism 06</p>
<h2>The Death of Deep Reading</h2>
<p>Maryanne Wolf, neuroscientist at UCLA and author of <em>Reader, Come Home</em>, has spent decades studying what happens in the brain during reading. Her central finding is both elegant and troubling: <strong>reading is not a natural human ability</strong>. Unlike speech, which unfolds from genetic blueprints, each human brain must construct its own reading circuit from older cognitive structures.</p>
<p>This circuit, once built, enables what Wolf calls <strong>deep reading</strong> &mdash; the state where a reader connects text to background knowledge, employs inferential and analogical thinking, takes the perspective of the author, and arrives at moments of genuine insight. Deep reading is where empathy, critical thinking, and understanding live in the brain.</p>

<div class="callout insight">
  <div class="callout-title">Wolf&rsquo;s central warning</div>
  <p>&ldquo;The digital age is effectively reshaping the reading circuits in our brains.&rdquo; When the brain adapts to processing information in rapid, shallow bursts, the contemplative dimension &mdash; the capacity to pause, reflect, and form insight &mdash; atrophies. Not because you forgot how to read, but because the neural circuit that enables deep reading is being overwritten by one optimized for scanning and skimming.</p>
</div>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_06_deep_reading_circuit.png" alt="The deep reading neural circuit and its atrophy from digital consumption" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">Wolf's deep reading circuit: a fragile neural network now atrophying as scanning pathways take over.</p>
</div>

<p>Wolf describes this as a &ldquo;hinge moment&rdquo; in human cognitive history. If the deep reading circuit atrophies across a generation, we lose the neurological substrate for empathy, perspective-taking, and resistance to demagoguery. Her proposed solution: <strong>biliteracy</strong> &mdash; build the deep reading circuit through physical books first, then introduce digital media. The order matters because neural circuits, once established, are more resilient.</p>
''')

# ── Section 7: DMN ──
ch('7. Default Mode Network', 'ch07.xhtml', '''
<p class="section-number">Mechanism 07</p>
<h2>Default Mode Network &mdash; What You Lose When You Never Do Nothing</h2>
<p>The Default Mode Network (DMN) is a large-scale brain network &mdash; medial prefrontal cortex, posterior cingulate cortex, precuneus, angular gyrus &mdash; that activates when you are <strong>not focused on the external world</strong>. It&rsquo;s the brain at wakeful rest: daydreaming, self-reflection, remembering the past, planning the future.</p>
<p>The DMN is not idle time. It is where the brain does its most important integrative work: constructing a coherent sense of self, consolidating memories, generating creative connections, and building the internal narrative that makes you <em>you</em>.</p>
<p>Short-form content consumption fills every moment of potential DMN activation. Waiting in line? Scroll. Sitting on the train? Scroll. Lying in bed before sleep? Scroll. The brain never enters the rest state that allows this network to function.</p>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_07_default_mode_network.png" alt="Default Mode Network active during rest versus suppressed during scrolling" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">The Default Mode Network: active during rest and self-reflection, suppressed by constant scrolling.</p>
</div>

<h3>DMN and Reading Comprehension</h3>
<p>Research published in <em>eLife</em> revealed a paradox: the DMN is active during both mind-wandering <em>and</em> deep reading comprehension. In focused readers with good comprehension, the primary visual cortex showed strong functional coupling to DMN regions that support reading. In those who mind-wandered, this coupling weakened. The DMN, properly engaged, is part of the deep reading circuit. Disrupted, it becomes the mechanism of distraction.</p>

<h3>The Consciousness Connection</h3>
<p>The DMN has emerged as a central focus in the neuroscience of consciousness. Research shows that its capacity to act as a &ldquo;global workspace&rdquo; for integrating information is compromised when it cannot activate properly. This is the same network disrupted in disorders of consciousness and under anesthesia. Chronic scrolling doesn&rsquo;t put you under &mdash; but it may be reducing the richness of your conscious experience.</p>
''')

# ── Section 8: Comparison ──
ch('8. How It Compares to Other Addictions', 'ch08.xhtml', '''
<p class="section-number">Mechanism 08</p>
<h2>How It Compares to Other Addictions</h2>

<table>
  <thead>
    <tr><th>Feature</th><th>Substance Addiction</th><th>Short-Form Content</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Reward circuit</strong></td><td>VTA &rarr; nucleus accumbens &rarr; PFC</td><td>Same pathway</td></tr>
    <tr><td><strong>D2 receptor reduction</strong></td><td>~20&ndash;22% (PET confirmed)</td><td>~20% (PET confirmed, Kim 2011)</td></tr>
    <tr><td><strong>Tolerance</strong></td><td>Need higher dose</td><td>Need more novel/extreme content</td></tr>
    <tr><td><strong>Withdrawal</strong></td><td>Physical + psychological</td><td>Psychological (anxiety, restlessness)</td></tr>
    <tr><td><strong>Prefrontal impairment</strong></td><td>Documented across substances</td><td>Documented (fMRI, fNIRS, VBM)</td></tr>
    <tr><td><strong>Habit shift</strong></td><td>Well-established</td><td>Emerging evidence</td></tr>
    <tr><td><strong>Reinforcement schedule</strong></td><td>Variable ratio (gambling) / fixed (drugs)</td><td>Variable ratio (by design)</td></tr>
    <tr><td><strong>Gray matter reduction</strong></td><td>ACC, OFC, PFC</td><td>ACC, OFC, mFG (same regions)</td></tr>
  </tbody>
</table>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_08_addiction_comparison.png" alt="Same reward circuit activated by substance and digital addiction" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">Same brain circuit, different stimulus: identical reward pathways and structural changes.</p>
</div>

<p>The neurological parallel is not metaphorical. Neuroimaging confirms that the same brain circuits, same neurotransmitter systems, and same structural changes observed in substance addiction are present in heavy digital media consumption.</p>

<div class="callout">
  <div class="callout-title">Why &ldquo;digital detoxes&rdquo; don&rsquo;t work</div>
  <p>During abstinence, D2 receptor density begins recovering. But the underlying reinforcement circuits &mdash; cue-reactivity patterns, automated checking behaviors, weakened prefrontal control &mdash; remain intact. When the user re-engages, the original pattern reactivates rapidly because the circuit was <strong>preserved, not dismantled</strong>. The fix requires restructuring the neural architecture, not just removing the stimulus.</p>
</div>
''')

# ── Section 9: Anhedonia ──
ch('9. The Anhedonia Epidemic', 'ch09.xhtml', '''
<p class="section-number">Mechanism 09</p>
<h2>Thrilled to Death &mdash; The Anhedonia Epidemic</h2>

<div class="book-card">
  <p class="book-title">Thrilled to Death: How the Endless Pursuit of Pleasure Is Leaving Us Numb</p>
  <p class="book-author">Dr. Archibald D. Hart &mdash; Clinical psychologist</p>
  <p class="book-thesis">The excessive pursuit of pleasure paradoxically destroys the brain&rsquo;s ability to experience pleasure. We are being thrilled to death &mdash; to the death of our ability to feel genuine joy.</p>
</div>

<p>Hart identified the central paradox years before the short-form video era made it universal: <strong>anhedonia</strong> &mdash; the inability to experience pleasure &mdash; is not caused by too little stimulation. It is caused by too much.</p>
<p>Previously, anhedonia was linked only to severe psychiatric disorders: major depression, schizophrenia, chronic pain states. Hart showed that a subtler, more insidious form was spreading through otherwise healthy populations. Not the clinical inability to feel anything &mdash; but a steady, creeping decline in the ability to find joy in small events and simple experiences.</p>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_09_anhedonia_threshold.png" alt="Hart's rising pleasure threshold model showing healthy, moderate, and heavy use" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">Hart's anhedonia model: dopamine flooding raises the barrier that enjoyment must cross.</p>
</div>

<h3>Hart&rsquo;s Threshold Model</h3>
<p>Dopamine flooding from overstimulation <strong>raises the threshold barrier</strong> that enjoyment must cross to reach the brain&rsquo;s pleasure center. Small pleasures &mdash; a sunset, a conversation, a meal &mdash; no longer clear the bar.</p>

<div class="callout">
  <div class="callout-title">The Rising Pleasure Threshold</div>
  <div class="threshold-text">
  <p><strong>Healthy brain:</strong> Threshold is low &mdash; everyday pleasures register easily.</p>
  <p><strong>Moderate use:</strong> Threshold rises &mdash; some everyday pleasures no longer register.</p>
  <p><strong>Heavy use:</strong> Threshold is high &mdash; almost nothing registers except extreme stimulation.</p>
  </div>
</div>

<h3>&ldquo;Digital Anhedonia&rdquo; &mdash; A New Clinical Concept</h3>
<p>In 2025, a research editorial in <em>Cureus</em> (Lakhan et al.) formally proposed the term <strong>&ldquo;digital anhedonia&rdquo;</strong> &mdash; the diminished ability to find pleasure in real-world experiences after prolonged digital saturation. The authors argued it may be the <strong>first affective disorder of the attention economy</strong>.</p>

<div class="callout warn">
  <div class="callout-title">The misdiagnosis problem</div>
  <p>Clinicians increasingly encounter teens and young adults reporting irritability, poor concentration, disrupted sleep, and social withdrawal. These symptoms are typically interpreted as anxiety, ADHD, or subclinical depression. But a unifying feature is often overlooked: <strong>digital overstimulation and its downstream neurocognitive impact</strong>.</p>
</div>
''')

# ── Section 10: Lembke ──
ch('10. The Pleasure-Pain Seesaw', 'ch10.xhtml', '''
<p class="section-number">Mechanism 10</p>
<h2>The Pleasure-Pain Seesaw</h2>

<div class="book-card">
  <p class="book-title">Dopamine Nation: Finding Balance in the Age of Indulgence</p>
  <p class="book-author">Dr. Anna Lembke &mdash; Medical Director of Addiction Medicine, Stanford University</p>
  <p class="book-thesis">The same brain regions that process pleasure also process pain, and they work like a balance scale. Chase enough highs, and your resting state quietly becomes a low.</p>
</div>

<p>Anna Lembke observed the same mechanism Hart described &mdash; but framed it through an elegant neuroscience principle: <strong>opponent-process theory</strong>.</p>
<p>One of the most important findings in neuroscience in the last 75 years is that the same brain areas that process pleasure also process pain, and they operate like a balance scale. Every pleasurable experience tilts the scale toward pleasure, but the brain actively compensates by pushing it back toward pain to restore equilibrium.</p>

<div class="seesaw-diagram">
  <p style="font-size:1.1em;"><strong>PLEASURE</strong> &nbsp;&nbsp;&harr;&nbsp;&nbsp; <strong>PAIN</strong></p>
  <p style="font-size:0.85em; color:#777;">&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; &#9650; &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;</p>
  <p style="font-size:0.85em; color:#777;">Every dopamine spike is followed by an equal and opposite dip.<br/>
  Chronic overstimulation tilts the resting point toward pain.</p>
</div>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_10_pleasure_pain_seesaw.png" alt="Lembke's pleasure-pain seesaw in three states" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">Lembke's opponent-process model: chronic use shifts the resting point below neutral.</p>
</div>

<p>Every dopamine spike is followed by an equal and opposite dip below baseline. That dip is the moment of restlessness, boredom, or anxiety you feel when you put your phone down. It&rsquo;s the micro-withdrawal that makes you pick it back up. And with chronic overstimulation, the resting point of the balance shifts. Your <strong>baseline mood settles below neutral</strong>.</p>

<div class="callout insight">
  <div class="callout-title">Lembke&rsquo;s key insight</div>
  <p>&ldquo;The smartphone is the modern-day hypodermic needle, delivering digital dopamine 24/7 for a wired generation.&rdquo; Many people struggling with depression, anxiety, insomnia, and low motivation are actually experiencing the consequences of chronic overstimulation &mdash; the addiction is causing the pain, not relieving it.</p>
</div>

<h3>The Counterintuitive Fix: Seek Discomfort</h3>
<p>Lembke&rsquo;s most counterintuitive finding: <strong>deliberate, mild discomfort</strong> &mdash; cold water immersion, intense exercise, fasting &mdash; can help reset the balance. These stressors tip the scale slightly toward pain, and the brain&rsquo;s compensatory rebound pushes back toward pleasure, producing a gentle, natural lift.</p>
<p>Her clinical protocol: a <strong>4-week abstinence period</strong> to allow dopamine receptor density to recover. Patients typically feel worse for the first 2 weeks. By week 4, ordinary experiences &mdash; food, conversation, sunlight &mdash; begin to register as pleasurable again.</p>
''')

# ── Section 11: The Shallows ──
ch('11. The Shallows', 'ch11.xhtml', '''
<p class="section-number">Mechanism 11</p>
<h2>The Shallows &mdash; Neuroplasticity Working Against You</h2>

<div class="book-card">
  <p class="book-title">The Shallows: What the Internet Is Doing to Our Brains</p>
  <p class="book-author">Nicholas Carr &mdash; Pulitzer Prize finalist (2011)</p>
  <p class="book-thesis">Neuroplasticity is a double-edged sword. The brain adapts to whatever you train it on. Train it on shallow, fragmented, hyperlinked content, and it becomes shallow, fragmented, and hyperlinked.</p>
</div>

<p>Carr&rsquo;s argument fills the gap between the dopamine research and the structural brain changes: <strong>neuroplasticity</strong>. The brain is not static. It physically restructures itself based on how you use it. Every hour you spend in one mode of thinking strengthens the neural pathways for that mode and weakens the pathways you aren&rsquo;t using.</p>
<p>This is not metaphor. Brain scientists have demonstrated that even <strong>five hours of internet use</strong> can cause the formation of new neural pathways in non-internet users.</p>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_11_neuroplasticity.png" alt="Neuroplasticity: deep thinking versus shallow processing pathways" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">Carr's thesis: the brain optimizes for what it does most — deep thinking pathways atrophy as shallow ones strengthen.</p>
</div>

<h3>What Gets Stronger vs. What Gets Weaker</h3>
<table>
  <thead>
    <tr><th>Strengthened by digital consumption</th><th>Weakened by digital consumption</th></tr>
  </thead>
  <tbody>
    <tr><td>Cursory reading and scanning</td><td>Deep reading and sustained comprehension</td></tr>
    <tr><td>Hurried, distracted thinking</td><td>Calm, concentrated, deliberate thinking</td></tr>
    <tr><td>Superficial learning (breadth)</td><td>Deep learning (depth)</td></tr>
    <tr><td>Impulsive decision-making</td><td>Deliberate decision-making</td></tr>
    <tr><td>Multitasking</td><td>Single-tasking and flow states</td></tr>
  </tbody>
</table>

<p>Carr identified a critical paradox of neuroplasticity: it provides an escape from genetic determinism, but it also imposes <strong>its own form of determinism</strong>. As particular circuits strengthen through repetition, they transform an activity into a habit.</p>

<div class="callout">
  <div class="callout-title">The hyperlink problem</div>
  <p>Carr cites studies showing that hyperlinks make text <em>harder</em> to understand, not easier. The cognitive load of deciding whether to click is larger than intuition suggests. People skim hypertext and retain less content.</p>
</div>

<p>The key takeaway from Marshall McLuhan: <strong>the medium is the message</strong>. The internet is not just a delivery mechanism for content. It is an environment that restructures the brain for a particular kind of cognition &mdash; fast, shallow, fragmented &mdash; at the expense of another kind: slow, deep, sustained.</p>
''')

# ── Section 12: Brain Fog ──
ch('12. Brain Fog and Slow Recall', 'ch12.xhtml', '''
<p class="section-number">Mechanism 12</p>
<h2>Brain Fog and Slow Recall &mdash; What&rsquo;s Actually Happening</h2>
<p>You know the word. You&rsquo;ve used it a hundred times. It&rsquo;s right there &mdash; but it won&rsquo;t come. Ten minutes later, in the shower, it surfaces effortlessly. This isn&rsquo;t random. It&rsquo;s a specific neurological pattern, and digital overconsumption is making it worse.</p>

<div style="margin: 1.5em 0; page-break-inside: avoid;">
  <img src="images/mechanism_12_brain_fog_retrieval.png" alt="Healthy versus impaired memory retrieval pathway" style="width:100%; height:auto;"/>
  <p style="font-size:0.8em; color:#777; margin-top:0.4em; font-style:italic;">Brain fog is a retrieval problem, not a storage problem — the highway to your memories is congested.</p>
</div>

<h3>The Retrieval Problem (Not a Storage Problem)</h3>
<p>The critical distinction: <strong>the memory exists</strong>. It is encoded and stored. The problem is <em>retrieval</em>. Memory retrieval depends on the <strong>prefrontal cortex</strong> coordinating with the <strong>hippocampus</strong> to reconstruct the distributed pattern of the memory.</p>

<div class="callout">
  <div class="callout-title">Why it comes back later</div>
  <p>The delayed recall you experience &mdash; remembering 10 minutes later, or in the shower &mdash; is the brain completing retrieval through an alternate, slower pathway. The memory was never gone. The highway to it was congested.</p>
</div>

<h3>Why Digital Consumption Causes This</h3>
<ul>
  <li><strong>Prefrontal cortex degradation.</strong> The PFC orchestrates retrieval. Neuroimaging shows 18% decreased PFC activity from dopamine loops, plus gray matter reduction.</li>
  <li><strong>Retrieval muscles atrophied.</strong> You&rsquo;ve outsourced recall to your phone. Every time you Google instead of trying to remember, you skip a retrieval attempt.</li>
  <li><strong>Cognitive residue from context-switching.</strong> Rapid switching leaves fragments of the previous task that interfere with the current one.</li>
  <li><strong>Dopamine-attention coupling disrupted.</strong> Dysregulated dopamine manifests as inattention, which presents as poor memory.</li>
  <li><strong>Shallow encoding from fragmented attention.</strong> Even when information enters memory, it&rsquo;s encoded shallowly because attention was fragmented during learning.</li>
  <li><strong>GABA/glutamate imbalance.</strong> Proton MRS imaging (2025) found that lower GABA and altered glutamate concentrations contribute to slower naming and retrieval interference.</li>
</ul>

<h3>The &ldquo;Tip of the Tongue&rdquo; Epidemic</h3>
<p>The tip-of-the-tongue (TOT) state involves three brain regions: the <strong>anterior cingulate cortex</strong>, the <strong>prefrontal cortex</strong>, and the <strong>insula</strong>. All three show reduced gray matter or reduced activation in heavy digital consumers.</p>

<div class="callout warn">
  <div class="callout-title">The error reinforcement trap</div>
  <p>Research shows that repeated TOT experiences for the same item can become self-reinforcing. The brain develops a maladaptive retrieval pattern where the <em>failure itself</em> becomes part of the memory trace. Breaking this loop requires deliberate retrieval practice.</p>
</div>
''')

# ── Section 13: Recovery ──
ch('13. The Recovery Protocol', 'ch13.xhtml', '''
<p class="section-number">Recovery</p>
<h2>The Recovery Protocol &mdash; What Actually Works</h2>
<p>The same neuroplasticity that created the problem can reverse it. But recovery requires targeted action on the specific circuits that are degraded &mdash; not just &ldquo;use your phone less.&rdquo;</p>

<div class="protocol-card">
  <p><span class="proto-num">1.</span> <span class="proto-title">Structured Stimulation Reduction</span></p>
  <p>Limit entertainment screen time to &le;2 hours/day. Target passive consumption specifically. Protect three windows: <strong>first hour after waking</strong> (no phone), <strong>meals</strong> (screen-free), and <strong>last hour before bed</strong>.</p>
  <p class="proto-evidence">Evidence: RCT showed significant improvements in stress, depression, and sleep quality within 3 weeks.</p>
</div>

<div class="protocol-card">
  <p><span class="proto-num">2.</span> <span class="proto-title">Active Retrieval Practice</span></p>
  <p>Stop Googling things you should know. When a name or word won&rsquo;t come, <strong>sit with the discomfort and keep trying</strong> for at least 60 seconds before looking it up. That struggle is the retrieval circuit being exercised.</p>
  <p class="proto-evidence">Evidence: Roediger &amp; Karpicke (2006) found active recall produced 80% retention after one week vs. 34% for passive re-reading.</p>
</div>

<div class="protocol-card">
  <p><span class="proto-num">3.</span> <span class="proto-title">Exercise (Non-Negotiable)</span></p>
  <p>150+ minutes/week of moderate intensity. In people with depleted dopamine systems, 8 weeks of structured exercise produced a measurable ~14% increase in striatal D2/D3 receptor availability on PET scans.</p>
  <p class="proto-evidence">Evidence: Human PET studies show D2 receptor upregulation in dopamine-depleted populations (Robertson 2016, Fisher 2013).</p>
</div>

<div class="protocol-card">
  <p><span class="proto-num">4.</span> <span class="proto-title">Deliberate Boredom</span></p>
  <p>Build stretches of unstimulated time into every day. No phone, no podcast, no background noise. This re-activates the <strong>Default Mode Network</strong> &mdash; responsible for memory consolidation, self-reflection, and creative connection.</p>
  <p class="proto-evidence">Evidence: DMN activation during wakeful rest is associated with memory consolidation and creative problem-solving.</p>
</div>

<div class="protocol-card">
  <p><span class="proto-num">5.</span> <span class="proto-title">Sleep Hygiene</span></p>
  <p>7&ndash;9 hours per night. No screens for 60 minutes before bed. Sleep is when the hippocampus replays and consolidates the day&rsquo;s memories into long-term storage.</p>
  <p class="proto-evidence">Evidence: Sleep&rsquo;s role in memory consolidation is one of the most robust findings in neuroscience.</p>
</div>

<div class="protocol-card">
  <p><span class="proto-num">6.</span> <span class="proto-title">Deep Reading (30 min/day)</span></p>
  <p>Read physical books for at least 30 minutes daily, without a phone in the room. Start with whatever you can sustain. If 30 minutes feels impossible, that itself is diagnostic.</p>
  <p class="proto-evidence">Evidence: Wolf&rsquo;s research shows the deep reading circuit can be rebuilt through practice.</p>
</div>

<div class="protocol-card">
  <p><span class="proto-num">7.</span> <span class="proto-title">Seek Mild Discomfort</span></p>
  <p>Cold showers, fasting, hard exercise. The brain&rsquo;s compensatory rebound from mild pain produces a gentle, natural dopamine lift &mdash; without the crash.</p>
  <p class="proto-evidence">Evidence: Lembke&rsquo;s clinical practice at Stanford. Opponent-process theory predicts pleasure rebound from controlled pain exposure.</p>
</div>

<div class="protocol-card">
  <p><span class="proto-num">8.</span> <span class="proto-title">Single-Task Everything</span></p>
  <p>Do one thing at a time. No music while reading. No scrolling while watching. Every act of sustained, single-pointed attention is a rep for the prefrontal cortex.</p>
  <p class="proto-evidence">Evidence: Loh &amp; Kanai (2014) found structural ACC reduction in media multitaskers.</p>
</div>

<h3>Recovery Timeline</h3>
<table>
  <thead>
    <tr><th>Phase</th><th>Timeframe</th><th>What Changes</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Withdrawal</strong></td><td>Days 1&ndash;3</td><td>Cravings, restlessness, irritability. This is real withdrawal &mdash; the pain side of Lembke&rsquo;s seesaw overcompensating.</td></tr>
    <tr><td><strong>Stabilization</strong></td><td>Days 4&ndash;7</td><td>Focus and energy begin stabilizing. Sleep quality improves measurably.</td></tr>
    <tr><td><strong>Cognitive return</strong></td><td>Weeks 2&ndash;3</td><td>Noticeable improvement in recall speed, sustained attention, and ability to hold a thought.</td></tr>
    <tr><td><strong>PFC restoration</strong></td><td>Week 4+</td><td>Prefrontal cortex function measurably restored. Decision-making and impulse control improve.</td></tr>
    <tr><td><strong>Structural recovery</strong></td><td>Months 2&ndash;6+</td><td>Gray matter volume changes take longer. Exercise accelerates this.</td></tr>
  </tbody>
</table>

<div class="callout insight">
  <div class="callout-title">The key principle</div>
  <p>Recovery is not about willpower. It&rsquo;s about understanding that <strong>your brain physically restructures based on what you do with it</strong>. The protocol is not a punishment &mdash; it&rsquo;s physical therapy for a brain that has been trained in the wrong direction.</p>
</div>
''')

# ── Section 14: Evidence Quality ──
ch('14. Evidence Quality Assessment', 'ch14.xhtml', '''
<h2>Evidence Quality &mdash; Honest Assessment</h2>
<p>Not all 8 steps rest on equal evidence. Here is an honest grading of each.</p>

<table>
  <thead>
    <tr><th>Step</th><th>Evidence</th><th>What exists</th><th>What doesn&rsquo;t</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Screen time reduction</strong></td>
      <td><span class="phase-badge phase-strong">Strong</span></td>
      <td>Multiple RCTs. Consistent improvements in well-being, mood, sleep.</td>
      <td>Effect sizes small-to-medium. The &le;2 hr threshold is a practical guideline.</td>
    </tr>
    <tr>
      <td><strong>2. Active retrieval</strong></td>
      <td><span class="phase-badge phase-strong">Very strong</span></td>
      <td>One of the most replicated findings in cognitive science. Meta-analyses show g &asymp; 0.50&ndash;0.61.</td>
      <td>Most studies test academic recall, not everyday &ldquo;tip-of-tongue&rdquo; retrieval.</td>
    </tr>
    <tr>
      <td><strong>3. Exercise</strong></td>
      <td><span class="phase-badge phase-mixed">Strong (general) / Mixed (D2)</span></td>
      <td>Exercise improving cognition: extremely robust. D2 upregulation in dopamine-depleted populations: PET evidence exists.</td>
      <td>D2 upregulation in healthy humans: mixed or null results. The &ldquo;40% dopamine increase&rdquo; is from mouse studies.</td>
    </tr>
    <tr>
      <td><strong>4. Deliberate boredom</strong></td>
      <td><span class="phase-badge phase-moderate">Moderate</span></td>
      <td>DMN&rsquo;s role in consolidation and creativity is well-established.</td>
      <td>No RCT has tested &ldquo;deliberate boredom&rdquo; as a cognitive intervention.</td>
    </tr>
    <tr>
      <td><strong>5. Sleep hygiene</strong></td>
      <td><span class="phase-badge phase-strong">Strong</span></td>
      <td>Sleep&rsquo;s role in memory consolidation is robust. Screen light disrupting melatonin is documented.</td>
      <td>The 60-minute cutoff is a clinical recommendation, not a precise finding.</td>
    </tr>
    <tr>
      <td><strong>6. Deep reading</strong></td>
      <td><span class="phase-badge phase-moderate">Moderate</span></td>
      <td>Wolf&rsquo;s neuroscience of the reading circuit is well-established.</td>
      <td>No RCT has tested &ldquo;30 minutes of daily deep reading&rdquo; as rehabilitation.</td>
    </tr>
    <tr>
      <td><strong>7. Mild discomfort</strong></td>
      <td><span class="phase-badge phase-moderate">Moderate</span></td>
      <td>Cold water immersion at 14&deg;C increased plasma dopamine ~250% in one study.</td>
      <td>That study measured plasma catecholamines, not brain dopamine directly.</td>
    </tr>
    <tr>
      <td><strong>8. Single-tasking</strong></td>
      <td><span class="phase-badge phase-weak">Weak (as intervention)</span></td>
      <td>Loh &amp; Kanai (2014) found correlation between multitasking and reduced ACC gray matter.</td>
      <td>Cross-sectional, not causal. No RCT has tested single-tasking as rehabilitation.</td>
    </tr>
  </tbody>
</table>

<div class="callout">
  <div class="callout-title">What this means in practice</div>
  <p>Steps 1, 2, 3 (general), and 5 rest on strong experimental evidence. Steps 4, 6, and 7 are grounded in solid neuroscience but haven&rsquo;t been tested as specific interventions. Step 8 is the weakest as an intervention claim. The honest framing: these are the best-supported actions available given current neuroscience, not a clinically validated treatment protocol.</p>
</div>
''')

# ── Section 15: Sources ──
ch('15. Sources and Key Studies', 'ch15.xhtml', '''
<h2>Key Studies and Research</h2>
<p>The findings above draw from peer-reviewed neuroscience research, systematic reviews, and meta-analyses published in major journals. Selected sources:</p>
<ul class="source-list">
  <li>Kim et al. (2011) &mdash; Reduced striatal dopamine D2 receptors in people with Internet addiction. PET imaging study, PubMed.</li>
  <li>Volkow et al. (2011) &mdash; Addiction: Beyond dopamine reward circuitry. PNAS.</li>
  <li>Fineberg et al. (2022) &mdash; Structural gray matter differences in Problematic Usage of the Internet: meta-analysis. Molecular Psychiatry.</li>
  <li>Montag et al. (2023) &mdash; Neuroimaging the effects of smartphone (over-)use on brain function and structure. Psychoradiology, Oxford Academic.</li>
  <li>Frontiers (2023) &mdash; Impact of digital technology, social media, and AI on cognitive functions. Frontiers in Cognition.</li>
  <li>Engineered highs: Reward variability and frequency as prerequisites of behavioural addiction. ScienceDirect.</li>
  <li>fNIRS assessment: decline in executive function following social media use. Scientific Reports, Nature (2025).</li>
  <li>How short video addiction affects risk decision-making (fNIRS). Frontiers in Human Neuroscience (2025).</li>
  <li>Impact of Short-Form Video Use on Cognitive and Mental Health: Systematic Review. medRxiv (2025).</li>
  <li>Neural, neurotransmitter, and molecular signatures of gray matter alterations in digital addiction. ScienceDirect (2026).</li>
  <li>Modern Day High: The Neurocognitive Impact of Social Media. PMC (2025).</li>
  <li>Perceptual coupling/decoupling of DMN during mind-wandering and reading. eLife.</li>
  <li>Maryanne Wolf &mdash; Reader, Come Home: The Reading Brain in a Digital World.</li>
  <li>Imaging addiction: D2 receptors and dopamine signaling. PMC.</li>
  <li>Human Attention Span Statistics 2026. World Futures Global.</li>
  <li>Archibald D. Hart &mdash; Thrilled to Death (2007).</li>
  <li>Anna Lembke &mdash; Dopamine Nation (2021). Stanford Addiction Medicine.</li>
  <li>Nicholas Carr &mdash; The Shallows (2010). Pulitzer Prize finalist.</li>
  <li>Lakhan et al. (2025) &mdash; Digital Anhedonia as an emerging clinical concept. Cureus.</li>
  <li>Merklein et al. (2025) &mdash; Anhedonia in everyday life. PLOS One.</li>
  <li>Rethinking Pain and Pleasure &mdash; Review of Dopamine Nation. PMC/NIH.</li>
  <li>Mnemonic factors associated with tip-of-the-tongue phenomenon (2025). Scientific Reports, Nature.</li>
  <li>Neural correlates of tip-of-the-tongue states. PMC.</li>
  <li>Understanding Digital Dementia and Cognitive Impact in the Internet Era. PMC (2024).</li>
  <li>How to Break Free From Brain Fog and Digital Overload. Psychology Today (2024).</li>
  <li>Working Memory in the Prefrontal Cortex. PMC.</li>
  <li>Dopamine Fasting: Science, Myths, and How to Reset (Dr. Cameron Sepah, UCSF).</li>
  <li>Screen Time Might Be Shrinking Your Brain. Psychology Today (2025).</li>
</ul>

<hr/>
<footer>
  <p>Compiled August 2026. This briefing synthesizes peer-reviewed neuroscience, neuroimaging meta-analyses, and cognitive science research. It is not medical advice.</p>
</footer>
''')


# ── Build the book ──
book.toc = [epub.Link(c.file_name, c.title, c.file_name.replace('.xhtml','')) for c in chapters]

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

book.spine = ['nav'] + chapters

output_path = '/home/user/AI Projects/brain-consumption-impact/The_Consumed_Mind.epub'
epub.write_epub(output_path, book)
print(f'EPUB written to: {output_path}')
