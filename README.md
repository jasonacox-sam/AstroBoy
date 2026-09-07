# AstroBoy 🚀

**[▶ Play it live](https://s3.amazonaws.com/sam.jasonacox.com-030769147843-us-east-1-an/demos/astroboy/index.html)**

![AstroBoy Start Screen](https://github.com/user-attachments/assets/2a904f69-aa3c-4a83-8cc4-f0355c209b9a)

A floating astronaut boy drifting through space — built with Three.js and served by a simple Python HTTP server.

## How to Play

You're floating in Earth orbit with AstroBoy, and his jetpack is empty. Radio transmissions keep coming in from mission control — but they're encrypted with a **Caesar cipher** (each letter shifted by a fixed number of positions in the alphabet).

1. **Read the transmission** that appears at the bottom of the screen.
2. **Decode the cipher** to reveal the hidden word or phrase.
3. **Type your answer and submit.** Correct? The fuel gauge jumps 25% and you get a satisfying particle burst. 💥
4. **Stuck?** Take a hint — each cipher offers 3 progressive hints.
5. **Solve all four ciphers** to fill the tank to 100%. AstroBoy's thrusters glow brighter as fuel builds, and when you're full: blastoff! He launches off-screen on a victory run through Earth Orbit → Red Planet → Ice World → Nebula → Home. 🌟

No time limit, no lives — just you, the stars, and some old-school cryptanalysis.

## Run it locally

```bash
python3 app.py
```

Then open http://localhost:8080

## Stack

- **Three.js** — 3D rendering in the browser
- **Python stdlib** — `http.server`, no dependencies

## Contributing

Found a bug or want to add a feature? Open an issue!
