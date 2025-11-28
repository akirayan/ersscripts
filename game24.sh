#!/bin/bash
# 24ゲーム出題スクリプト (整数専用)
# 大画面にお題を表示して60秒後に解答を表示、その後繰り返す

while true; do
  # ランダムに手札を作る
  HAND=$(shuf -i 1-9 -n 4 | tr '\n' ' ')
  
  # 解があるかチェック（整数専用 solve24_int.py を使う）
  RESULT=$(python3 solve24.py $HAND --limit 1)
  
  if ! echo "$RESULT" | grep -q "解なし"; then
    clear
    echo "🎲 お題: $HAND"
    echo "⏳ 60秒で 24 を作ろう！"
    echo ""
    
    # カウントダウン
    for t in $(seq 60 -1 1); do
      echo -ne "\r残り $t 秒 " 
      sleep 1
    done
    
    echo -e "\n\n✅ 解答例:"
    # python3 solve24.py $HAND --limit 5   # 5個まで表示
    python3 solve24.py $HAND   # 全て表示
    echo ""
    echo "==============================="
    echo "次の問題に進みます（5秒後）"
    sleep 5
  fi
done
