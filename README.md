# FRACTALS-PART-01
***Interactive fractal generator built with Python &amp; Pygame — includes L-systems, Pythagoras trees, and Sierpinski triangle with live animation and video export.***

# 🌿 Fractal Generator (Python + Pygame)*

Interactive fractal visualizer and animation tool built with Python and Pygame.  
Includes several classic fractals and the ability to create your own L-systems with live animation and video export.

---
---
## 🍃 Features*

- 🍏 Real-time fractal growth (W / S to control)  
- 🌳 Pythagoras tree, ♻️ Sierpinski triangle, 🌿 L-systems (custom rules)  
- 🍈 Automatic recording — saves .mp4 in /records  
- 🍐 Adjustable iterations, step size, and angles  
- 🥑 Dynamic scaling for all fractals

---
---
## 🧩 Project Structurefractals/*

    fractals_01/
    │
    └── fractals/
    │    ├── main.py
    │    ├── tree_pifagor.py
    │    ├── sapfinski.py
    │    ├── l_systems.py
    │
    ├── rules/
    │    └── lsystem_rules.py
    │
    └── records/

---
---
## ✳️ Controls*

| Key     | Action               |
| ------- | ---------------------|
| 1   | Run Sierpinski triangle  |
| 2   | Run Pythagoras tree      |
| 3   | Run preset L-system      |
| 4   | Run custom L-system      |
| W   | Grow the fractal         |
| S   | Shrink or reverse growth |
| A, D | Сhanging the angle of the Pythagorean tree |
| Mouse Scroll   | Сhanging the color and increasing/decreasing the Serbian triangle |
| ESC | Quit the current fractal |

---
---
## 🌱 Installation*
### 1️⃣ Clone the repository
```bush
git clone https://github.com/gasich27/fractals_01.git
cd fractals
```

### 2️⃣ Install dependencies
```bush
pip install -r requirements.txt
```

### 3️⃣ Run the project
```bush
python -m fractals.main
```

---
---
## 🍀 Example L-System Rule*
```bush
"bush": {
        "axiom": "X",
        "rules": {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"},
        "angle": 18
    }
```

<img width="1251" height="702" alt="Снимок экрана 2025-11-10 014655" src="https://github.com/user-attachments/assets/7eed7fde-4ce1-4a03-846c-c2f8e9101bc2" />

---
---
## 💮 Future Plans* 

  *** Add more and more fractals.  
  *** Add GUI adding l-systems rules.  
  *** Add a generation site with the ability to download.  
  *** Add music generation.  
  *** Add the combination of fractal rules.  
  *** Add volume fractals.  
  *** Article on the application of fractals in technical systems and AI.

---
---
## ⚪ Author*
  GitHub: https://github.com/gasich27  

---
  <p align="center">
  <img width="591" height="48" alt="ñ÷ `B q7`NjzR1 yiD zE1`Mj#j´ `B 2^3HhU (3)" src="https://github.com/user-attachments/assets/61a952ca-2c74-4905-b852-7049d0a1b36a" />
</p>


