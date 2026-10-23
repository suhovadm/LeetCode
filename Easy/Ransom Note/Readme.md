* Решение методом Replace. Не самое эффективное, но тем неменее.  

383. Записка о выкупе (Ransom Note)  

Дано.  
Даны две строки ransomNote и magazine.  
Верните true, если строку ransomNote можно составить, используя буквы из строки magazine, и false в противном случае.  
Каждую букву из строки magazine можно использовать в строке ransomNote только один раз.  

Примеры.  

Пример 1.  

Ввод: ransomNote = "a", magazine = "b"  
Вывод: false // Нельзя, потому что в magazine только "B".  

Пример 2.  

Ввод: ransomNote = "aa", magazine = "ab"  
Вывод: false // Нельзя, потому что в magazine только одна "A", а мне нужно 2 "A".  

Пример 3.  

Ввод: ransomNote = "aa", magazine = "aab"  
Вывод: true // Можно, потому что мне нужно 2 "A" и в magazine 2 "A", а "B" можно просто выкинуть.  
