
---

# 🎥 Manim Practice Codes

This repository contains my practice scripts created using [Manim](https://www.manim.community/), a mathematical animation engine.  
Each script demonstrates a specific mathematical or animation concept, along with generated outputs in GIF formats

---

## 📂 Folder Structure

manim-practice/ │ ├── README.md               # This file ├── requirements.txt        # Python dependencies ├── .gitignore              # Ignore unnecessary files │ ├── src/                    # All Python scripts │   ├── animate.py │   ├── circle.py │   ├── example.py │   ├── mobjects.py │   ├── rotations.py │   ├── square.py │   ├── transform.py │   └── twotransform.py │ ├── media/                  # Animation outputs │   ├── gifs/               # Optimized GIF previews for README │   │   ├── animate.gif │   │   ├── circle.gif │   │   ├── example.gif │   │   ├── mobjects.gif │   │   ├── rotations.gif │   │   ├── square.gif │   │   ├── transform.gif │   │   └── twotransform.gif │   └── videos/             # High-quality MP4 downloads │       ├── animate.mp4 │       ├── circle.mp4 │       ├── example.mp4 │       ├── mobjects.mp4 │       ├── rotations.mp4 │       ├── square.mp4 │       ├── transform.mp4 │       └── twotransform.mp4 │ └── docs/                   # Extra explanations (optional) ├── how-to-run.md └── concepts.md

---

## ⚙️ Installation
1. Clone this repository:
```bash
git clone https://github.com/your-username/manim-practice.git
cd manim-practice
```
2. Install dependencies:


```bash
pip install -r requirements.txt
```

---

▶️ Running a Script

Use the Manim CLI to render any animation:
```bash
manim -pql src/animate.py AnimateScene
```
Options:

-p → Play after rendering

-ql → Render in low quality (faster)

Replace AnimateScene with the actual scene class name in the script.



---

📜 Codes & Previews

<details>
<summary>Animate</summary>animate.py

Download MP4

</details><details>
<summary>Circle</summary>circle.py

Download MP4

</details><details>
<summary>Example</summary>example.py

Download MP4

</details><!-- Repeat for other scripts -->
---

🎯 Why GIFs for README?

Autoplay & loop directly on GitHub

No need to click or download

Smaller file size (if optimized)


To convert MP4 to GIF:

ffmpeg -i input.mp4 -vf "fps=20,scale=640:-1:flags=lanczos" -loop 0 output.gif


---

📜 License

This project is licensed under the MIT License.

---

This version:
- Looks **professional** yet beginner-friendly.  
- Keeps **folder structure visible**.  
- Has **dropdowns** for each script with GIF preview + MP4 download link.  
- Adds a **conversion command** for GIFs without the casual conversation style.  

If you want, I can **auto-generate the `<details>` dropdown list for all your scripts** so you don’t have to manually write them for each file. Would you like me to do that next?
