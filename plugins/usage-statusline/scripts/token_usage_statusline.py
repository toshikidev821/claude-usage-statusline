#!/usr/bin/env python3
"""Claude Code statusLine: 公式のプラン使用制限(5時間/7日)を視覚的に表示する。

Claude Code は statusLine コマンドの stdin に、Anthropic側が計算した
正確な rate_limits (five_hour / seven_day の used_percentage・resets_at) を
そのまま渡してくれる。これは claude.ai の「プラン使用制限」パネルと同じ
公式データなので、自前でトークンを数えて推定する必要はない。
"""
import sys
import json
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))

BAR_WIDTH = 10
FILLED = "█"
EMPTY = "░"


def read_stdin_json():
    try:
        if sys.stdin.isatty():
            return {}
        return json.load(sys.stdin)
    except Exception:
        return {}


def bar(fraction):
    fraction = max(0.0, min(1.0, fraction))
    filled_n = round(fraction * BAR_WIDTH)
    return FILLED * filled_n + EMPTY * (BAR_WIDTH - filled_n)


def color_for(pct):
    if pct < 50:
        return "🟢"
    if pct < 80:
        return "🟡"
    return "🔴"


def fmt_remaining(delta):
    total_min = int(delta.total_seconds() // 60)
    if total_min <= 0:
        return "まもなく"
    h, m = divmod(total_min, 60)
    if h > 0:
        return f"{h}時間{m}分"
    return f"{m}分"


def fmt_window(name, window, now, date_fmt):
    if not window:
        return None
    pct = window.get("used_percentage")
    resets_at = window.get("resets_at")
    if pct is None:
        return None
    emoji = color_for(pct)
    piece = f"{emoji} {name} [{bar(pct / 100)}] {pct:.0f}%使用済み"
    if resets_at is not None:
        reset_dt = datetime.fromtimestamp(resets_at, tz=timezone.utc)
        remaining = reset_dt - now
        reset_local = reset_dt.astimezone(JST)
        piece += f" (残り{fmt_remaining(remaining)} / {reset_local.strftime(date_fmt)}リセット)"
    return piece


def main():
    data = read_stdin_json()
    model_name = (data.get("model") or {}).get("display_name") or "Claude"
    rate_limits = data.get("rate_limits") or {}
    now = datetime.now(timezone.utc)

    parts = [f"🤖 {model_name}"]

    five_hour = fmt_window("5h", rate_limits.get("five_hour"), now, "%H:%M")
    seven_day = fmt_window("7d", rate_limits.get("seven_day"), now, "%m/%d %H:%M")

    if five_hour:
        parts.append(five_hour)
    if seven_day:
        parts.append(seven_day)

    if not five_hour and not seven_day:
        ctx = data.get("context_window") or {}
        used = ctx.get("used_percentage")
        if used is not None:
            parts.append(f"🧠 コンテキスト{used:.0f}%使用（プラン使用制限は最初の応答後に表示されます）")
        else:
            parts.append("プラン使用制限データなし")

    print(" | ".join(parts))


if __name__ == "__main__":
    main()
