# Deadlock in Python (Safe Demonstration)

## 📌 Objective
To understand deadlock and demonstrate how it can be avoided using timeout.

## 🔒 What is Deadlock?
Deadlock occurs when two or more threads wait indefinitely for each other’s resources.

## ⚠️ Scenario
Thread 1 → holds Lock1, waits for Lock2  
Thread 2 → holds Lock2, waits for Lock1  

##  Solution Used
Timeout-based locking to avoid deadlock.

## Learning
Deadlock can be avoided by proper resource handling strategies.

## Run
python deadlock.py
