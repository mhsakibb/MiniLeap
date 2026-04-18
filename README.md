MiniLeap — Game Design Document (GDD)
Overview
Title: MiniLeap | Engine: Python + PyOpenGL (GLUT) | Single File, No External Assets
Premise: MiniLeap the cat is disturbed from sleep by a fly, chases it, and runs through 3 themed worlds collecting coins and avoiding obstacles.

Screen Flow
Splash → Story → Instructions → Main Menu → [Level Select Confirm] → Gameplay → Game Over → Main Menu

Characters & Assets (All Code-Rendered)
MiniLeap Cat — orange pixel-art cat with animated running legs, tail, ears, eyes. Jump pose changes leg position.
Obstacles per level:
WorldObstacle 1Obstacle 2Obstacle 3JungleBrown wooden log (round)Rock/stoneMine bomb (instant death)Ice KingdomSnowy log (white-scratched)Ice rockIce cactus (yellow liquid, instant death)UndergroundMuddy logCave rockMine bomb
Collectibles:

Gold coin (all levels) → +1 score per collect
Recovery Star → appears after injury, collect to reduce injury count by 1

Injury system: 3 hits = Game Over (mine/cactus = instant death regardless)

Level Backgrounds (All Code-Drawn)
Jungle: Multi-layer silhouettes — dark foreground palms/ferns, mid olive canopy trees, distant light-green hills. Green grass floor with scrolling trees.
Ice Kingdom: Dark teal→navy sky with stars. Distant jagged ice-mountain silhouette (dark gray-blue body, white/light-blue caps). White-blue ground. Snow-dusted logs.
Underground: Deep cave with teal/blue-purple crystal foreground layers, pink/purple mid crystals, light-purple distant crystals. Stalactites from ceiling. Underground rail-line floor.
Weather (Jungle only): Occasional rain — randomly spawning falling droplets, not too fast. Purely cosmetic.

Gameplay Rules

Speed: starts easy, gradually increases (Easy→Medium→Hard)
Jump: Space (single or double, up to 2 jumps in air)
Coins: random heights, +1 each
Stars: spawn after injury at a reachable position
Game Over screen: score shown, R=Restart, Space=Main Menu


Now, the full code:Ran 3 commands, viewed a file, created a fileRan 3 commands, viewed a file, created a file1,348 lines — fully syntax-verified. Here's your complete GDD recap + what's implemented:

What's in the code
Screen 1 — Cosmic Splash
Animated starfield with twinkling + nebula blobs, the cat character bobbing in the center, rotating star ring, pulsing "MINILEAP" title, blinking "Press SPACE" prompt.
Screen 2 — Story (3 phases)
Phase 1: Cat sleeping with floating Z/z/Z. Phase 2: Fly buzzing around the annoyed cat (fly has wing-flap animation). Phase 3: Cat chasing fly in a running loop — then auto-advances to Instructions.
Screen 3 — Instructions
Cards for Jump / Double Jump / Collect / Danger, with injury heart icons and an animated cat demo.
Screen 4 — Main Menu
3 clickable level cards (mouse click + keyboard 1/2/3) with mini scene previews, animated pulsing borders, and a cat walking across the bottom.
Screen 5 — Confirm popup
"Are you Ready? / Press SPACE" with bouncing cat.
Gameplay (all 3 levels)

Parallax-scrolling backgrounds — Jungle (palm silhouettes, canopy trees, ferns, sun, optional rain), Ice Kingdom (teal→navy sky, stars, aurora, jagged ice mountains with white caps, snowy ground + bumps), Underground (crystal layers in teal/purple/pink, stalactites, rail line with sleepers)
3 obstacle types per level with full unique art (logs, rocks, mines/ice-cactus)
Spinning coin animation, glowing star power-up
Double jump, injury hearts, explosion particles, speed scaling Easy→Medium→Hard
Game Over overlay with coin count, R=Restart, Space=Main Menu
