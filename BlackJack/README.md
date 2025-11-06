# 🃏 Blackjack Game (Python Starter Project)

Welcome to your **Blackjack Project**!  
In this challenge, you’ll be building a command-line version of the classic card game **Blackjack**.

---

## 🎯 Objective

Use your Python skills to complete a fully working **Blackjack CLI game**.  
You’ll start from the given `game.py` template and fill in the missing logic (marked with `TODO` comments).

---

## 🧠 Game Rules

1. The deck is **unlimited** in size.
2. There are **no Jokers**.
3. Jack, Queen, and King count as **10**.
4. Ace can count as **11 or 1**, depending on the total score.
5. Cards are **not removed** from the deck after being drawn.
6. A **Blackjack** is when the first two cards total **21**.

---

## 🗂️ Project Files

blackjack/
│
├── game.py # Main starter code (you will complete this)
├── art.py # Contains ASCII art logo (you’ll create this)
└── README.md # Project instructions (this file)

## 🎮 Example Game Play

 ____  _            _        _            _    
| __ )| | __ _  ___| | __   / \   ___ ___(_)___ 
|  _ \| |/ _` |/ __| |/ /  / _ \ / __/ __| / __|
| |_) | | (_| | (__|   <  / ___ \ (__\__ \ \__ \
|____/|_|\__,_|\___|_|\_\/_/   \_\___|___/_|___/

Your cards: [10, 6], current score: 16
Computer's first card: 7
Type 'y' to get another card, 'n' to pass: y
You drew a 5.
Your new total is 21. You win! 🎉

## 🚀 How to Run the Game

1. **Clone or download** this repository.

   ```bash
    git clone https://github.com/yourusername/blackjack-starter.git
    cd blackjack-starter
    python3 game.py
