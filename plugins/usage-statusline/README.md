# Usage Statusline

Claude Code のステータスラインに、公式のプラン使用制限（5時間 / 7日ウィンドウ）を
プログレスバー付きで表示するプラグインです。

```
🤖 Fable 5 | 🟢 5h [█░░░░░░░░░] 10%使用済み (残り3時間38分 / 14:30リセット) | 🟢 7d [███░░░░░░░] 26%使用済み (残り15時間8分 / 08/18 02:00リセット)
```

## 特徴

- Claude Code が statusLine コマンドの stdin に渡す **公式の `rate_limits` データ**
  （`five_hour` / `seven_day` の `used_percentage` と `resets_at`）をそのまま表示。
  claude.ai の「プラン使用制限」パネルと同じ値なので、自前のトークン推定は不要
- 使用率に応じた色分け: 🟢 50%未満 / 🟡 50〜79% / 🔴 80%以上
- リセットまでの残り時間と、リセット時刻（JST）を表示
- rate_limits が未取得の間はコンテキスト使用率をフォールバック表示

## インストール

```
/plugin marketplace add toshikidev821/claude-usage-statusline
/plugin install usage-statusline@toshikidev821-plugins
```

インストール後、Claude Code 内で次を実行:

```
/usage-statusline:install
```

同梱スクリプトが `~/.claude/scripts/` にコピーされ、`~/.claude/settings.json` の
`statusLine` に登録されます。

## 動作要件

- Python 3（macOS / Linux 標準の `python3` で動作。外部依存なし）
- Claude Code の statusLine 対応バージョン

## 手動設定

プラグインを使わず手動で設定する場合は、`scripts/token_usage_statusline.py` を
任意の場所に置き、`~/.claude/settings.json` に以下を追加してください:

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 /path/to/token_usage_statusline.py",
    "refreshInterval": 5
  }
}
```

## ライセンス

MIT
