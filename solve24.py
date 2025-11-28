#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
24ゲーム ソルバー (整数専用版)
- 入力: 1〜9 の数字4つ（例: 5 9 2 5）
- 四則演算 + - * / と丸括弧を使って、ちょうど24を作る式を列挙
- 各数字は1回ずつ使用
- 除算は「割り切れる場合のみ」許可（小数・分数は使わない）
"""

from itertools import permutations
import argparse

TARGET = 24

def combine(a, b):
    """2つの項 (value, expr) を四則で結合して候補を列挙 (整数専用)"""
    (va, ea) = a
    (vb, eb) = b
    out = []
    # 加算
    out.append((va + vb, f"({ea}+{eb})"))
    # 乗算
    out.append((va * vb, f"({ea}*{eb})"))
    # 減算
    out.append((va - vb, f"({ea}-{eb})"))
    out.append((vb - va, f"({eb}-{ea})"))
    # 除算（割り切れる場合のみ）
    if vb != 0 and va % vb == 0:
        out.append((va // vb, f"({ea}/{eb})"))
    if va != 0 and vb % va == 0:
        out.append((vb // va, f"({eb}/{ea})"))
    return out

def solve24(nums):
    """nums: 4つの整数 -> 24になる式(set[str])"""
    items = [(n, str(n)) for n in nums]
    sols = set()

    def dfs(nodes):
        if len(nodes) == 1:
            val, expr = nodes[0]
            if val == TARGET:
                pretty = expr
                if pretty.startswith("(") and pretty.endswith(")"):
                    pretty = pretty[1:-1]
                sols.add(pretty)
            return

        L = len(nodes)
        for i in range(L):
            for j in range(i+1, L):
                rest = [nodes[k] for k in range(L) if k != i and k != j]
                for c in combine(nodes[i], nodes[j]):
                    dfs(rest + [c])

    dfs(items)
    return sols

def main():
    p = argparse.ArgumentParser(description="24ゲーム ソルバー (整数専用版)")
    p.add_argument("digits", nargs=4, type=int, help="1..9 の数字を4つ（例: 5 9 2 5）")
    p.add_argument("--limit", type=int, default=0, help="表示件数の上限（0=無制限）")
    args = p.parse_args()

    sols = sorted(solve24(args.digits))
    if not sols:
        print("解なし（整数だけでは24を作れませんでした）")
        return

    print(f"解 {len(sols)} 件")
    count = 0
    for s in sols:
        print(s)
        count += 1
        if args.limit and count >= args.limit:
            break

if __name__ == "__main__":
    main()
