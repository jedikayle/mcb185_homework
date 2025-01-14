gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -E "^[rznoica]+$" | grep -E "^.{4,}$" | head -50
